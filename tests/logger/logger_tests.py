import os
import unittest
from models.logger.logger import Logger
from models.logger.log_level import LogLevel
from models.logger.constants import DEBUG, INFO, SUCCESS, WARNING, ERROR, CRITICAL, MIN_LOG_LEVEL, MAX_BUFFER_SIZE


class LoggerTests(unittest.TestCase):

    def test_logger_critical(self):
        # Arrange
        logger = Logger()
        # Act
        log = logger.critical("test")
        # Assert
        self.assertEqual(log.message, "test")
        self.assertEqual(log.level, LogLevel(CRITICAL))
        self.assertEqual(log.next, None)
        self.assertEqual(log.previous, None)

    def test_logger_error(self):
        # Arrange
        logger = Logger()
        # Act
        log = logger.error("test")
        # Assert
        self.assertEqual(log.message, "test")
        self.assertEqual(log.level, LogLevel(ERROR))
        self.assertEqual(log.next, None)
        self.assertEqual(log.previous, None)

    def test_logger_warning(self):
        # Arrange
        logger = Logger()
        # Act
        log = logger.warning("test")
        # Assert
        self.assertEqual(log.message, "test")
        self.assertEqual(log.level, LogLevel(WARNING))
        self.assertEqual(log.next, None)
        self.assertEqual(log.previous, None)

    def test_logger_success(self):
        # Arrange
        logger = Logger()
        # Act
        log = logger.success("test")
        # Assert
        self.assertEqual(log.message, "test")
        self.assertEqual(log.level, LogLevel(SUCCESS))
        self.assertEqual(log.next, None)
        self.assertEqual(log.previous, None)

    def test_logger_info(self):
        # Arrange
        logger = Logger()
        # Act
        log = logger.info("test")
        # Assert
        self.assertEqual(log.message, "test")
        self.assertEqual(log.level, LogLevel(INFO))
        self.assertEqual(log.next, None)
        self.assertEqual(log.previous, None)

    def test_logger_debug(self):
        # Arrange
        logger = Logger()
        # Act
        log = logger.debug("test")
        # Assert
        self.assertEqual(log.message, "test")
        self.assertEqual(log.level, LogLevel(DEBUG))
        self.assertEqual(log.next, None)
        self.assertEqual(log.previous, None)

    def test_logger_log(self):
        # Arrange
        logger = Logger()
        # Act
        log = logger.log("test", DEBUG)
        # Assert
        self.assertEqual(log.message, "test")
        self.assertEqual(log.level, LogLevel(DEBUG))
        self.assertEqual(log.next, None)
        self.assertEqual(log.previous, None)

    def test_log_file_path(self):
        # Arrange
        logger = Logger("test")
        # Act
        # Assert
        self.assertNotEqual(logger.get_log_filepath(), "test")

    def test_minimum_log_level(self):
        # Arrange
        below_minimum = MIN_LOG_LEVEL + 10
        logger = Logger()
        # Act
        logger.log("test", below_minimum)
        # Assert
        self.assertEqual(logger.size(), 0)

    def test_save_logs_to_file_creation(self):
        # Arrange
        logger = Logger()
        logger.debug("test")
        # Act
        filepath = logger.get_log_filepath()
        logger.save()
        self.assertTrue(os.path.exists(filepath))

    def test_save_logs_to_file_content(self):
        # Arrange
        logger = Logger()
        # Act
        log = logger.success("test")
        filepath = logger.get_log_filepath()
        logger.save()
        with open(filepath, "r") as file:
            content = file.read()
        # Assert
        self.assertEqual(content, str(log) + "\n")

    def test_more_than_max_logs(self):
        logger = Logger()
        for i in range(0, 2 * MAX_BUFFER_SIZE + 1):
            logger.critical("test")
        self.assertEqual(logger.size(), 1)

if __name__ == '__main__':
    unittest.main()
