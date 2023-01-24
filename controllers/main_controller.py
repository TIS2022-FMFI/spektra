from time import sleep

from PySide6.QtCore import QObject, QRunnable, QThreadPool, QEventLoop, QMetaObject, QThread, Qt
from controllers.file_manager_controller import FileManagerController
from controllers.logger_controller import LoggerController
from controllers.measurement_controller.measurement_controller import MeasurementController

class MainController(QObject):
    def __init__(self, key):
        super(MainController, self).__init__()
        self.workers = QThreadPool().globalInstance()
        self._key = key
        self.file_manager = FileManagerController(key)
        self.logger = LoggerController(key)
        self._measurement = MeasurementController()


    def _interconnect_file_manager_controller(self):
        # connects the file manager controller to other controllers
        self.file_manager.log_s.connect(lambda level, message, show_user: self.logger.log(level, message, show_user))

    def start_measurement(self):
        QMetaObject.invokeMethod(self._measurement, "start", Qt.QueuedConnection)

    def stop_measurement(self):
        QMetaObject.invokeMethod(self._measurement, "stop", Qt.QueuedConnection)

    def exit_measurement(self, key):
        if key == self._key:
            self._measurement.exit()
    def update_measurement_settings(self, key, value):
        self.data_processing.set_legend_field(key, value)