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
    status_report_s = Signal(int, str)
    voltmeter_status_s = Signal(bool)
    lockin_settings_s = Signal(dict)
    motor_move_to_angle_s = Signal(int, bool)
    measurement_start_fail_s = Signal()
    measurement_started_s = Signal()
    measured_value_s = Signal(float, float, float, bool)
    progress_s = Signal(float)
    measurement_ended_s = Signal(float)

    def __init__(self):
        """
        initializes measurement controller object
        """
        super().__init__()

        self.data_processing = None
        self._lockin = Lockin('SR510')
        self._motor = Motor()
        self._elem = None

        self.current_motor_angle = None
        self.correction = 0
        self.integrations = 1

        self.measurement_in_progress = False

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
        """
        Set minimal sensitivity that can be used for automatic sensitivity switching.
        @param value: int (index of the sensitivity based on list inside lockinds_data.json)
        @return: None
        """
        if self._lockin.can_auto_switch():
            self._lockin.set_min_auto_sensitivity(value)

    def comport_cable_info(self, comport):
        return f'{comport.vid}:{comport.pid}:{comport.serial_number}'

    @QtCore.Slot(str, str)
    def new_comports_chosen(self, lockin_comport_name, motor_comport_name):
        """
        Set information about connected cables at chosen comports.
        @param lockin_comport_name:
        @param motor_comport_name:
        @return: None
        """
        for comport in list_ports.comports():
            if comport.name == lockin_comport_name:
                self.lockin_cable_info = self.comport_cable_info(comport)
            elif comport.name == motor_comport_name:
                self.motor_cable_info = self.comport_cable_info(comport)

        self._lockin.disconnect()
        self._motor.disconnect()

    def check_periphery(self):
        """
        Check if motor and lockin are connected and connect them
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
                        self.status_report_s.emit(CRITICAL, f"Chyba pri pripajaní lockinu: {e}")
            elif self.comport_cable_info(comport) == self.motor_cable_info:

                found_motor_cable = True
                if self._motor.connected is False:
                    try:
                        self._motor.connect(comport.name)
                    except Exception as e:
                        self.status_report_s.emit(CRITICAL, f"Chyba pri pripajaní krokového motora: {e}")

        if not found_motor_cable:
            if self._motor.connected:
                self.status_report_s.emit(WARNING, "Motor bol odpojený")
            self._motor.disconnect()

        if not found_lockin_cable:
            self._lockin.disconnect()
            self.voltmeter_status_s.emit(False)

    def lockin_read_setting_safely(self, setting):
        """
        Read a setting from lockin and log any error
        @param setting: str
        @return: requested setting
        """
        try:
            return self._lockin.read_setting(setting)
        except Exception as e:
            self.status_report_s.emit(CRITICAL, e)

    def get_important_lockin_values(self):
        """
        get/load lockin parameters
        """
        data = {setting: self.lockin_read_setting_safely(setting) for setting in SETTINGS_IN_GUI}
        data[SETTABLE_GAIN] = self._lockin.can_auto_switch()
        self.lockin_settings_s.emit(data)

    def link_data_processing_controller(self, dpc):
        """
        connect data processing controller object
        @param dpc: data processing controller
        """
        self.data_processing = dpc

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
        cur_gain = self._lockin.current_gain_value()
        self.status_report_s.emit(INFO, f'Namerana hodnota: {measured_value} so senzitivitou {cur_gain}')

        if measured_value >= 0.7 * cur_gain:
            if self._lockin.lower_gain():
                settle_delay = 5 * self._lockin.read_setting(PRE_TIME_CONST)
                gain_val = self._lockin.current_gain_value()
                self.status_report_s.emit(INFO, f'SENZITIVITA sa znížila na {gain_val} čaká sa {settle_delay}s')
                sleep(settle_delay)
        elif measured_value <= 0.2 * cur_gain:
            if self._lockin.higher_gain():
                settle_delay = 5 * self._lockin.read_setting(PRE_TIME_CONST)
                gain_val = self._lockin.current_gain_value()
                self.status_report_s.emit(INFO, f'SENZITIVITA sa zvýšila na {gain_val} čaká sa {settle_delay}s')
                sleep(settle_delay)

    def save_and_show_measurement(self, elem, value, correction):
        """
        send measurement to data processing controller
        @param elem: used grating
        @param value: measured value at concrete angle
        @param correction: used correction of measurement
        @raise data_processing_error: raises an exception when trying to send measurement
        """
        angle = self.current_motor_angle
        wavelength = elem.angleToWavelength(angle) + correction

        try:
            self.data_processing.add_measurement(angle, wavelength, value)
        except DataProcessingError as e:
            self.status_report_s.emit(WARNING, e.message)
            return

        self.measured_value_s.emit(angle, wavelength, value, True)

    def failed_measurement(self, msg):
        """
        failed measurement
        @param msg: message to show when failed measurement
        """
        self.status_report_s.emit(WARNING, msg)
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
    def start(self, start, end, steps_per_measurement):
        """
        start overall measurement
        @param start: start position of measurement (angle)
        @param end: end position of measurement (angle)
        @param steps_per_measurement: number of step per one measured value
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
            # self.move_to_angle(start, False)

        self._lockin.prepare()
        self.get_important_lockin_values()

        try:
            self.data_processing.create_new_file()
        except DataProcessingError as e:
            self.failed_measurement(e.message)
            return

        self.measurement_started_s.emit()
        self.measurement_in_progress = True
        self.progress_s.emit(0)

        disperse_element = self._elem
        correction = self.correction
        integrations = self.integrations

        total_motor_steps = disperse_element.angleToSteps(distance)

        last_movement_remaining_steps = total_motor_steps % steps_per_measurement
        last_irregular_movement_needed = last_movement_remaining_steps > 0

        regular_motor_movements = total_motor_steps // steps_per_measurement
        number_of_measurements = 1 + regular_motor_movements + (1 if last_irregular_movement_needed else 0)

        def measure():
            nonlocal measurement_no
            measured_values = [self._lockin.read_value() for _ in range(integrations)]
            measured_value = sum(measured_values) / len(measured_values)

            self.save_and_show_measurement(disperse_element, measured_value, correction)
            self.adjust_sensitivity(measured_value)

            self.progress_s.emit(measurement_no / number_of_measurements * 100)
            self.status_report_s.emit(INFO, f"{measurement_no}. uhol: {self.current_motor_angle:.3f} nameraná hodnota: {measured_value}")
            measurement_no += 1

        def move_motor_forward(steps):
            motor_movement_duration = self._motor.move_forward(steps)
            sleep(motor_movement_duration)

        self.status_report_s.emit(INFO, f"dĺžka merania: {distance}°, počet krokov: {total_motor_steps}, počet meraní: {number_of_measurements}")
        measurement_no = 1
        measure()

        angle_change_per_move = disperse_element.stepsToAngle(steps_per_measurement)

        for i in range(regular_motor_movements):
            if self.measurement_in_progress is False:
                self.measurement_ended()
                return
            move_motor_forward(steps_per_measurement)
            self.current_motor_angle += angle_change_per_move
            measure()

        if last_irregular_movement_needed:
            if self.measurement_in_progress is False:
                self.measurement_ended()
                return
            move_motor_forward(last_movement_remaining_steps)
            self.current_motor_angle = end
            measure()

        self.current_motor_angle = end
        self.measurement_ended()
        self.progress_s.emit(100)
        self.measurement_in_progress = False

    def measurement_ended(self):
        self.current_motor_angle = round(self.current_motor_angle, 2)
        self.measurement_ended_s.emit(self.current_motor_angle)

    @QtCore.Slot()
    def stop(self):
        """
        stop running measurement
        """
        self.measurement_in_progress = False

    @QtCore.Slot(float)
    def move_to_angle(self, end_angle, from_gui=True):
        """
        move to specified angle
        @param from_gui: bool called from gui?
        @param end_angle: position, where to move (angle)
        """
        if self.current_motor_angle is None:
            self.status_report_s.emit(WARNING, "Poloha motora nie je inicializovaná.")
            return

        if not self._elem.is_angle_within_min_max(end_angle):
            if not from_gui:
                self.failed_measurement("Pokúšaš sa posunúť mimo rozsah mriežky")
            else:
                self.status_report_s.emit(WARNING, "Pokúšaš sa posunúť mimo rozsah mriežky")
            return

        if from_gui and self.measurement_in_progress:
            self.status_report_s.emit(WARNING, "Nemôžeš hýbať motorom počas merania.")
            return

        if self.current_motor_angle == end_angle:
            return

        distance = end_angle - self.current_motor_angle
        steps = self._elem.angleToSteps(abs(distance))
        forward = distance > 0

        self.potential_new_angle = end_angle

        self.motor_move_to_angle_s.emit(steps, forward)

    @QtCore.Slot(int, bool)
    def confirmed_move_to_angle(self, steps, forward):
        """
        Called after user confirmed motor movement steps and direction
        @param steps: int
        @param forward: bool
        @return: None
        """
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
            self.status_report_s.emit(WARNING, "Motor nie je pripojeny")
            return
        self.status_report_s.emit(INFO, f'Motor sa pohybuje dopredu o {steps} krokov')
        self._motor.move_forward(steps)

    @QtCore.Slot(int)
    def move_reverse(self, steps):
        """
        move reverse given steps
        @param steps: number of steps
        """
        if not self._motor.connected:
            self.status_report_s.emit(WARNING, "Motor nie je pripojeny")
            return
        self.status_report_s.emit(INFO, f'Motor sa pohybuje dozadu o {steps} krokov')
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
