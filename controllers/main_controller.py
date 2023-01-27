from PySide6.QtCore import QObject, QThreadPool, QMetaObject, Qt, Q_ARG
from controllers.file_manager_controller import FileManagerController
from controllers.logger_controller import LoggerController
from controllers.measurement_controller.measurement_controller import MeasurementController

from models.disperse_element import Grating


class MainController(QObject):
    def __init__(self, view, key):
        super(MainController, self).__init__()
        self.view = view
        self.workers = QThreadPool().globalInstance()
        self._key = key
        self.file_manager = FileManagerController(key)
        self.logger = LoggerController(key)

        self._measurement = MeasurementController()
        self._connect_measurement()

    def _connect_measurement(self):
        #self.view.widgets.action_play.setEnabled(False)
        self._measurement.progress_s.connect(lambda p: self.view.widgets.progressBar.setValue(p))
        self._measurement.progress_s.connect(lambda p: self.view.switch_play_button() if p == 100 else None)

        self.dispElemCBox = self.view.widgets.devices_controls_devices_selection_disperse_cbox
        self.dispElemCBox.activated.connect(self.update_disperse_element_choice)

        self._measurement.voltmeter_status_s.connect(self.voltmeter_status)

        self._measurement.measured_value_s.connect(self.updateGraph)
        self._measurement.new_measurement_started_s.connect(self.clearGraph)

        self.view.widgets.action_stop.triggered.connect(self.stop_measurement)

        self._measurement.lockin_settings_s.connect(self.set_values_from_lockin)

        self._measurement.measurement_start_fail_s.connect(self.set_play_button)

    def voltmeter_status(self, connected):
        self.view.on_voltmeter_connection_change(connected)
        self.view.widgets.action_play.setEnabled(connected)
    def set_play_button(self):
        self.view.switch_play_button()

    def set_values_from_lockin(self, data):
        widgets = self.view.widgets
        widgets.measurement_config_menu_angle_sbox.setValue(data['phase_shift'])
        widgets.measurement_config_menu_ref_sbox.setValue(data['ref_frequency'])
        widgets.measurement_config_menu_time_const_dsbox.setValue(data['pre_time_const'])
        widgets.measurement_config_menu_span_dsbox.setValue(666)

    def clearGraph(self):
        self.view.widgets.graph_view.initialize()
        self.view.widgets.graph_view.plotGraph()

    def updateGraph(self, wavelength, value, cmp):
        self.view.widgets.graph_view.addMeasurement([[wavelength, value]], cmp)
        self.view.widgets.graph_view.plotGraph()

    def _interconnect_file_manager_controller(self):
        # connects the file manager controller to other controllers
        self.file_manager.log_s.connect(lambda level, message, show_user: self.logger.log(level, message, show_user))

    def start_measurement(self, start, stop, stepSize, correction, integrations):
        QMetaObject.invokeMethod(self._measurement, "set_arguments", Q_ARG(float, correction), Q_ARG(int, integrations))

        QMetaObject.invokeMethod(
            self._measurement,
            "start",
            Qt.QueuedConnection,
            Q_ARG(float, start),
            Q_ARG(float, stop),
            Q_ARG(int, stepSize)
        )

    def update_disperse_element_choice(self):
        dispname = self.view.widgets.devices_controls_devices_selection_disperse_cbox.currentText()
        QMetaObject.invokeMethod(self._measurement, 'set_disperse_element', Qt.QueuedConnection, Q_ARG(str, dispname))

    def create_calibration(self, data):
        new_grating = Grating()
        new_grating.save_calibration(data)
        self.view.update_disperse_elements_list()

    def stop_measurement(self):
        QMetaObject.invokeMethod(self._measurement, 'stop', Qt.DirectConnection)

    def go_to_pos(self, pos):
        QMetaObject.invokeMethod(self._measurement, 'moveToPos', Qt.QueuedConnection, Q_ARG(float, pos))

    def initialization(self, pos):
        QMetaObject.invokeMethod(self._measurement, 'initialization', Qt.QueuedConnection, Q_ARG(float, pos))

    def move_forward(self, steps):
        QMetaObject.invokeMethod(self._measurement, 'moveForward', Qt.QueuedConnection, Q_ARG(int, steps))

    def move_reverse(self, steps):
        QMetaObject.invokeMethod(self._measurement, 'moveReverse', Qt.QueuedConnection, Q_ARG(int, steps))

    def exit_measurement(self, key):
        if key == self._key:
            self._measurement.exit()

    def update_measurement_settings(self, key, value):
        self._measurement.data_processing_controller.data_processing.set_legend_field(key, value)
