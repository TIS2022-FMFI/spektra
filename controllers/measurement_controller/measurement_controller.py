from PySide6 import QtCore
from PySide6.QtCore import QObject, Signal, QThread, QTimer

from errors.data_processing_error import DataProcessingError
from models.motor.Motor import Motor
from models.lockin.constants import *
from models.lockin.lockin import Lockin
from models.disperse_element import Grating
from models.logger.constants import *

from time import sleep
from serial.tools import list_ports


class MeasurementController(QObject):
    state_s = Signal(str)
    progress_s = Signal(float)
    voltmeter_status_s = Signal(bool)
    measured_value_s = Signal(float, float, bool)
    measurement_started_s = Signal()
    measurement_ended_s = Signal(float)
    lockin_settings_s = Signal(dict)
    measurement_start_fail_s = Signal()
    motor_move_to_pos_s = Signal(int, bool)


    def __init__(self):
        """
        initializes measurement controller object
        """
        super(MeasurementController, self).__init__()
        self.data_processing = None
        self.logger = None
        self.current_motor_angle = None
        self.running = False
        self._lockin = Lockin('SR510')
        self._motor = Motor()
        self._elem = None
        self.correction = 0
        self.integrations = 1

        # temporary hopefuly
        self.SR510_cable_serial_number = 'A7CB1935A'

        self.lockin_cable_info = None
        self.motor_cable_info = None

        self.lockin_motor_connected_check = QTimer()
        self.lockin_motor_connected_check.timeout.connect(self.check_periphery)
        self.lockin_motor_connected_check.start(750)

        self._measurement_thread = QThread()
        self._measurement_thread.setPriority(QThread.HighestPriority)
        self._measurement_thread.finished.connect(self._measurement_thread.deleteLater)
        self.moveToThread(self._measurement_thread)
        self._measurement_thread.start()

    @QtCore.Slot(int)
    def set_lockin_min_auto_sensitivity(self, value):
        if self._lockin.can_auto_switch():
            self._lockin.set_min_auto_sensitivity(value)

    def comport_cable_info(self, comport):
        return f'{comport.vid}:{comport.pid}:{comport.serial_number}'

    @QtCore.Slot(str, str)
    def new_comports_chosen(self, lockin_comport_name, motor_comport_name):
        print(lockin_comport_name, motor_comport_name)
        for comport in list_ports.comports():
            if comport.name == lockin_comport_name:
                self.lockin_cable_info = self.comport_cable_info(comport)
            elif comport.name == motor_comport_name:
                self.motor_cable_info = self.comport_cable_info(comport)

        self._lockin.disconnect()
        self._motor.disconnect()

    def check_periphery(self):
        """
        check if motor and lockin are connected and connect them
        """

        found_lockin_cable = False
        found_motor_cable = False

        for comport in list_ports.comports():
            if self.comport_cable_info(comport) == self.lockin_cable_info:
                found_lockin_cable = True
                if self._lockin.connected is False:
                    try:
                        self._lockin.connect(comport.name)
                        self.get_important_lockin_values()
                        self.voltmeter_status_s.emit(True)
                    except Exception as e:
                        self.logger.log(CRITICAL, f"Chyba pri pripajaní lockinu: {e}")
            elif self.comport_cable_info(comport) == self.motor_cable_info:

                found_motor_cable = True
                if self._motor.connected is False:
                    try:
                        self._motor.connect(comport.name)
                    except Exception as e:
                        self.logger.log(CRITICAL, f"Chyba pri pripajaní krokového motora: {e}")

        if not found_motor_cable:
            if self._motor.connected:
                self.logger.log(WARNING, "Motor bol odpojený")
            self._motor.disconnect()

        if not found_lockin_cable:
            self._lockin.disconnect()
            self.voltmeter_status_s.emit(False)

    def lockin_read_setting_safely(self, setting):
        try:
            return self._lockin.read_setting(setting)
        except Exception as e:
            self.logger.log(CRITICAL, e)

    def get_important_lockin_values(self):
        """
        get/load lockin parameters
        """
        data = {setting: self.lockin_read_setting_safely(setting) for setting in SETTINGS_IN_GUI}
        self.lockin_settings_s.emit(data)

    def link_data_processing_controller(self, dpc):
        """
        connect data processing controller object
        @param dpc: data processing controller
        """
        self.data_processing = dpc

    def link_logger(self, log):
        """
        connect data logger controller object
        @param log: logger controller
        """
        self.logger = log

    @QtCore.Slot(str)
    def set_disperse_element(self, name):
        """
        set disperse element
        @param name: name of disperse element
        """
        self._elem = Grating(name)

    def adjust_sensitivity(self, measured_value):
        """
        adjust lockin sensitivity, based on measured value
        @param measured_value: current measured value
        """
        if measured_value < 0:
            return

        cur_gain = self._lockin.current_gain_value()
        print(f'namerana hodnota: {measured_value}, current sensitivity {cur_gain} ')

        if measured_value >= 0.7 * cur_gain:
            self._lockin.lower_gain()
            ptc = self._lockin.read_setting(PRE_TIME_CONST)
            sleep(3 * ptc)
            print(f'Zosilnenie sa znizilo na {self._lockin.current_gain_value()}')
        elif measured_value <= 0.2 * cur_gain:
            self._lockin.higher_gain()
            ptc = self._lockin.read_setting(PRE_TIME_CONST)
            sleep(3 * ptc)
            print(f'Zosilnenie sa zvysilo na {self._lockin.current_gain_value()}')

    def save_and_show_measurement(self, elem, value, correction):
        """
        send measurement to data processing controller
        @param elem: used grid
        @param value: measured value at concrete angle
        @param correction: used correction of measurement
        @raise data_processing_error: raises an exception when trying to send measuremnt
        """
        angle = self.current_motor_angle
        wavelength = elem.angleToWavelength(angle) + correction

        try:
            self.data_processing.add_measurement(angle, wavelength, value)
        except DataProcessingError as e:
            self.logger.log(WARNING, e.message)
            return

        self.measured_value_s.emit(wavelength, value, True)

    def failed_measurement(self, msg):
        """
        failed measurement
        @param msg: message to show when failed measurement
        """
        self.logger.log(WARNING, msg)
        self.measurement_start_fail_s.emit()

    @QtCore.Slot(float, int)
    def set_arguments(self, correction, integrations):
        """
        set additional measurement arguments
        @param correction: correction value for given measurement
        @param integrations: integration value for given measurement
        """
        self.correction = correction
        self.integrations = integrations

    @QtCore.Slot(float, float, int)
    def start(self, start, end, steps_per_data_point):
        """
        start overall measurement
        @param start: start position of measurement (angle)
        @param end: end position of measurement (angle)
        @param steps_per_data_point: number of step per one measured value
        @raise data_processing_error: raises an exception when trying to start measurement
        """
        if not self._lockin.connected:
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
            self.failed_measurement("Nastavte motor na štartovaciu pozíciu merania")
            return
            #self.move_to_pos(start, False)

        self._lockin.prepare()
        self.get_important_lockin_values()

        try:
            self.data_processing.create_new_file()
        except DataProcessingError as e:
            self.failed_measurement(e.message)
            return

        self.measurement_started_s.emit()
        self.running = True
        self.progress_s.emit(0)

        elem = self._elem
        correction = self.correction
        integrations = self.integrations
        steps = elem.angleToSteps(distance)
        last_step = steps % steps_per_data_point
        data_points = steps // steps_per_data_point

        print(f"dist: {distance} \nsteps: {steps} \nvalues: {data_points}")

        angle_per_data_point = elem.stepsToAngle(steps_per_data_point)

        for i in range(data_points):
            if self.running is False:
                self.measurement_ended()
                return

            self.progress_s.emit(i / data_points * 100)
            print(f"iter: {i}")

            measured_values = [self._lockin.read_value() for _ in range(integrations)]
            measured_value = sum(measured_values) / len(measured_values)

            self.save_and_show_measurement(elem, measured_value, correction)
            self.adjust_sensitivity(measured_value)

            duration = self._motor.move_forward(steps_per_data_point)
            sleep(duration)
            self.current_motor_angle += angle_per_data_point

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

        self.measurement_ended()
        self.progress_s.emit(100)
        self.running = False

    @QtCore.Slot()
    def stop(self):
        """
        stop running measurement
        """
        self.running = False

    @QtCore.Slot(float)
    def move_to_pos(self, end_angle, from_gui=True):
        """
        move to specified position
        @param from_gui: ci bola metoda zavola z gui
        @param end_angle: position, where to move (angle)
        """
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

        self.potential_new_angle = end_angle

        self.motor_move_to_pos_s.emit(steps, forward)

    @QtCore.Slot(int, bool)
    def confirmed_move_to_pos(self, steps, forward):
        print('moving confirmed')
        if forward:
            self.move_forward(steps)
        else:
            self.move_reverse(steps)

        self.current_motor_angle = self.potential_new_angle


    @QtCore.Slot(int)
    def move_forward(self, steps):
        """
        move forward given steps
        @param steps: number of steps
        """
        if not self._motor.connected:
            self.logger.log(WARNING, "Motor nie je pripojeny")
            return
        print(f'moveF je uspesny, pocet krokov: {steps}')
        self._motor.move_forward(steps)

    @QtCore.Slot(int)
    def move_reverse(self, steps):
        """
        move reverse given steps
        @param steps: number of steps
        """
        if not self._motor.connected:
            self.logger.log(WARNING, "Motor nie je pripojeny")
            return
        print(f'moveR je uspesny, pocet krokov: {steps}')
        self._motor.move_reverse(steps)

    @QtCore.Slot(float)
    def initialization(self, pos):
        """
        initialize position of stepped motor
        @param pos: position, which to be used for initialization (angle)
        """
        self.current_motor_angle = pos

    def exit(self):
        """
        exit measurement
        """
        self._measurement_thread.quit()
        self._measurement_thread.wait()

    def measurement_ended(self):
        self.current_motor_angle = round(self.current_motor_angle, 2)
        self.measurement_ended_s.emit(self.current_motor_angle)

