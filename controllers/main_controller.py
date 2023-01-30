from PySide6.QtCore import QObject, QThreadPool, QMetaObject, Qt, Q_ARG
from PySide6.QtWidgets import QMessageBox

from controllers.file_manager_controller import FileManagerController
from controllers.logger_controller import LoggerController
from controllers.measurement_controller.measurement_controller import MeasurementController

from models.disperse_element import Grating
from models.lockin.constants import *


class MainController(QObject):
    def __init__(self, view, key):
        """
        initializes main controller object
        """
        super(MainController, self).__init__()
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
        connect the view with file measurement controller features
        """
        # self.view.widgets.action_play.setEnabled(False)
        self._measurement.progress_s.connect(lambda p: self.view.widgets.progressBar.setValue(p))
        self._measurement.progress_s.connect(lambda p: self.view.switch_play_button() if p == 100 else None)

        disp_elem_cbox = self.view.widgets.devices_controls_devices_selection_disperse_cbox
        disp_elem_cbox.activated.connect(self.update_disperse_element_choice)

        self._measurement.voltmeter_status_s.connect(self.voltmeter_status)

        self._measurement.measured_value_s.connect(self.update_graph)
        self._measurement.new_measurement_started_s.connect(self.clear_graph)

        self.view.widgets.action_stop.triggered.connect(self.stop_measurement)

        self._measurement.lockin_settings_s.connect(self.set_values_from_lockin)

        self._measurement.measurement_start_fail_s.connect(self.set_play_button)

        self._measurement.motor_move_to_pos_s.connect(self.go_to_pos_confirmation)


    def voltmeter_status(self, connected):
        """
        get and set voltmeter status
        @param connected: if true voltmeter connected else not
        """
        self.view.on_voltmeter_connection_change(connected)
        self.view.widgets.action_play.setEnabled(connected)

    def set_play_button(self):
        """
        switch between stop and play button
        """
        self.view.switch_play_button()

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
        widgets.measurement_config_menu_span_dsbox.setValue(666)

    def clear_graph(self):
        """
        remove all values from graph
        """
        self.view.widgets.graph_view.initialize()
        self.view.widgets.graph_view.plotGraph()

    def update_graph(self, wavelength, value, cmp):
        """
        update graph with given values
        @param wavelength: given wavelength value
        @param value: given measured value
        @param cmp: if true current measurement else older measurement
        """
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
        @param stepSize: number of unit steps for one measurement
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
        QMetaObject.invokeMethod(self._measurement, 'stop', Qt.DirectConnection)

    def go_to_pos_confirmation(self, steps, forward):
        """
        confirmation go_to_pos value
        @param steps: number of steps
        @param forward: if true motor go forward else reverse
        """
        dir_text = "dopredu" if forward else "dozadu"
        dialog_window = self.view.widgets.goto_confirmation_dialog
        dialog_window.setText(f"Motor sa posunie o {steps} krokov {dir_text}. Je to v poriadku ?")

        if dialog_window.exec() == QMessageBox.Yes:
            QMetaObject.invokeMethod(
                self._measurement,
                'confirmed_move_to_pos',
                Q_ARG(int, steps),
                Q_ARG(bool, forward))

    def go_to_pos(self, pos):
        """
        motor goes at given position
        @param pos: position to go (angle)
        """
        if pos is None:
            return
        QMetaObject.invokeMethod(self._measurement, 'move_to_pos', Qt.QueuedConnection, Q_ARG(float, pos))

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
