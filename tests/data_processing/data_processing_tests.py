import unittest

from measurementSettings import measurementSettings
from models.data_processing.data_processing import DataProcessing
from errors.data_processing_error import DataProcessingError


class DataProcessingTests(unittest.TestCase):
    def test_successful_create_file(self):
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

        dp = DataProcessing()
        dp.setSettings(s)
        dp.setFileName("mojPokusOHlavicku")

        # Act
        try:
            dp.createNewFile()
            # Assert
            self.assertTrue(True)
        except DataProcessingError:
            self.assertTrue(False)

    def test_unsuccessful_create_file1(self):
        # Arrange
        settingsDict = {
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

        dp = DataProcessing()
        dp.setSettings(s)
        # Act
        try:
            dp.createNewFile()
            # Assert
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual("Legenda nie je kompletne vyplnená. Nie je možne vytvoriť nový súbor pre meranie.",
                             e.message)

    def test_unsuccessful_create_file2(self):
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
            'startAngstrom': '340', 'endAngle': '200',
            'stepOfMotor': '1.3', 'numberOfIntegrations': '1',
            'correction': '2', 'lockIn': 'Lockin nano voltmeter type 232',
            'lockInReference': '1.4', 'range': '2.44',
            'phaseShift': '1', 'timeConstante': '1'
        }

        s = measurementSettings()
        for key, value in settingsDict.items():
            s.setSetting(key, value)

        dp = DataProcessing()
        dp.setSettings(s)
        try:
            #act
            dp.createNewFile()
            # Assert
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual("Legenda nie je kompletne vyplnená. Nie je možne vytvoriť nový súbor pre meranie.",
                             e.message)

    def test_creating_file_without_name(self):
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

        dp = DataProcessing()
        dp.setSettings(s)
        try:
            # Act
            dp.createNewFile()
            # Assert
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual("Nie je vyplnené meno súboru. Nie je možné vytvoriť nový súbor pre meranie.",
                             e.message)
        
    def test_add_measurement_succesfull(self):
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

        dp = DataProcessing()
        dp.setSettings(s)
        dp.setFileName("mojPokusOHlavicku")
        dp.createNewFile()

        try:
            # Act
            dp.addMeasurement(2.34, 5.002, 12.223)
        except DataProcessingError as e:
            self.assertTrue(False)
            return

        # Assert
        with open(dp.path + dp.fileName, 'r', encoding="utf-8") as f:
            line = f.readline()
            while line != '' :
                lastLine = line
                line = f.readline()

        rightResult = '{: <20s}\t{: <20s}\t{}'.format(str(2.34), str(5.002), str(12.223))
        self.assertEqual(rightResult, lastLine)

    def test_add_multiple_measurement_succesfull(self):
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

        dp = DataProcessing()
        dp.setSettings(s)
        dp.setFileName("mojPokusOHlavicku")
        dp.createNewFile()
        # Act
        try:
            dp.addMeasurement(2.38928190194, 5.00216871718, 12.22921291829103)
            dp.addMeasurement(0.24, 19.63727, 1.11)
            dp.addMeasurement(3, 1, 18)#
        except DataProcessingError:
            self.assertTrue(False)
            return

        # Assert
        with open(dp.path + dp.fileName, 'r', encoding="utf-8") as f:
            line = f.readline()
            while line != '':
                lastLine = line
                line = f.readline()

        rightResult = '{: <20s}\t{: <20s}\t{}'.format(str(3), str(1), str(18))
        self.assertEqual(rightResult, lastLine)

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
        self.assertEqual("C:\\Desktop\\priecinok\\pokus1.txt", dp.path + dp.fileName)

    def test_set_file_path2(self):
        # Arrange
        dp = DataProcessing()
        # Act
        dp.setFileName("pokus1")
        dp.setFilePath("C:\\Desktop\\priecinok\\")
        # Assert
        self.assertEqual("C:\\Desktop\\priecinok\\pokus1.txt",
                         dp.path + dp.fileName)

    def test_load_measurement_from_file_no_measurements(self):
        # Arrange
        dp = DataProcessing()
        s = measurementSettings()
        dp.setSettings(s)
        fileName = "test_file_no_measurements.txt"
        # Act
        try:
            dp.loadMeasurements(fileName)
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual(e.message, "Načítaný súbor nie je v správnom formáte. Neobsahuje nameraná údaje.")

    def test_load_measurement_from_file_not_enough_collums(self):
        # Arrange
        dp = DataProcessing()
        s = measurementSettings()
        dp.setSettings(s)
        fileName = "test_file_not_enough_collums.txt"
        # Act
        try:
            dp.loadMeasurements(fileName)
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual(e.message, "Načítaný súbor nie je v správnom formáte. Namerané údaje sú v zlom formáte.")

    def test_load_measurement_from_file_not_float(self):
        # Arrange
        dp = DataProcessing()
        s = measurementSettings()
        dp.setSettings(s)
        fileName = "test_file_not_float.txt"
        # Act
        try:
            dp.loadMeasurements(fileName)
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual(e.message, "Načítaný súbor nie je v správnom formáte. Namerané údaje sú v zlom formáte.")

    def test_load_measurement_from_file_right_data(self):
        # Arrange
        dp = DataProcessing()
        s = measurementSettings()
        dp.setSettings(s)
        fileName = "test_file_right_data.txt"
        # Act
        legend, listOfMeasurements = dp.loadMeasurements(fileName)
        # Assert
        self.assertEqual([[13.2, 92], [2.03, 3.00001]], listOfMeasurements)

    def test_load_measurement_from_file_without_start_of_measurments(self):
        # Arrange
        dp = DataProcessing()
        s = measurementSettings()
        dp.setSettings(s)
        fileName = "test_file_without_start_of_measurments.txt"
        # Act
        try:
            dp.loadMeasurements(fileName)
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual(e.message, "Načítaný súbor nie je v správnom formáte. Neobsahuje nameraná údaje.")

    def test_load_measurement_from_file_wrong_legend(self):
        # Arrange
        dp = DataProcessing()
        s = measurementSettings()
        dp.setSettings(s)
        fileName = "test_file_wrong_legend.txt"
        # Act
        try:
            dp.loadMeasurements(fileName)
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual(e.message, "Legenda v načítanom súbore je v nespravnom formáte.")

    def test_load_measurement_from_file_no_legend(self):
        # Arrange
        dp = DataProcessing()
        s = measurementSettings()
        dp.setSettings(s)
        fileName = "test_file_no_legend.txt"
        # Act
        try:
            dp.loadMeasurements(fileName)
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual(e.message, "Legenda v načítanom súbore je v nespravnom formáte.")

if __name__ == "__main__":
    unittest.main()