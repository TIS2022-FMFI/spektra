import unittest
from datetime import datetime
from time import sleep

from models.logger.log import Log
from models.logger.log_level import LogLevel
from models.logger.constants import DEBUG, INFO, SUCCESS, WARNING, ERROR, CRITICAL


class LogTests(unittest.TestCase):

    def test_log_init(self):
        # Arrange
        log_level = LogLevel(DEBUG)
        log = Log("test", log_level)
        # Act
        # Assert
        self.assertEqual(log.message, "test")
        self.assertEqual(log.level, log_level)
        self.assertEqual(log.next, None)
        self.assertEqual(log.previous, None)

    def test_log_str_format(self):
        # Arrange
        log_level = LogLevel(DEBUG)
        log = Log("test", log_level)
        # Act
        # Assert
        self.assertEqual(str(log), f'{log.timestamp.strftime(("%d. %m. %Y %H:%M:%S"))} - {log.level}: {log.message}')

    def test_log_repr_format(self):
        # Arrange
        log_level = LogLevel(DEBUG)
        log = Log("test", log_level)
        # Act
        # Assert
        self.assertEqual(repr(log), str(log))

    def test_log_eq(self):
        # Arrange
        log_level = LogLevel(DEBUG)
        log = Log("test", log_level)
        log2 = Log("test", log_level)
        # Act
        # Assert
        self.assertEqual(log, log2)

    def test_log_lt(self):
        # Arrange
        log_level = LogLevel(DEBUG)
        log = Log("test", log_level)
        sleep(0.01)
        log2 = Log("test", log_level)
        # Act
        # Assert
        self.assertTrue(log < log2)

    def test_log_gt(self):
        # Arrange
        log_level = LogLevel(DEBUG)
        log = Log("test", log_level)
        sleep(0.01)
        log2 = Log("test", log_level)
        # Act
        # Assert
        self.assertTrue(log2 > log)

    def test_log_le(self):
        # Arrange
        log_level = LogLevel(DEBUG)
        log = Log("test", log_level)
        sleep(0.01)
        log2 = Log("test", log_level)
        # Act
        # Assert
        self.assertTrue(log <= log2)
        self.assertTrue(log <= log)

    def test_log_ge(self):
        # Arrange
        log_level = LogLevel(DEBUG)
        log = Log("test", log_level)
        sleep(0.01)
        log2 = Log("test", log_level)
        # Act
        # Assert
        self.assertTrue(log2 >= log)
        self.assertTrue(log2 >= log2)

    def test_log_ne(self):
        # Arrange
        log_level = LogLevel(DEBUG)
        log = Log("test", log_level)
        log2 = Log("test2", log_level)
        # Act
        # Assert
        self.assertTrue(log != log2)
        self.assertFalse(log != log)

    def test_log_level(self):
        # Arrange
        log_level = LogLevel(DEBUG)
        log = Log("test", log_level)
        # Act
        # Assert
        self.assertEqual(log.level, log_level)

    def test_log_message(self):
        # Arrange
        log_level = LogLevel(DEBUG)
        log = Log("test", log_level)
        # Act
        # Assert
        self.assertEqual(log.message, "test")

    def test_log_timestamp(self):
        # Arrange
        log_level = LogLevel(DEBUG)
        log = Log("test", log_level)
        # Act
        # Assert
        self.assertTrue(log.timestamp is not None)
        self.assertTrue(isinstance(log.timestamp, datetime))

    def test_log_next(self):
        # Arrange
        log_level = LogLevel(DEBUG)
        log = Log("test", log_level)
        # Act
        # Assert
        self.assertEqual(log.next, None)

    def test_log_previous(self):
        # Arrange
        log_level = LogLevel(DEBUG)
        log = Log("test", log_level)
        # Act
        # Assert
        self.assertEqual(log.previous, None)

    def test_log_set_next(self):
        # Arrange
        log_level = LogLevel(DEBUG)
        log = Log("test", log_level)
        log2 = Log("test2", log_level)
        # Act
        log.next = log2
        # Assert
        self.assertEqual(log.next, log2)

    def test_log_set_previous(self):
        # Arrange
        log_level = LogLevel(DEBUG)
        log = Log("test", log_level)
        log2 = Log("test2", log_level)
        # Act
        log.previous = log2
        # Assert
        self.assertEqual(log.previous, log2)

    def test_log_set_level(self):
        # Arrange
        log_level = LogLevel(DEBUG)
        log = Log("test", log_level)
        log_level2 = LogLevel(INFO)
        # Act
        log.level = log_level2
        # Assert
        self.assertEqual(log.level, log_level2)


if __name__ == '__main__':
    unittest.main()
