import unittest
from time import sleep

from models.logger.log_buffer import LogBuffer
from models.logger.log import Log
from models.logger.constants import DEBUG, INFO, SUCCESS, WARNING, ERROR, CRITICAL


class LogBufferTests(unittest.TestCase):

    def test_add_first(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        # Act
        log_buffer.add(log)
        # Assert
        self.assertEqual(log_buffer.head, log)
        self.assertEqual(log_buffer.tail, log)
        self.assertEqual(log_buffer.head.next, None)
        self.assertEqual(log_buffer.head.previous, None)

    def test_add_second(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        log2 = Log("test2", INFO)
        # Act
        log_buffer.add(log)
        log_buffer.add(log2)
        # Assert
        self.assertEqual(log_buffer.head, log)
        self.assertEqual(log_buffer.tail, log2)
        self.assertEqual(log_buffer.head.next, log2)
        self.assertEqual(log_buffer.head.previous, None)
        self.assertEqual(log_buffer.tail.next, None)
        self.assertEqual(log_buffer.tail.previous, log)

    def test_add_third(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        log2 = Log("test2", INFO)
        log3 = Log("test3", SUCCESS)
        # Act
        log_buffer.add(log)
        log_buffer.add(log2)
        log_buffer.add(log3)
        # Assert
        self.assertEqual(log_buffer.head, log)
        self.assertEqual(log_buffer.tail, log3)
        self.assertEqual(log_buffer.head.next, log2)
        self.assertEqual(log_buffer.head.previous, None)
        self.assertEqual(log_buffer.tail.next, None)
        self.assertEqual(log_buffer.tail.previous, log2)
        self.assertEqual(log_buffer.tail.previous.previous, log)

    def test_add_fourth(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        log2 = Log("test2", INFO)
        log3 = Log("test3", SUCCESS)
        log4 = Log("test4", WARNING)
        # Act
        log_buffer.add(log)
        log_buffer.add(log2)
        log_buffer.add(log3)
        log_buffer.add(log4)
        # Assert
        self.assertEqual(log_buffer.head, log)
        self.assertEqual(log_buffer.tail, log4)
        self.assertEqual(log_buffer.head.next, log2)
        self.assertEqual(log_buffer.head.previous, None)
        self.assertEqual(log_buffer.tail.next, None)
        self.assertEqual(log_buffer.tail.previous, log3)
        self.assertEqual(log_buffer.tail.previous.previous, log2)

    def test_add_four_in_mixed_order(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        sleep(0.01)
        log2 = Log("test2", INFO)
        sleep(0.01)
        log3 = Log("test3", SUCCESS)
        sleep(0.01)
        log4 = Log("test4", WARNING)
        # Act
        log_buffer.add(log4)
        log_buffer.add(log)
        log_buffer.add(log3)
        log_buffer.add(log2)
        # Assert
        self.assertEqual(log_buffer.head, log)
        self.assertEqual(log_buffer.tail, log4)
        self.assertEqual(log_buffer.head.next, log2)
        self.assertEqual(log_buffer.head.previous, None)
        self.assertEqual(log_buffer.tail.next, None)
        self.assertEqual(log_buffer.tail.previous, log3)
        self.assertEqual(log_buffer.tail.previous.previous, log2)

    def test_add_four_in_mixed_order_with_remove(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        sleep(0.01)
        log2 = Log("test2", INFO)
        sleep(0.01)
        log3 = Log("test3", SUCCESS)
        sleep(0.01)
        log4 = Log("test4", WARNING)
        # Act
        log_buffer.add(log4)
        log_buffer.add(log)
        log_buffer.add(log3)
        log_buffer.add(log2)
        log_buffer.get()
        # Assert
        self.assertEqual(log_buffer.head, log2)
        self.assertEqual(log_buffer.tail, log4)
        self.assertEqual(log_buffer.head.next, log3)
        self.assertEqual(log_buffer.head.previous, None)
        self.assertEqual(log_buffer.tail.next, None)
        self.assertEqual(log_buffer.tail.previous, log3)
        self.assertEqual(log_buffer.tail.previous.previous, log2)

    def test_add_four_in_mixed_order_with_remove_and_add(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        sleep(0.01)
        log2 = Log("test2", INFO)
        sleep(0.01)
        log3 = Log("test3", SUCCESS)
        sleep(0.01)
        log4 = Log("test4", WARNING)
        # Act
        log_buffer.add(log4)
        log_buffer.add(log)
        log_buffer.add(log3)
        log_buffer.add(log2)
        log_buffer.get()
        log_buffer.add(log)

        # Assert
        self.assertEqual(log_buffer.head, log)
        self.assertEqual(log_buffer.tail, log4)
        self.assertEqual(log_buffer.head.next, log2)
        self.assertEqual(log_buffer.head.previous, None)
        self.assertEqual(log_buffer.tail.next, None)
        self.assertEqual(log_buffer.tail.previous, log3)
        self.assertEqual(log_buffer.tail.previous.previous, log2)

    def test_add_four_in_mixed_order_with_remove_and_add_and_remove(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        sleep(0.01)
        log2 = Log("test2", INFO)
        sleep(0.01)
        log3 = Log("test3", SUCCESS)
        sleep(0.01)
        log4 = Log("test4", WARNING)
        # Act
        log_buffer.add(log4)
        log_buffer.add(log)
        log_buffer.add(log3)
        log_buffer.add(log2)
        log_buffer.get()
        log_buffer.add(log)
        log_buffer.get()
        # Assert
        self.assertEqual(log_buffer.head, log2)
        self.assertEqual(log_buffer.tail, log4)
        self.assertEqual(log_buffer.head.next, log3)
        self.assertEqual(log_buffer.head.previous, None)
        self.assertEqual(log_buffer.tail.next, None)
        self.assertEqual(log_buffer.tail.previous, log3)
        self.assertEqual(log_buffer.tail.previous.previous, log2)

    def test_remove_all(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        log2 = Log("test2", INFO)
        log3 = Log("test3", SUCCESS)
        log4 = Log("test4", WARNING)
        # Act
        log_buffer.add(log)
        log_buffer.add(log2)
        log_buffer.add(log3)
        log_buffer.add(log4)
        log_buffer.get()
        log_buffer.get()
        log_buffer.get()
        log_buffer.get()
        # Assert
        self.assertEqual(log_buffer.head, None)
        self.assertEqual(log_buffer.tail, None)

    def test_remove_all_and_add(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        log2 = Log("test2", INFO)
        log3 = Log("test3", SUCCESS)
        log4 = Log("test4", WARNING)
        # Act
        log_buffer.add(log)
        log_buffer.add(log2)
        log_buffer.add(log3)
        log_buffer.add(log4)
        log_buffer.get()
        log_buffer.get()
        log_buffer.get()
        log_buffer.get()
        log_buffer.add(log)
        # Assert
        self.assertEqual(log_buffer.head, log)
        self.assertEqual(log_buffer.tail, log)

    def test_remove_to_one_left(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        log2 = Log("test2", INFO)
        log3 = Log("test3", SUCCESS)
        log4 = Log("test4", WARNING)
        # Act
        log_buffer.add(log)
        log_buffer.add(log2)
        log_buffer.add(log3)
        log_buffer.add(log4)
        log_buffer.get()
        log_buffer.get()
        log_buffer.get()
        # Assert
        self.assertEqual(log_buffer.head, log4)
        self.assertEqual(log_buffer.tail, log4)

    def test_remove_to_two_left(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        log2 = Log("test2", INFO)
        log3 = Log("test3", SUCCESS)
        log4 = Log("test4", WARNING)
        # Act
        log_buffer.add(log)
        log_buffer.add(log2)
        log_buffer.add(log3)
        log_buffer.add(log4)
        log_buffer.get()
        log_buffer.get()
        # Assert
        self.assertEqual(log_buffer.head, log3)
        self.assertEqual(log_buffer.tail, log4)

    def test_str_representation(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        log2 = Log("test2", INFO)
        log3 = Log("test3", SUCCESS)
        log4 = Log("test4", WARNING)
        # Act
        log_buffer.add(log)
        log_buffer.add(log2)
        log_buffer.add(log3)
        log_buffer.add(log4)
        # Assert
        res = f"{str(log)}\n{str(log2)}\n{str(log3)}\n{str(log4)}\n"
        self.assertEqual(str(log_buffer), res)

    def test_dump_to_file(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        log2 = Log("test2", INFO)
        log3 = Log("test3", SUCCESS)
        log4 = Log("test4", WARNING)
        # Act
        log_buffer.add(log)
        log_buffer.add(log2)
        log_buffer.add(log3)
        log_buffer.add(log4)
        expected = str(log_buffer)
        log_buffer.dump_to_file("test.txt")
        # Assert
        with open("test.txt", "r") as f:
            actual = f.read()
        self.assertEqual(expected, actual)

    def test_dump_to_file_with_empty_buffer(self):
        # Arrange
        log_buffer = LogBuffer()
        # Act
        log_buffer.dump_to_file("test.txt")
        # Assert
        with open("test.txt", "r") as f:
            actual = f.read()
        self.assertEqual("", actual)

    def test_length(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        log2 = Log("test2", INFO)
        log3 = Log("test3", SUCCESS)
        log4 = Log("test4", WARNING)
        # Act
        log_buffer.add(log)
        log_buffer.add(log2)
        log_buffer.add(log3)
        log_buffer.add(log4)
        # Assert
        self.assertEqual(len(log_buffer), 4)

    def test_length_with_empty_buffer(self):
        # Arrange
        log_buffer = LogBuffer()
        # Act
        # Assert
        self.assertEqual(len(log_buffer), 0)

    def test_length_with_one_element(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        # Act
        log_buffer.add(log)
        # Assert
        self.assertEqual(len(log_buffer), 1)

    def test_length_with_add_get(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        log2 = Log("test2", INFO)
        log3 = Log("test3", SUCCESS)
        log4 = Log("test4", WARNING)
        # Act
        log_buffer.add(log)
        log_buffer.add(log2)
        log_buffer.add(log3)
        log_buffer.add(log4)
        log_buffer.get()
        log_buffer.get()
        log_buffer.get()
        log_buffer.get()
        # Assert
        self.assertEqual(len(log_buffer), 0)

    def test_length_with_add_get_add(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        log2 = Log("test2", INFO)
        log3 = Log("test3", SUCCESS)
        log4 = Log("test4", WARNING)
        # Act
        log_buffer.add(log)
        log_buffer.add(log2)
        log_buffer.add(log3)
        log_buffer.add(log4)
        log_buffer.get()
        log_buffer.get()
        log_buffer.get()
        log_buffer.get()
        log_buffer.add(log)
        # Assert
        self.assertEqual(len(log_buffer), 1)

    def test_length_with_add_get_add_get(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        log2 = Log("test2", INFO)
        log3 = Log("test3", SUCCESS)
        log4 = Log("test4", WARNING)
        # Act
        log_buffer.add(log)
        log_buffer.add(log2)
        log_buffer.add(log3)
        log_buffer.add(log4)
        log_buffer.get()
        log_buffer.get()
        log_buffer.get()
        log_buffer.get()
        log_buffer.add(log)
        log_buffer.get()
        # Assert
        self.assertEqual(len(log_buffer), 0)

    def test_length_with_remove_to_two_left(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        log2 = Log("test2", INFO)
        log3 = Log("test3", SUCCESS)
        log4 = Log("test4", WARNING)
        # Act
        log_buffer.add(log)
        log_buffer.add(log2)
        log_buffer.add(log3)
        log_buffer.add(log4)
        log_buffer.get()
        log_buffer.get()
        # Assert
        self.assertEqual(len(log_buffer), 2)

    def test_length_with_remove_to_one_left(self):
        # Arrange
        log_buffer = LogBuffer()
        log = Log("test", DEBUG)
        log2 = Log("test2", INFO)
        log3 = Log("test3", SUCCESS)
        log4 = Log("test4", WARNING)
        # Act
        log_buffer.add(log)
        log_buffer.add(log2)
        log_buffer.add(log3)
        log_buffer.add(log4)
        log_buffer.get()
        log_buffer.get()
        log_buffer.get()
        # Assert
        self.assertEqual(len(log_buffer), 1)


if __name__ == "__main__":
    unittest.main()