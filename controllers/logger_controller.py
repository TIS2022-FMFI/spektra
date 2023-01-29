from PySide6.QtCore import QObject, Signal

from models.logger.log import Log
from models.logger.logger import Logger


class LoggerController(QObject):
    display_log_s = Signal(Log)

    def __init__(self, key):
        super(LoggerController, self).__init__()
        self._key = key
        self._logger = Logger()

    def log(self, level, message, show_user=True):
        """
        Log a message to the logger.
        :param level: The level of the log.
        :param message: The message to log.
        :param show_user: Whether to show the log to the user.
        """
        log = self._logger.log(message, level)
        if show_user:
            self.display_log_s.emit(log)

    def get_model(self, key):
        if key == self._key:
            return self._logger
        else:
            raise ValueError("Invalid key")

    def save_logs_to_file(self):
        """Save the logs to a file."""
        self._logger.save()
