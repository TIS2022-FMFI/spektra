import os

from models.logger.log import Log
from models.logger.log_buffer import LogBuffer
from models.logger.log_level import LogLevel
from models.logger.constants import DEBUG, INFO, SUCCESS, WARNING, ERROR, CRITICAL, MIN_LOG_LEVEL, LOG_FILE_EXTENSION
from settings import Settings
from utils.file_utils import remove_files_older_than, generate_log_file_name


class Logger:
    def __init__(self, log_file: str = None):
        self._log_file = log_file
        self._set_log_file()
        self._buffer = LogBuffer()
        remove_files_older_than(os.path.dirname(self._log_file), LOG_FILE_EXTENSION, Settings.LOGS_MAX_AGE)

    def critical(self, message):
        return self.log(message, CRITICAL)

    def error(self, message):
        return self.log(message, ERROR)

    def warning(self, message):
        return self.log(message, WARNING)

    def success(self, message):
        return self.log(message, SUCCESS)

    def info(self, message):
        return self.log(message, INFO)

    def debug(self, message):
        return self.log(message, DEBUG)

    def log(self, message, level):
        log = Log(message, LogLevel(level))
        if Settings.DEBUG and level == DEBUG:
            print(log)
        if log.level >= MIN_LOG_LEVEL:
            try:
                self._buffer.add(log)
            except BufferError:
                self._flush()
                self._buffer.add(log)
        ret = log.copy
        ret.next = ret.previous = None
        return ret

    def _flush(self):
        self._buffer.dump_to_file(self._log_file)
        self._log_file = os.path.join(os.path.dirname(self._log_file), generate_log_file_name())

    def _set_log_file(self):
        if self._log_file is None or not os.path.exists(self._log_file):
            self._log_file = os.path.join(os.getcwd(), Settings.LOGS_FOLDER, generate_log_file_name())
            if not os.path.exists(os.path.dirname(self._log_file)):
                os.makedirs(os.path.dirname(self._log_file))

    def save(self):
        self._flush()

    def size(self):
        return len(self._buffer)

    def get_log_filepath(self):
        return self._log_file
