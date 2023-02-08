from PySide6.QtCore import QObject, QThreadPool, QMetaObject, Qt, Q_ARG
from PySide6.QtWidgets import QMessageBox

from controllers.file_manager_controller import FileManagerController
from controllers.logger_controller import LoggerController
from controllers.measurement_controller.measurement_controller import MeasurementController

from models.disperse_element import Grating
from models.lockin.constants import *

from models.logger.constants import *


class MainController(QObject):
    def __init__(self, view, key):
        """
        initializes main controller object
        """
        super().__init__()
        self.view = view
        self.workers = QThreadPool().globalInstance()
        self._key = key
        self.file_manager = FileManagerController(key)
        self.logger = LoggerController(key)
        self.selected_disperse_element = Grating()

        self._measurement = MeasurementController()
        self._connect_measurement()

    def _connect_measurement(self):
        """
        connect the view with measurement controller features
        """
        widgets = self.view.widgets

        # disperse element combobox
        disp_elem_cbox = widgets.devices_controls_devices_selection_disperse_cbox
        disp_elem_cbox.activated.connect(self.update_disperse_element_choice)

        # lockin connection status
        self._measurement.voltmeter_status_s.connect(self.voltmeter_status)

        # measurement signals
        self._measurement.progress_s.connect(widgets.progressBar.setValue)
        self._measurement.lockin_settings_s.connect(self.set_values_from_lockin)
        self._measurement.measurement_start_fail_s.connect(self.view.switch_play_button)

        self._measurement.measurement_started_s.connect(self.clear_graph)
        self._measurement.measurement_started_s.connect(lambda: self.view.device_control_buttons_set_enabled(False))

        self._measurement.measured_value_s.connect(self.update_graph)
        self._measurement.measurement_ended_s.connect(self.set_measurement_start_and_reenable_device_buttons)

        # go to pos with confirmation
        self._measurement.motor_move_to_angle_s.connect(self.move_to_angle_confirmation)

        # moveForward/moveReverse
        steps_to_move = widgets.devices_controls_engine_positioning_step_sbox.value

        widgets.devices_controls_engine_positioning_right_btn.clicked.connect(
            lambda: self.move_reverse(steps_to_move()))
        widgets.devices_controls_engine_positioning_left_btn.clicked.connect(
            lambda: self.move_forward(steps_to_move()))

        # switch units
        motor_goto = widgets.devices_controls_goto_sbox
        measurement_start = widgets.measurement_config_menu_start_sbox
        measurement_end = widgets.measurement_config_menu_end_sbox

        variable_sboxes = [motor_goto, measurement_start, measurement_end]

        widgets.radioButton_2.pressed.connect(
            lambda: None if widgets.radioButton_2.isChecked() else self.angle_sboxes_convert(True, variable_sboxes))
        widgets.radioButton.pressed.connect(
            lambda: None if widgets.radioButton.isChecked() else self.angle_sboxes_convert(False, variable_sboxes))

        # moveToPosition
        widgets.devices_controls_goto_btn.clicked.connect(
            lambda: self.move_to_angle(self.get_angle(widgets.devices_controls_goto_sbox)))

        # init position
        widgets.devices_controls_calibration_btn.clicked.connect(
            lambda: self.initialization(self.get_angle(widgets.motor_init_pos_sbox)))

        # start measurement
        start_angle = lambda: self.get_angle(widgets.measurement_config_menu_start_sbox)
        end_angle = lambda: self.get_angle(widgets.measurement_config_menu_end_sbox)
        steps_per_datapoint = widgets.measurement_motor_step.value
        correction = widgets.measurement_correction_sbox.value
        integrations = widgets.measurement_integrations_sbox.value

        widgets.action_play.triggered.connect(self.view.switch_play_button)
        widgets.action_play.triggered.connect(
            lambda: self.start_measurement(
                start_angle(),
                end_angle(),
                steps_per_datapoint(),
                correction(),
                integrations()
            )
        )

        # stop action
        widgets.action_stop.triggered.connect(self.stop_measurement)

        # calibration window
        widgets.actionKalibr_cia.triggered.connect(self.view.show_calibration_dialog)
        widgets.calibration_dialog.calibration_data_s.connect(
            lambda data: self.create_calibration(data))
        widgets.calibration_dialog.step_button.clicked.connect(
            lambda: self.move_forward(widgets.calibration_dialog.step_size.value()))

        # calibration window
        widgets.action_choose_comport.triggered.connect(self.view.show_comport_choice_dialog)
        widgets.comport_choice_dialog.comports_confirmed_s.connect(self.new_comports_chosen)

        # auto sensitivity
        widgets.measurement_config_menu_span_auto_check.clicked.connect(self.auto_sensitivity_checkbox)
        widgets.measurement_config_menu_min_sensitivity_sbox.setValue(LOWEST_AUTO_SETTABLE_GAIN_DEFAULT)
        widgets.measurement_config_menu_min_sensitivity_sbox.valueChanged.connect(self.set_lockin_min_auto_sensitivity)

        # logger
        self._measurement.status_report_s.connect(lambda level, message: self.logger.log(level, message))

    def auto_sensitivity_checkbox(self):
        is_enabled = self.view.widgets.measurement_config_menu_span_auto_check.isChecked()
        self.view.widgets.measurement_config_menu_min_sensitivity_sbox.setEnabled(is_enabled)
        self.view.widgets.measurement_config_menu_span_dsbox.setEnabled(not is_enabled)

    def set_lockin_min_auto_sensitivity(self, value):
        QMetaObject.invokeMethod(
            self._measurement,
            "set_lockin_min_auto_sensitivity",
            Q_ARG(int, value)
        )

    def new_comports_chosen(self, lockin, motor):
        self.logger.log(INFO, f'Vybranté comporty lockin: {lockin}, motor: {motor}')
        QMetaObject.invokeMethod(
            self._measurement,
            "new_comports_chosen",
            Qt.QueuedConnection,
            Q_ARG(str, lockin),
            Q_ARG(str, motor)
        )

    def angstrom_unit_selected(self):
        return self.view.widgets.radioButton_2.isChecked()

    def get_angle(self, sbox):
        """
        get angle values from GUI sboxes
        @param sbox: sbox object with value
        """
        gui_value = sbox.value()
        selected_element = self.selected_disperse_element
        if not selected_element.is_valid():
            self.logger.log(WARNING, "Neplatný alebo nevybraný disperzný prvok.")
            return None
        if self.angstrom_unit_selected():
            return selected_element.wavelengthToAngle(gui_value)
        return gui_value

    def angle_sboxes_convert(self, to_angstroms, boxes):
        """
        convert angle values from GUI sboxes to Angstrom
        @param to_angstroms: if true convert to Angstrom else not
        @param boxes: list of boxes to change
        """
        selected_element = self.selected_disperse_element

        if not selected_element.is_valid():
            return
        if to_angstroms:
            for sbox in boxes:
                sbox.setSuffix(" Å")
                sbox.setRange(0, 20000)
                angle = selected_element.clamp_angle(sbox.value())
                sbox.setValue(selected_element.angleToWavelength(angle))

        else:
            for sbox in boxes:
                sbox.setSuffix(" °")
                angle = selected_element.wavelengthToAngle(sbox.value())
                sbox.setValue(selected_element.clamp_angle(angle))
                sbox.setRange(selected_element.minAngle, selected_element.maxAngle)

    def set_measurement_start_and_reenable_device_buttons(self, cur_angle):
        self.view.switch_play_button()
        if self.angstrom_unit_selected():
            self.angle_sboxes_convert(True, [self.view.widgets.measurement_config_menu_start_sbox])
        else:
            self.view.widgets.measurement_config_menu_start_sbox.setValue(cur_angle)

        self.view.device_control_buttons_set_enabled(True)

    def voltmeter_status(self, connected):
        """
        get and set voltmeter status
        @param connected: if true voltmeter connected else not
        """
        self.view.on_voltmeter_connection_change(connected)
        self.view.widgets.action_play.setEnabled(connected)

    def set_values_from_lockin(self, data):
        """
        set lickin parameters of measurement
        @param data: data to be set
        """
        widgets = self.view.widgets
        widgets.measurement_config_menu_angle_sbox.setValue(data[PHASE_SHIFT])
        widgets.measurement_config_menu_ref_sbox.setValue(data[REFERENCE_FREQUENCY])
        widgets.measurement_config_menu_time_const_dsbox.setValue(data[PRE_TIME_CONST])
        widgets.measurement_config_menu_time_const_dsbox_post.setValue(data[POST_TIME_CONST])
        widgets.measurement_config_menu_span_dsbox.setValue(data[GAIN])

        is_settable_gain = data[SETTABLE_GAIN]

        self.view.widgets.measurement_config_menu_min_sensitivity_sbox.setEnabled(is_settable_gain)
        self.view.widgets.measurement_config_menu_span_auto_check.setChecked(is_settable_gain)
        self.view.widgets.measurement_config_menu_span_auto_check.setEnabled(is_settable_gain)
        self.view.widgets.measurement_config_menu_span_dsbox.setEnabled(not is_settable_gain)

    def clear_graph(self):
        """
        remove all values from graph
        """
        self.view.widgets.graph_view.initialize()
        self.view.widgets.graph_view.plotGraph()

    def update_graph(self, angle, wavelength, value, cmp):
        """
        update graph with given values
        @param angle: current angle
        @param wavelength: given wavelength value
        @param value: given measured value
        @param cmp: if true current measurement else older measurement
        """
        self.view.widgets.motor_init_pos_sbox.setValue(angle)
        self.view.widgets.graph_view.addMeasurement([[wavelength, value]], cmp)
        self.view.widgets.graph_view.plotGraph()

    def _interconnect_file_manager_controller(self):
        """
        connect file manager with other controllers
        """
        self.file_manager.log_s.connect(lambda level, message, show_user: self.logger.log(level, message, show_user))

    def start_measurement(self, start, end, step_size, correction, integrations):
        """
        start actual measurement process
        @param start: start position of measurement (angle)
        @param end: end position of measurement (angle)
        @param step_size: number of unit steps for one measurement
        @param correction: correction parameter value
        @param integrations: integration parameter value
        """
        if start is None or end is None:
            start = 0
            end = -1

        QMetaObject.invokeMethod(
            self._measurement,
            "set_arguments",
            Q_ARG(float, correction),
            Q_ARG(int, integrations)
        )
        QMetaObject.invokeMethod(
            self._measurement,
            "start",
            Qt.QueuedConnection,
            Q_ARG(float, start),
            Q_ARG(float, end),
            Q_ARG(int, step_size)
        )

    def update_disperse_element_choice(self):
        """
        update disperse element according to element chosen in GUI
        """
        element_name = self.view.widgets.devices_controls_devices_selection_disperse_cbox.currentText()
        self.selected_disperse_element = Grating(element_name)
        min_angle, max_angle = self.selected_disperse_element.minAngle, self.selected_disperse_element.maxAngle
        self.view.widgets.motor_init_pos_sbox.setRange(min_angle, max_angle)
        QMetaObject.invokeMethod(self._measurement, 'set_disperse_element', Q_ARG(str, element_name))

    def create_calibration(self, data):
        """
        create calibration for disperse element
        @param data: calibration data
        """
        new_grating = Grating()
        new_grating.save_calibration(data)
        self.view.update_disperse_elements_list()

    def stop_measurement(self):
        """
        stop currently running measurement
        """
        self.view.switch_play_button()
        QMetaObject.invokeMethod(self._measurement, 'stop', Qt.DirectConnection)

    def move_to_angle_confirmation(self, steps, forward):
        """
        confirmation move_to_angle value
        @param steps: number of steps
        @param forward: if true motor go forward else reverse
        """
        dir_text = "dopredu" if forward else "dozadu"
        dialog_window = self.view.widgets.goto_confirmation_dialog
        dialog_window.setText(f"Motor sa posunie o {steps} krokov {dir_text}. Je to v poriadku ?")

        if dialog_window.exec() == QMessageBox.Yes:
            QMetaObject.invokeMethod(
                self._measurement,
                'confirmed_move_to_angle',
                Q_ARG(int, steps),
                Q_ARG(bool, forward))

    def move_to_angle(self, pos):
        """
        motor goes at given position
        @param pos: position to go (angle)
        """
        if pos is None:
            return
        QMetaObject.invokeMethod(self._measurement, 'move_to_angle', Qt.QueuedConnection, Q_ARG(float, pos))

    def initialization(self, pos):
        """
        initialization of stepped motor position
        @param pos: actual initialization position of stepped motor (angle)
        """
        if pos is None:
            return
        QMetaObject.invokeMethod(self._measurement, 'initialization', Qt.QueuedConnection, Q_ARG(float, pos))

    def move_forward(self, steps):
        """
        move stepped motor forward
        @param steps: number of steps to move
        """
        QMetaObject.invokeMethod(self._measurement, 'move_forward', Qt.QueuedConnection, Q_ARG(int, steps))

    def move_reverse(self, steps):
        """
        move stepped motor reverse
        @param steps: number of steps to move
        """
        QMetaObject.invokeMethod(self._measurement, 'move_reverse', Qt.QueuedConnection, Q_ARG(int, steps))

    def exit_measurement(self, key):
        """
        exit measurement
        @param key: key string
        """
        if key == self._key:
            self._measurement.exit()
