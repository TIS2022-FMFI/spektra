import unittest

from measurementSettings import measurementSettings
from errors.data_processing_error import DataProcessingError


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
            'measurementOfSample': 'ref', 'temperature': '15.4',
            'nameOfDispersingElement': 'M465645', 'inputCreviceEnd': '3.4',
            'inputCreviceBegin': '2.4', 'outputCreviceEnd': '5.3',
            'outputCreviceBegin': '3.4', 'opticalFilter': 'filter',
            'typeOfDetector': 'Si-fotodioda', 'additionalInfoDetector': 'nazov',
            'typeOfLight': 'Laser', 'nameOfLight': 'nadupany',
            'startAngstrom': '340', 'endAngstrom': '200',
            'stepOfMotor': '1.3', 'numberOfIntegrations': '1',
            'correction': '2', 'lockIn': 'Lockin nano voltmeter type 232',
            'lockInReference': '1.4', 'range': '2.44',
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
            'measurementOfSample': 'ref', 'temperature': '15.4',
            'nameOfDispersingElement': 'M465645', 'inputCreviceEnd': '3.4',
            'inputCreviceBegin': '2.4', 'outputCreviceEnd': '5.3',
            'outputCreviceBegin': '3.4', 'opticalFilter': 'filter',
            'typeOfDetector': 'Si-fotodioda', 'additionalInfoDetector': 'nazov',
            'typeOfLight': 'Laser', 'nameOfLight': 'nadupany',
            'startAngstrom': '340', 'endAngstrom': '200',
            'stepOfMotor': '1.3', 'numberOfIntegrations': '1',
            'correction': '2', 'lockIn': 'Lockin nano voltmeter type 232',
            'lockInReference': '1.4', 'range': '2.44',
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
            'measurementOfSample': 'ref', 'temperature': '15.4',
            'nameOfDispersingElement': 'M465645', 'inputCreviceEnd': '3.4',
            'inputCreviceBegin': '2.4', 'outputCreviceEnd': '5.3',
            'outputCreviceBegin': '3.4', 'opticalFilter': 'filter',
            'typeOfDetector': 'Si-fotodioda', 'additionalInfoDetector': 'nazov',
            'typeOfLight': 'Laser', 'nameOfLight': 'nadupany',
            'endAngstrom': '200',
            'stepOfMotor': '1.3', 'numberOfIntegrations': '1',
            'correction': '2', 'lockIn': 'Lockin nano voltmeter type 232',
            'lockInReference': '1.4', 'range': '2.44',
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
            'measurementOfSample': 'ref', 'temperature': '15.4',
            'nameOfDispersingElement': 'M465645', 'inputCreviceEnd': '3.4',
            'inputCreviceBegin': '2.4', 'outputCreviceEnd': '5.3',
            'outputCreviceBegin': '3.4', 'opticalFilter': 'filter',
            'typeOfDetector': 'Si-fotodioda', 'additionalInfoDetector': 'nazov',
            'typeOfLight': 'Laser', 'nameOfLight': 'nadupany',
            'startAngstrom': '340', 'endAngstrom': '200',
            'stepOfMotor': '1.3', 'numberOfIntegrations': '1',
            'correction': '2', 'lockIn': 'Lockin nano voltmeter type 232',
            'lockInReference': '1.4', 'range': '2.44',
            'phaseShift': '1', 'timeConstante': '1'
        }
        s = measurementSettings()
        for key, value in settingsDict.items():
            s.setSetting(key, value)

        # Act
        s.storeLastJsonLegend()
        old_legend = dict(s.legend)
        del old_legend["nameSample"]

        s.setSetting("lockIn", "iny lockin")
        s.setSetting("correction", "15")
        s.loadLastJsonLegend()
        # Assert
        self.assertEqual(old_legend, s.legend)

    def test_check_correct_load_from_string(self):
        # Arrange
        with open("test_file_without_start_of_measurments.txt", 'r', encoding="utf-8") as f:
            stringLegend = f.read()

        s = measurementSettings()
        # Act
        try:
            loadedSetttings = s.loadStringLegend(stringLegend)
            # Assert
            self.assertEqual(stringLegend,
                             str(loadedSetttings))
        except DataProcessingError as e:
            self.assertTrue(False)


    def test_check_load_from_string_wrong(self):
        # Arrange
        with open("test_file_wrong_legend.txt", 'r', encoding="utf-8") as f:
            stringLegend = f.read()
        stringLegend = "\n".join(stringLegend.split("\n")[:-3])
        s = measurementSettings()
        # Act
        try:
            s.loadStringLegend(stringLegend)
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual("Legenda v načítanom súbore je v nespravnom formáte.",
                             e.message)

    def test_check_load_from_empty_string(self):
        # Arrange
        stringLegend = "\n \n"
        s = measurementSettings()
        # Act
        try:
            s.loadStringLegend(stringLegend)
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual("Legenda v načítanom súbore je v nespravnom formáte.",
                             e.message)



if __name__ == "__main__":
    unittest.main()