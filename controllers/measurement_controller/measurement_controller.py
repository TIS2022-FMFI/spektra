from PySide6 import QtCore
from PySide6.QtCore import QObject, Signal, QThread, QTimer

from errors.data_processing_error import DataProcessingError
from models.motor.Motor import Motor
from models.lockin.constants import *
from models.lockin.lockin import SR510
from models.disperse_element import Grating
from models.logger.constants import *
from models.data_processing.dataProcessing import DataProcessing

from time import sleep
from serial.tools import list_ports


class MeasurementController(QObject):
    state_s = Signal(str)
    progress_s = Signal(float)
    voltmeter_status_s = Signal(bool)
    measured_value_s = Signal(float, float, bool)
    new_measurement_started_s = Signal()
    lockin_settings_s = Signal(dict)
    measurement_start_fail_s = Signal()
    motor_move_to_pos_s = Signal(int, bool)

    def __init__(self):
        super(MeasurementController, self).__init__()
        self.data_processing_controller = None
        self.logger = None
        self.current_motor_angle = None
        self.running = False
        self._lockin = None
        self._motor = Motor()
        self._elem = None
        self.correction = 0
        self.integrations = 1

        # temporary hopefuly
        self.sr510_cable_serial_number = 'A7CB1935A'

        self.lockin_comport = None
        self.motor_comport = None

        self.lockin_motor_connected_check = QTimer()
        self.lockin_motor_connected_check.timeout.connect(self.check_periphery)
        self.lockin_motor_connected_check.start(750)

        self._measurement_thread = QThread()
        self._measurement_thread.setPriority(QThread.HighestPriority)
        self._measurement_thread.finished.connect(self._measurement_thread.deleteLater)
        self.moveToThread(self._measurement_thread)
        self._measurement_thread.start()

    def check_periphery(self):
        maybe_motor_comport_listed = []
        found_lockin = False
        for comport in list_ports.comports():
            if comport.serial_number == self.sr510_cable_serial_number:
                found_lockin = True
                self.lockin_comport = comport.name
                if self._lockin is None:
                    self.connect_lockin()

                self.voltmeter_status_s.emit(True)
                continue
            maybe_motor_comport_listed.append(comport)

        if not self._motor.connected and len(maybe_motor_comport_listed) == 1:
            self.motor_comport = maybe_motor_comport_listed[0].name
            self._motor.connect(self.motor_comport)
            self.logger.log(INFO, f"Pripojený {self.motor_comport}. Predpokladá sa, že je to krokový motor.")

        if not found_lockin:
            self._lockin = None
            self.voltmeter_status_s.emit(False)

    def lockin_read_setting_safely(self, setting):
        try:
            self._lockin.read_setting(setting)
        except Exception as e:
            self.logger.log(CRITICAL, e)

    def get_important_lockin_values(self):
        data = {setting: self.lockin_read_setting_safely(setting) for setting in ALL_SETTINGS}
        self.lockin_settings_s.emit(data)

    def connect_lockin(self):
        try:
            self._lockin = SR510(self.lockin_comport)
        except Exception as e:
            self.logger.log(CRITICAL, e)

        self.get_important_lockin_values()

    def link_data_processing_controller(self, dpc):
        self.data_processing_controller = dpc

    def link_logger(self, log):
        self.logger = log

    @QtCore.Slot(str)
    def set_disperse_element(self, name):
        self._elem = Grating(name)

    def adjust_sensitivity(self, measured_value):
        if measured_value < 0:
            return

        cur_gain = self._lockin.current_gain_value()
        print(f'namerana hodnota: {measured_value}, current sensitivity {cur_gain} ')

        if measured_value >= 0.7 * cur_gain:
            self._lockin.lower_gain()
            ptc = self._lockin.get_pre_time_const()
            sleep(3 * ptc)
            print(f'Zosilnenie sa znizilo na {self._lockin.current_gain_value()}')
        elif measured_value <= 0.2 * cur_gain:
            self._lockin.higher_gain()
            ptc = self._lockin.get_pre_time_const()
            sleep(3 * ptc)
            print(f'Zosilnenie sa zvysilo na {self._lockin.current_gain_value()}')

    def save_and_show_measurement(self, elem, value, correction):
        angle = self.current_motor_angle
        wavelength = elem.angleToWavelength(angle) + correction

        try:
            self.data_processing_controller.data_processing.add_measurement(angle, wavelength, value)
        except DataProcessingError as e:
            self.logger.log(WARNING, e.message)
            return

        self.measured_value_s.emit(wavelength, value)

    def failed_measurement(self, msg):
        self.logger.log(WARNING, msg)
        self.measurement_start_fail_s.emit()

    @QtCore.Slot(float, int)
    def set_arguments(self, correction, integrations):
        self.correction = correction
        self.integrations = integrations

    @QtCore.Slot(float, float, int)
    def start(self, start, end, steps_per_data_point):
        if self._lockin is None:
            self.failed_measurement("Lockin nie je pripojený.")
            return

        if not self._motor.connected:
            self.failed_measurement("Motor nie je pripojený.")
            return

        if self._elem is None:
            self.failed_measurement("Nie je vybraný žiadny disperzný prvok.")
            return

        if self.current_motor_angle is None:
            self.failed_measurement("Poloha motora nie je inicializovaná.")
            return

        distance = end - start
        if distance <= 0:
            self.failed_measurement("Začiatok merania musí by menší ako koniec merania.")
            return

        if start != self.current_motor_angle:
            self.move_to_pos(start, False)

        self._lockin.prepare()
        self.get_important_lockin_values()

        try:
            self.data_processing_controller.data_processing.create_new_file()
        except DataProcessingError as e:
            self.failed_measurement(e.message)
            return

        self.new_measurement_started_s.emit()
        self.running = True
        self.progress_s.emit(0)

        elem = self._elem
        correction = self.correction
        integrations = self.integrations
        steps = elem.angleToSteps(distance)
        last_step = steps % steps_per_data_point
        data_points = steps // steps_per_data_point

        print(f"dist: {distance} \nsteps: {steps} \nvalues: {data_points}")

        anglePerDataPoint = elem.stepsToAngle(steps_per_data_point)

        measured_value = self._lockin.read_value()
        self.save_and_show_measurement(elem, measured_value, correction)

        for i in range(data_points):
            if self.running is False:
                self.aborted_measurement()
                return

            self.progress_s.emit(i / data_points * 100)
            print(f"iter: {i}")

            measured_values = [self._lockin.read_value() for _ in range(integrations)]
            measured_value = sum(measured_values) / len(measured_values)

            self.save_and_show_measurement(elem, measured_value, correction)
            self.adjust_sensitivity(measured_value)

            duration = self._motor.move_forward(steps_per_data_point)
            sleep(duration)
            self.current_motor_angle += anglePerDataPoint

            print(f"pos: {self.current_motor_angle:.3f} measurement: {measured_value}")

        if last_step > 0 and self.running:
            duration = self._motor.move_forward(last_step)
            sleep(duration)
            self.current_motor_angle += elem.stepsToAngle(last_step)

            measured_values = [self._lockin.read_value() for _ in range(integrations)]
            measured_value = sum(measured_values) / len(measured_values)

            self.save_and_show_measurement(elem, measured_value, correction)
            self.adjust_sensitivity(measured_value)

            print(f"pos: {self.current_motor_angle:.3f} measurement: {measured_value}")

        self.progress_s.emit(100)
        self.running = False

    @QtCore.Slot()
    def stop(self):
        self.running = False

    @QtCore.Slot(float)
    def move_to_pos(self, end_angle, from_gui=True):
        if self.current_motor_angle is None:
            self.logger.log(WARNING, "Poloha motora nie je inicializovaná.")
            return

        if not self._elem.is_angle_within_min_max(end_angle):
            if not from_gui:
                self.failed_measurement("Pokúšaš sa posunúť mimo rozsah mriežky")
            else:
                self.logger.log(WARNING, "Pokúšaš sa posunúť mimo rozsah mriežky")
            return

        if from_gui and self.running:
            self.logger.log(WARNING, "Nemôžeš hýbať motorom počas merania.")
            return

        if self.current_motor_angle == end_angle:
            return


        distance = end_angle - self.current_motor_angle
        steps = self._elem.angleToSteps(abs(distance))
        forward = distance > 0

        self.motor_move_to_pos_s.emit(steps, forward)

    @QtCore.Slot(int, bool)
    def confirmed_move_to_pos(self, steps, forward):
        print('moving confirmed')
        if forward:
            self.moveForward(steps)
        else:
            self.moveReverse(steps)

    @QtCore.Slot(int)
    def moveForward(self, steps):
        if not self._motor.connected:
            self.logger.log(WARNING, "Motor nie je pripojeny")
            return
        print(f'moveF je uspesny, pocet krokov: {steps}')
        self._motor.move_forward(steps)

    @QtCore.Slot(int)
    def moveReverse(self, steps):
        if not self._motor.connected:
            self.logger.log(WARNING, "Motor nie je pripojeny")
            return
        print(f'moveR je uspesny, pocet krokov: {steps}')
        self._motor.move_reverse(steps)

    @QtCore.Slot(float)
    def initialization(self, pos):
        self.current_motor_angle = pos

    def exit(self):
        self._measurement_thread.quit()
        self._measurement_thread.wait()

    def aborted_measurement(self):
        pass
