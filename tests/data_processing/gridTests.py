import unittest

from models.data_processing.grid import *

class SettingsTests(unittest.TestCase):

    def test_check_correct_waveLength1_456039(self):
        # Arrange
        grid = Grid456039()
        # Act
        result = grid.get_wave_length(13.746)
        # Assert
        self.assertEqual(7300.0946014708625, result)

    def test_check_correct_waveLength2_456039(self):
        # Arrange
        grid = Grid456039()
        # Act
        result = grid.get_wave_length(29.439)
        # Assert
        self.assertEqual(15099.743664394833, result)

    def test_check_correct_waveLength1_465645(self):
        # Arrange
        grid = Grid465645()
        # Act
        result = grid.get_wave_length(13.746)
        # Assert
        self.assertEqual(1.472094839926199, result)

    def test_check_correct_waveLength2_465645(self):
        # Arrange
        grid = Grid465645()
        # Act
        result = grid.get_wave_length(29.439)
        # Assert
        self.assertEqual(3.035446779217908, result)

    def test_check_correct_waveLength1_455931(self):
        # Arrange
        grid = Grid455931()
        # Act
        result = grid.get_wave_length(13.858)
        # Assert
        self.assertEqual(4200.26353934956, result)

    def test_check_correct_waveLength2_455931(self):
        # Arrange
        grid = Grid455931()
        # Act
        result = grid.get_wave_length(28.992)
        # Assert
        self.assertEqual(12000.093014439637, result)

if __name__ == "__main__":
    unittest.main()