import unittest

from models.data_processing.settings import settings
from models.data_processing.data_processing import DataProcessing


class DataProcessingTests(unittest.TestCase):



    def test_successful_create_file(self):
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

        s = settings()
        for key, value in settingsDict.items():
            s.setSetting(key, value)

        dp = DataProcessing()
        dp.setFilePath("C:\\Users\\lucin\\OneDrive\\Desktop\\spektra\\spektra")
        dp.setFileName("mojPokusOHlavicku")

        # Act
        result = dp.createNewFile(s)
        # Assert
        self.assertTrue(result)

    def test_unsuccessful_create_file1(self):
        # Arrange
        settingsDict = {
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

        s = settings()
        for key, value in settingsDict.items():
            s.setSetting(key, value)

        dp = DataProcessing()

        # Act
        result = dp.createNewFile(s)
        # Assert
        self.assertFalse(result)

    def test_unsuccessful_create_file2(self):
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
            'startAngstrom': '340', 'endAngle': '200',
            'stepOfMotor': '1.3', 'numberOfMitigations': '1',
            'correction': '2', 'lockIn': 'Lockin nano voltmeter type 232',
            'lockInReference': '1.4', 'lockInFilter': 'signal filters',
            'phaseShift': '1', 'timeConstante': '1'
        }

        s = settings()
        for key, value in settingsDict.items():
            s.setSetting(key, value)

        dp = DataProcessing()

        # Act
        result = dp.createNewFile(s)
        # Assert
        self.assertFalse(result)

    def test_creating_file_without_name(self):
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

        s = settings()
        for key, value in settingsDict.items():
            s.setSetting(key, value)

        dp = DataProcessing()

        # Act
        result = dp.createNewFile(s)
        # Assert
        self.assertFalse(result)

    def test_set_file_name(self):
        # Arrange
        dp = DataProcessing()
        # Act
        dp.setFileName("pokus1")
        # Assert
        self.assertEqual("pokus1.txt", dp.fileName)

    def test_set_file_path1(self):
        # Arrange
        dp = DataProcessing()
        # Act
        dp.setFileName("pokus1")
        dp.setFilePath("C:\\Desktop\\priecinok")
        # Assert
        self.assertEqual("C:\\Desktop\\priecinok\\pokus1.txt", dp.fileName)

    def test_set_file_path2(self):
        # Arrange
        dp = DataProcessing()
        # Act
        dp.setFileName("pokus1")
        dp.setFilePath("C:\\Desktop\\priecinok\\")
        # Assert
        self.assertEqual("C:\\Desktop\\priecinok\\pokus1.txt",
                         dp.fileName)




if __name__ == "__main__":
    unittest.main()