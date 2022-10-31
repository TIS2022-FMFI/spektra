import unittest

from models.logger.log_level import LogLevel
from models.logger import constants as logger_constants


class LogLevelTests(unittest.TestCase):

    def test_debug_color(self):
        # Arrange
        log_level = logger_constants.DEBUG
        log = LogLevel(log_level)
        # Act
        color = log.color()
        # Assert
        self.assertEqual((color.red(), color.green(), color.blue()), logger_constants.COLORS[log_level])

    def test_debug_name(self):
        # Arrange
        log_level = logger_constants.DEBUG
        log = LogLevel(log_level)
        # Act
        # Assert
        self.assertEqual(str(log), logger_constants.STR[log_level])

    def test_debug_level(self):
        # Arrange
        log_level = logger_constants.DEBUG
        log = LogLevel(log_level)
        # Act
        # Assert
        self.assertEqual(log.level, log_level)

    def test_info_color(self):
        # Arrange
        log_level = logger_constants.INFO
        log = LogLevel(log_level)
        # Act
        color = log.color()
        # Assert
        self.assertEqual((color.red(), color.green(), color.blue()), logger_constants.COLORS[log_level])

    def test_info_name(self):
        # Arrange
        log_level = logger_constants.INFO
        log = LogLevel(log_level)
        # Act
        # Assert
        self.assertEqual(str(log), logger_constants.STR[log_level])

    def test_info_level(self):
        # Arrange
        log_level = logger_constants.INFO
        log = LogLevel(log_level)
        # Act
        # Assert
        self.assertEqual(log.level, log_level)

    def test_success_color(self):
        # Arrange
        log_level = logger_constants.SUCCESS
        log = LogLevel(log_level)
        # Act
        color = log.color()
        # Assert
        self.assertEqual((color.red(), color.green(), color.blue()), logger_constants.COLORS[log_level])

    def test_success_name(self):
        # Arrange
        log_level = logger_constants.SUCCESS
        log = LogLevel(log_level)
        # Act
        # Assert
        self.assertEqual(str(log), logger_constants.STR[log_level])

    def test_success_level(self):
        # Arrange
        log_level = logger_constants.SUCCESS
        log = LogLevel(log_level)
        # Act
        # Assert
        self.assertEqual(log.level, log_level)

    def test_warning_color(self):
        # Arrange
        log_level = logger_constants.WARNING
        log = LogLevel(log_level)
        # Act
        color = log.color()
        # Assert
        self.assertEqual((color.red(), color.green(), color.blue()), logger_constants.COLORS[log_level])

    def test_warning_name(self):
        # Arrange
        log_level = logger_constants.WARNING
        log = LogLevel(log_level)
        # Act
        # Assert
        self.assertEqual(str(log), logger_constants.STR[log_level])

    def test_warning_level(self):
        # Arrange
        log_level = logger_constants.WARNING
        log = LogLevel(log_level)
        # Act
        # Assert
        self.assertEqual(log.level, log_level)

    def test_error_color(self):
        # Arrange
        log_level = logger_constants.ERROR
        log = LogLevel(log_level)
        # Act
        color = log.color()
        # Assert
        self.assertEqual((color.red(), color.green(), color.blue()), logger_constants.COLORS[log_level])

    def test_error_name(self):
        # Arrange
        log_level = logger_constants.ERROR
        log = LogLevel(log_level)
        # Act
        # Assert
        self.assertEqual(str(log), logger_constants.STR[log_level])

    def test_error_level(self):
        # Arrange
        log_level = logger_constants.ERROR
        log = LogLevel(log_level)
        # Act
        # Assert
        self.assertEqual(log.level, log_level)

    def test_critical_color(self):
        # Arrange
        log_level = logger_constants.CRITICAL
        log = LogLevel(log_level)
        # Act
        color = log.color()
        # Assert
        self.assertEqual((color.red(), color.green(), color.blue()), logger_constants.COLORS[log_level])

    def test_critical_name(self):
        # Arrange
        log_level = logger_constants.CRITICAL
        log = LogLevel(log_level)
        # Act
        # Assert
        self.assertEqual(str(log), logger_constants.STR[log_level])

    def test_critical_level(self):
        # Arrange
        log_level = logger_constants.CRITICAL
        log = LogLevel(log_level)
        # Act
        # Assert
        self.assertEqual(log.level, log_level)

    def test_invalid_log_level(self):
        # Arrange
        log_level = 100
        # Act
        # Assert
        with self.assertRaises(ValueError):
            LogLevel(log_level)


if __name__ == '__main__':
    unittest.main()