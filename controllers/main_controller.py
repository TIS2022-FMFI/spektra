from PySide6.QtCore import QObject

from controllers.file_manager_controller import FileManagerController
from controllers.logger_controller import LoggerController


class MainController(QObject):
    def __init__(self, key):
        super(MainController, self).__init__()
        self._key = key
        self.file_manager = FileManagerController(key)
        self.logger = LoggerController(key)
        self._interconnect_file_manager_controller()

    def _interconnect_file_manager_controller(self):
        # connects the file manager controller to other controllers
        self.file_manager.log_s.connect(lambda lvl, msg, show_user: self.logger.log(lvl, msg, show_user))
