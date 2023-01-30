import unittest
from models.disperse_element import Grating


class TestGratingMethods(unittest.TestCase):
    AVAILABLE_GRATINGS = [Grating('465645'), Grating('465626'), Grating('456039'), Grating('455931')]
    ANGLE_WAVELENGTH = [{13.554: 1.44, 18.996: 2.00, 29.226: 3.00}, {13.746: 365, 20.981: 550, 28.374: 730},
                        {14.130: 0.75, 21.180: 1.11, 29.012: 1.49}, {13.858: 420, 21.287: 810, 28.992: 1200}]

    def test_angle_to_wavelength(self):
        """
        test if converting angles to wavelengths gives correct values
        """
        for index in range(len(self.AVAILABLE_GRATINGS)):
            grid = self.AVAILABLE_GRATINGS[index]

            for angle, wavelength in self.ANGLE_WAVELENGTH[index].items():
                self.assertEqual(round(grid.angleToWavelength(angle), 2), wavelength)

    def test_wavelength_to_angle(self):
        """
        test if converting wavelengths to angles gives correct values
        """
        for index in range(len(self.AVAILABLE_GRATINGS)):
            grid = self.AVAILABLE_GRATINGS[index]

            for angle, wavelength in self.ANGLE_WAVELENGTH[index].items():
                self.assertEqual(round(grid.wavelengthToAngle(wavelength), 3), angle)


if __name__ == '__main__':
    unittest.main()
