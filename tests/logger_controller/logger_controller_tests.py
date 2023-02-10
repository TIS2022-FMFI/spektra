import unittest

from controllers.logger_controller import LoggerController


class LoggerControllerTests(unittest.TestCase):
    def test_logger_is_empty(self):
        # Arrange
        controller = LoggerController("test")
        self.assertEqual(controller.is_logger_empty(), True)
        controller.log(10, "test", False)
        self.assertEqual(controller.is_logger_empty(), False)



