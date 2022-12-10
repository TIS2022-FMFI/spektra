import unittest

from measurementSettings import measurementSettings


class SettingsTests(unittest.TestCase):

    def test_check_correct_setParam(self):
        # Arrange
        s = measurementSettings()
        # Act
        result = s.setSetting("nameSample", "utorkajsia vzorka")
        # Assert
        self.assertTrue(result)

    def test_check_incorrect_setParam(self):
        # Arrange
        s = measurementSettings()
        # Act
        result = s.setSetting("name", "utorkajsia vzorka")
        # Assert
        self.assertFalse(result)

    def test_check_correct_settings(self):
        # Arrange
        settingsDict = {
            'nameSample': 'utorkajsia vzorka',
            'noteToTech': 'blabla', 'thickness': '11.3',
            'reference': 'ref', 'temperature': '15.4',
            'nameOfDispersingElement': 'M465645', 'inputCreviceWidth': '3.4',
            'inputCreviceHeight': '2.4', 'outputCreviceWidth': '5.3',
            'outputCreviceHeight': '3.4', 'opticalFilter': 'filter',
            'typeOfDetector': 'Si-fotodioda', 'additionalInfoDetector': 'nazov',
            'typeOfLight': 'Laser', 'nameOfLight': 'nadupany',
            'startAngstrom': '340', 'endAngstrom': '200',
            'stepOfMotor': '1.3', 'numberOfMitigations': '1',
            'correction': '2', 'lockIn': 'Lockin nano voltmeter type 232',
            'lockInReference': '1.4', 'lockInFilter': 'signal filters',
            'phaseShift': '1', 'timeConstante': '1'
        }

        s = measurementSettings()
        for key, value in settingsDict.items():
            s.setSetting(key, value)

        # Act
        result = s.checkLegend()
        # Assert
        self.assertTrue(result)

    def test_check_missing_mandatory(self):
        # Arrange
        settingsDict = {
            'noteToTech': 'blabla', 'thickness': '11.3',
            'reference': 'ref', 'temperature': '15.4',
            'nameOfDispersingElement': 'M465645', 'inputCreviceWidth': '3.4',
            'inputCreviceHeight': '2.4', 'outputCreviceWidth': '5.3',
            'outputCreviceHeight': '3.4', 'opticalFilter': 'filter',
            'typeOfDetector': 'Si-fotodioda', 'additionalInfoDetector': 'nazov',
            'typeOfLight': 'Laser', 'nameOfLight': 'nadupany',
            'startAngstrom': '340', 'endAngstrom': '200',
            'stepOfMotor': '1.3', 'numberOfMitigations': '1',
            'correction': '2', 'lockIn': 'Lockin nano voltmeter type 232',
            'lockInReference': '1.4', 'lockInFilter': 'signal filters',
            'phaseShift': '1', 'timeConstante': '1'
        }
        s = measurementSettings()
        for key, value in settingsDict.items():
            s.setSetting(key, value)

        # Act
        result = s.checkLegend()
        # Assert
        self.assertFalse(result)

    def test_check_missing_alternatives(self):
        # Arrange
        settingsDict = {
            'nameSample': 'utorkajsia vzorka',
            'noteToTech': 'blabla', 'thickness': '11.3',
            'reference': 'ref', 'temperature': '15.4',
            'nameOfDispersingElement': 'M465645', 'inputCreviceWidth': '3.4',
            'inputCreviceHeight': '2.4', 'outputCreviceWidth': '5.3',
            'outputCreviceHeight': '3.4', 'opticalFilter': 'filter',
            'typeOfDetector': 'Si-fotodioda', 'additionalInfoDetector': 'nazov',
            'typeOfLight': 'Laser', 'nameOfLight': 'nadupany',
            'endAngstrom': '200',
            'stepOfMotor': '1.3', 'numberOfMitigations': '1',
            'correction': '2', 'lockIn': 'Lockin nano voltmeter type 232',
            'lockInReference': '1.4', 'lockInFilter': 'signal filters',
            'phaseShift': '1', 'timeConstante': '1'
        }

        s = measurementSettings()
        for key, value in settingsDict.items():
            s.setSetting(key, value)

        # Act
        result = s.checkLegend()
        # Assert
        self.assertFalse(result)

    def test_check_correct_load(self):
        # Arrange
        settingsDict = {
            'nameSample': 'utorkajsia vzorka',
            'noteToTech': 'blabla', 'thickness': '11.3',
            'reference': 'ref', 'temperature': '15.4',
            'nameOfDispersingElement': 'M465645', 'inputCreviceWidth': '3.4',
            'inputCreviceHeight': '2.4', 'outputCreviceWidth': '5.3',
            'outputCreviceHeight': '3.4', 'opticalFilter': 'filter',
            'typeOfDetector': 'Si-fotodioda', 'additionalInfoDetector': 'nazov',
            'typeOfLight': 'Laser', 'nameOfLight': 'nadupany',
            'startAngstrom': '340', 'endAngstrom': '200',
            'stepOfMotor': '1.3', 'numberOfMitigations': '1',
            'correction': '2', 'lockIn': 'Lockin nano voltmeter type 232',
            'lockInReference': '1.4', 'lockInFilter': 'signal filters',
            'phaseShift': '1', 'timeConstante': '1'
        }
        s = measurementSettings()
        for key, value in settingsDict.items():
            s.setSetting(key, value)

        # Act
        s.storeLastLegend()
        old_legend = dict(s.legend)
        del old_legend["nameSample"]

        s.setSetting("lockIn", "iny lockin")
        s.setSetting("correction", "15")
        s.loadLastLegend()
        # Assert
        self.assertEqual(old_legend, s.legend)


if __name__ == "__main__":
    unittest.main()