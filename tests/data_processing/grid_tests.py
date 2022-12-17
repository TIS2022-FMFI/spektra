import unittest

from models.data_processing.grid import grid_456039
from models.data_processing.grid import grid_465645

class SettingsTests(unittest.TestCase):

    def test_check_correct_waveLength1_456039(self):
        # Arrange
        grid = grid_456039()
        # Act
        result = grid.get_wave_length(13.746)
        # Assert
        self.assertEqual(0.7360474199630995, result)

    def test_check_correct_waveLength2_456039(self):
        # Arrange
        grid = grid_456039()
        # Act
        result = grid.get_wave_length(29.439)
        # Assert
        self.assertEqual(1.517723389608954, result)

    def test_check_correct_waveLength1_465645(self):
        # Arrange
        grid = grid_465645()
        # Act
        result = grid.get_wave_length(13.746)
        # Assert
        self.assertEqual(1.472094839926199, result)

    def test_check_correct_waveLength2_465645(self):
        # Arrange
        grid = grid_465645()
        # Act
        result = grid.get_wave_length(29.439)
        # Assert
        self.assertEqual(3.035446779217908, result)

if __name__ == "__main__":
    unittest.main()