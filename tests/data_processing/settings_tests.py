import unittest

from models.data_processing.measurement_settings import measurement_settings
from errors.data_processing_error import data_processing_error


class SettingsTests(unittest.TestCase):

    def test_check_correct_setParam(self):
        # Arrange
        s = measurement_settings()
        # Act
        try:
            s.set_setting_field("nameSample", "utorkajsia vzorka")
            # Assert
            self.assertEqual("utorkajsia vzorka", s.legend["nameSample"])
        except data_processing_error:
            self.assertTrue(False)


    def test_check_incorrect_setParam(self):
        # Arrange
        s = measurement_settings()
        # Act
        try:
            s.set_setting_field("name", "utorkajsia vzorka")
            # Assert
            self.assertTrue(False)
        except data_processing_error as e:
            self.assertEqual("Do legendy je vkladaná neexistujúca položka (zly key).", e.message)


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
            'startPosition': '340', 'endPosition': '200',
            'stepOfMotor': '1.3', 'numberOfIntegrations': '1',
            'correction': '2', 'lockIn': 'Lockin nano voltmeter type 232',
            'lockInReference': '1.4', 'range': '2.44',
            'phaseShift': '1', 'timeConstante': '1'
        }

        s = measurement_settings()
        for key, value in settingsDict.items():
            s.set_setting_field(key, value)

        # Act
        result = s.check_completness_of_legend()
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
            'startPosition': '340', 'endPosition': '200',
            'stepOfMotor': '1.3', 'numberOfIntegrations': '1',
            'correction': '2', 'lockIn': 'Lockin nano voltmeter type 232',
            'lockInReference': '1.4', 'range': '2.44',
            'phaseShift': '1', 'timeConstante': '1'
        }
        s = measurement_settings()
        for key, value in settingsDict.items():
            s.set_setting_field(key, value)

        # Act
        result = s.check_completness_of_legend()
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
            'endPosition': '200',
            'stepOfMotor': '1.3', 'numberOfIntegrations': '1',
            'correction': '2', 'lockIn': 'Lockin nano voltmeter type 232',
            'lockInReference': '1.4', 'range': '2.44',
            'phaseShift': '1', 'timeConstante': '1'
        }

        s = measurement_settings()
        for key, value in settingsDict.items():
            s.set_setting_field(key, value)

        # Act
        result = s.check_completness_of_legend()
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
            'startPosition': '340', 'endPosition': '200',
            'stepOfMotor': '1.3', 'numberOfIntegrations': '1',
            'correction': '2', 'lockIn': 'Lockin nano voltmeter type 232',
            'lockInReference': '1.4', 'range': '2.44',
            'phaseShift': '1', 'timeConstante': '1'
        }
        s = measurement_settings()
        for key, value in settingsDict.items():
            s.set_setting_field(key, value)

        # Act
        s.store_last_json_legend()
        old_legend = dict(s.legend)
        del old_legend["nameSample"]

        s.set_setting_field("lockIn", "iny lockin")
        s.set_setting_field("correction", "15")
        s.load_last_json_legend()
        # Assert
        self.assertEqual(old_legend, s.legend)

    def test_check_correct_load_from_string(self):
        # Arrange
        with open("test_file_without_start_of_measurments.txt", 'r', encoding="utf-8") as f:
            stringLegend = f.read()

        s = measurement_settings()
        # Act
        try:
            loadedSetttings = s.load_string_legend(stringLegend)
            # Assert
            self.assertEqual(stringLegend,
                             str(loadedSetttings))
        except data_processing_error as e:
            self.assertTrue(False)


    def test_check_load_from_string_wrong(self):
        # Arrange
        with open("test_file_wrong_legend.txt", 'r', encoding="utf-8") as f:
            stringLegend = f.read()
        stringLegend = "\n".join(stringLegend.split("\n")[:-3])
        s = measurement_settings()
        # Act
        try:
            s.load_string_legend(stringLegend)
            self.assertTrue(False)
        except data_processing_error as e:
            self.assertEqual("Legenda v načítanom súbore je v nespravnom formáte.",
                             e.message)

    def test_check_load_from_empty_string(self):
        # Arrange
        stringLegend = "\n \n"
        s = measurement_settings()
        s.legend = dict()
        # Act
        try:
            s.load_string_legend(stringLegend)
            self.assertTrue(False)
        except data_processing_error as e:
            self.assertEqual("Legenda v načítanom súbore je v nespravnom formáte.",
                             e.message)



if __name__ == "__main__":
    unittest.main()