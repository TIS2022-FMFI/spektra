from PySide6.QtCore import QObject, Signal

from models.logger.log import Log
from models.logger.logger import Logger


class LoggerController(QObject):
    display_log_s = Signal(Log)

    def __init__(self, key):
        super(LoggerController, self).__init__()
        self._key = key
        self._logger = Logger()

    def debug(self, message, show_user=True):
        log = self._logger.debug(message)
        if show_user:
            self.display_log_s.emit(log)

    def info(self, message, show_user=True):
        log = self._logger.info(message)
        if show_user:
            self.display_log_s.emit(log)

    def warning(self, message, show_user=True):
        log = self._logger.warning(message)
        if show_user:
            self.display_log_s.emit(log)

    def error(self, message, show_user=True):
        log = self._logger.error(message)
        if show_user:
            self.display_log_s.emit(log)

    def critical(self, message, show_user=True):
        log = self._logger.critical(message)
        if show_user:
            self.display_log_s.emit(log)

    def get_model(self, key):
        if key == self._key:
            return self._logger
        else:
            raise ValueError("Invalid key")

    def save_logs_to_file(self):
        self._logger.save()
