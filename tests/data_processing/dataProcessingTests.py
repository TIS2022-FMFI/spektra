import unittest

from models.data_processing.measurementSettings import MeasurementSettings
from models.data_processing.dataProcessing import DataProcessing
from errors.data_processing_error import DataProcessingError
from models.data_processing.constants import *


class DataProcessingTests(unittest.TestCase):
    def test_successful_create_file(self):
        # Arrange
        settingsDict = {
            NAME_SAMPLE_KEY: 'utorkajsia vzorka',
            NOTE_TO_TECH_KEY: 'blabla', THICKNESS_KEY: '11.3',
            MEASURE_OF_SAMPLE_KEY: 'ref', TEMPERATURE_KEY: '15.4',
            NAME_OF_DISPERS_ELEM_KEY: 'M465645', INPUT_CREVICE_END_KEY: '3.4',
            INPUT_CREVICE_BEGIN_KEY: '2.4', OUTPUT_CREVICE_END_KEY: '5.3',
            OUTPUT_CREVICE_BEGIN_KEY: '3.4', OPTICAL_FILTER_KEY: 'filter',
            TYPE_OF_DETECTOR_KEY: 'Si-fotodioda', ADDITIONAL_INFO_DETECTOR_KEY: 'nazov',
            TYPE_LIGHT_KEY: 'Laser', NAME_LIGHT_KEY: 'nadupany',
            START_POSITION_KEY: '340', END_POSITION_KEY: '200',
            STEP_OF_MOTOR_KEY: '1.3', NUM_OF_INTEGRATIONS_KEY: '1',
            CORRECTION_KEY: '2', LOCK_IN_KEY: 'Lockin nano voltmeter type 232',
            LOCK_IN_REFERENCE_KEY: '1.4', RANGE_KEY: '2.44',
            PHASE_SHIFT_KEY: '1', TIME_CONSTANT_KEY: '1'
        }

        dp = DataProcessing(None)
        for key, value in settingsDict.items():
            dp.set_legend_field(key, value)

        dp.set_file_name("mojPokusOHlavicku")

        # Act
        try:
            dp.create_new_file()
            # Assert
            self.assertTrue(True)
        except DataProcessingError:
            self.assertTrue(False)

    def test_unsuccessful_create_file1(self):
        # Arrange
        settingsDict = {
            MEASURE_OF_SAMPLE_KEY: 'ref', TEMPERATURE_KEY: '15.4',
            NAME_OF_DISPERS_ELEM_KEY: 'M465645', INPUT_CREVICE_END_KEY: '3.4',
            INPUT_CREVICE_BEGIN_KEY: '2.4', OUTPUT_CREVICE_END_KEY: '5.3',
            OUTPUT_CREVICE_BEGIN_KEY: '3.4', OPTICAL_FILTER_KEY: 'filter',
            TYPE_OF_DETECTOR_KEY: 'Si-fotodioda', ADDITIONAL_INFO_DETECTOR_KEY: 'nazov',
            TYPE_LIGHT_KEY: 'Laser', NAME_LIGHT_KEY: 'nadupany',
            START_POSITION_KEY: '340', END_POSITION_KEY: '200',
            STEP_OF_MOTOR_KEY: '1.3', NUM_OF_INTEGRATIONS_KEY: '1',
            CORRECTION_KEY: '2', LOCK_IN_KEY: 'Lockin nano voltmeter type 232',
            LOCK_IN_REFERENCE_KEY: '1.4', RANGE_KEY: '2.44',
            PHASE_SHIFT_KEY: '1', TIME_CONSTANT_KEY: '1'
        }

        dp = DataProcessing(None)
        for key, value in settingsDict.items():
            dp.set_legend_field(key, value)

        # Act
        try:
            dp.create_new_file()
            # Assert
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual("Legenda nie je kompletne vyplnená. Nie je možne vytvoriť nový súbor pre meranie.",
                             e.message)

    def test_successful_create_file_angle(self):
        # Arrange
        settingsDict = {
            NAME_SAMPLE_KEY: 'utorkajsia vzorka',
            NOTE_TO_TECH_KEY: 'blabla', THICKNESS_KEY: '11.3',
            MEASURE_OF_SAMPLE_KEY: 'ref', TEMPERATURE_KEY: '15.4',
            NAME_OF_DISPERS_ELEM_KEY: 'M465645', INPUT_CREVICE_END_KEY: '3.4',
            INPUT_CREVICE_BEGIN_KEY: '2.4', OUTPUT_CREVICE_END_KEY: '5.3',
            OUTPUT_CREVICE_BEGIN_KEY: '3.4', OPTICAL_FILTER_KEY: 'filter',
            TYPE_OF_DETECTOR_KEY: 'Si-fotodioda', ADDITIONAL_INFO_DETECTOR_KEY: 'nazov',
            TYPE_LIGHT_KEY: 'Laser', NAME_LIGHT_KEY: 'nadupany',
            START_POSITION_KEY: '340', END_POSITION_KEY: '200',
            STEP_OF_MOTOR_KEY: '1.3', NUM_OF_INTEGRATIONS_KEY: '1',
            CORRECTION_KEY: '2', LOCK_IN_KEY: 'Lockin nano voltmeter type 232',
            LOCK_IN_REFERENCE_KEY: '1.4', RANGE_KEY: '2.44',
            PHASE_SHIFT_KEY: '1', TIME_CONSTANT_KEY: '1'
        }

        dp = DataProcessing(None)
        dp.set_file_name("mojPokusOHlavicku")
        for key, value in settingsDict.items():
            dp.set_legend_field(key, value)

        dp.set_unit_type_position(Unit.Uhol)

        dp.create_new_file()

    def test_creating_file_without_name(self):
        # Arrange
        settingsDict = {
            NAME_SAMPLE_KEY: 'utorkajsia vzorka',
            NOTE_TO_TECH_KEY: 'blabla', THICKNESS_KEY: '11.3',
            MEASURE_OF_SAMPLE_KEY: 'ref', TEMPERATURE_KEY: '15.4',
            NAME_OF_DISPERS_ELEM_KEY: 'M465645', INPUT_CREVICE_END_KEY: '3.4',
            INPUT_CREVICE_BEGIN_KEY: '2.4', OUTPUT_CREVICE_END_KEY: '5.3',
            OUTPUT_CREVICE_BEGIN_KEY: '3.4', OPTICAL_FILTER_KEY: 'filter',
            TYPE_OF_DETECTOR_KEY: 'Si-fotodioda', ADDITIONAL_INFO_DETECTOR_KEY: 'nazov',
            TYPE_LIGHT_KEY: 'Laser', NAME_LIGHT_KEY: 'nadupany',
            START_POSITION_KEY: '340', END_POSITION_KEY: '200',
            STEP_OF_MOTOR_KEY: '1.3', NUM_OF_INTEGRATIONS_KEY: '1',
            CORRECTION_KEY: '2', LOCK_IN_KEY: 'Lockin nano voltmeter type 232',
            LOCK_IN_REFERENCE_KEY: '1.4', RANGE_KEY: '2.44',
            PHASE_SHIFT_KEY: '1', TIME_CONSTANT_KEY: '1'
        }

        dp = DataProcessing(None)
        for key, value in settingsDict.items():
            dp.set_legend_field(key, value)

        try:
            # Act
            dp.create_new_file()
            # Assert
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual("Nie je vyplnené meno súboru. Nie je možné vytvoriť nový súbor pre meranie.",
                             e.message)
        
    def test_add_measurement_succesfull(self):
        # Arrange
        settingsDict = {
            NAME_SAMPLE_KEY: 'utorkajsia vzorka',
            NOTE_TO_TECH_KEY: 'blabla', THICKNESS_KEY: '11.3',
            MEASURE_OF_SAMPLE_KEY: 'ref', TEMPERATURE_KEY: '15.4',
            NAME_OF_DISPERS_ELEM_KEY: 'M465645', INPUT_CREVICE_END_KEY: '3.4',
            INPUT_CREVICE_BEGIN_KEY: '2.4', OUTPUT_CREVICE_END_KEY: '5.3',
            OUTPUT_CREVICE_BEGIN_KEY: '3.4', OPTICAL_FILTER_KEY: 'filter',
            TYPE_OF_DETECTOR_KEY: 'Si-fotodioda', ADDITIONAL_INFO_DETECTOR_KEY: 'nazov',
            TYPE_LIGHT_KEY: 'Laser', NAME_LIGHT_KEY: 'nadupany',
            START_POSITION_KEY: '340', END_POSITION_KEY: '200',
            STEP_OF_MOTOR_KEY: '1.3', NUM_OF_INTEGRATIONS_KEY: '1',
            CORRECTION_KEY: '2', LOCK_IN_KEY: 'Lockin nano voltmeter type 232',
            LOCK_IN_REFERENCE_KEY: '1.4', RANGE_KEY: '2.44',
            PHASE_SHIFT_KEY: '1', TIME_CONSTANT_KEY: '1'
        }

        dp = DataProcessing(None)
        for key, value in settingsDict.items():
            dp.set_legend_field(key, value)

        dp.set_file_name("mojPokusOHlavicku")
        dp.create_new_file()

        try:
            # Act
            dp.add_measurement(2.34, 5.002, 12.223)
        except DataProcessingError as e:
            self.assertTrue(False)
            return

        # Assert
        with open(dp.path + dp.file_name, 'r', encoding="utf-8") as f:
            line = f.readline()
            while line != '' :
                lastLine = line
                line = f.readline()

        rightResult = '{: <20s}\t{: <20s}\t{}'.format(str(2.34), str(5.002), str(12.223))
        self.assertEqual(rightResult, lastLine)

    def test_add_multiple_measurement_succesfull(self):
        # Arrange
        settingsDict = {
            NAME_SAMPLE_KEY: 'utorkajsia vzorka',
            NOTE_TO_TECH_KEY: 'blabla', THICKNESS_KEY: '11.3',
            MEASURE_OF_SAMPLE_KEY: 'ref', TEMPERATURE_KEY: '15.4',
            NAME_OF_DISPERS_ELEM_KEY: 'M465645', INPUT_CREVICE_END_KEY: '3.4',
            INPUT_CREVICE_BEGIN_KEY: '2.4', OUTPUT_CREVICE_END_KEY: '5.3',
            OUTPUT_CREVICE_BEGIN_KEY: '3.4', OPTICAL_FILTER_KEY: 'filter',
            TYPE_OF_DETECTOR_KEY: 'Si-fotodioda', ADDITIONAL_INFO_DETECTOR_KEY: 'nazov',
            TYPE_LIGHT_KEY: 'Laser', NAME_LIGHT_KEY: 'nadupany',
            START_POSITION_KEY: '340', END_POSITION_KEY: '200',
            STEP_OF_MOTOR_KEY: '1.3', NUM_OF_INTEGRATIONS_KEY: '1',
            CORRECTION_KEY: '2', LOCK_IN_KEY: 'Lockin nano voltmeter type 232',
            LOCK_IN_REFERENCE_KEY: '1.4', RANGE_KEY: '2.44',
            PHASE_SHIFT_KEY: '1', TIME_CONSTANT_KEY: '1'
        }

        dp = DataProcessing(None)
        for key, value in settingsDict.items():
            dp.set_legend_field(key, value)

        dp.set_file_name("mojPokusOHlavicku")
        dp.create_new_file()
        # Act
        try:
            dp.add_measurement(2.38928190194, 5.00216871718, 12.22921291829103)
            dp.add_measurement(0.24, 19.63727, 1.11)
            dp.add_measurement(3, 1, 18)#
        except DataProcessingError:
            self.assertTrue(False)
            return

        # Assert
        with open(dp.path + dp.file_name, 'r', encoding="utf-8") as f:
            line = f.readline()
            while line != '':
                lastLine = line
                line = f.readline()

        rightResult = '{: <20s}\t{: <20s}\t{}'.format(str(3), str(1), str(18))
        self.assertEqual(rightResult, lastLine)

    def test_set_file_name(self):
        # Arrange
        dp = DataProcessing(None)
        # Act
        dp.set_file_name("pokus1.txt")
        # Assert
        self.assertEqual("pokus1.txt", dp.file_name)

    def test_set_file_path1(self):
        # Arrange
        dp = DataProcessing(None)
        # Act
        dp.set_file_name("pokus1")
        dp.set_file_path("C:\\Desktop\\priecinok")
        # Assert
        self.assertEqual("C:\\Desktop\\priecinok\\pokus1.txt", dp.path + dp.file_name)

    def test_set_file_path2(self):
        # Arrange
        dp = DataProcessing(None)
        # Act
        dp.set_file_name("pokus1")
        dp.set_file_path("C:\\Desktop\\priecinok\\")
        # Assert
        self.assertEqual("C:\\Desktop\\priecinok\\pokus1.txt",
                         dp.path + dp.file_name)

    def test_load_measurement_from_file_no_measurements(self):
        # Arrange
        dp = DataProcessing(None)

        fileName = "test_file_no_measurements.txt"
        # Act
        try:
            dp.load_old_file(fileName)
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual(e.message, "Načítaný súbor nie je v správnom formáte. Neobsahuje nameraná údaje.")

    def test_load_measurement_from_file_not_enough_collums(self):
        # Arrange
        dp = DataProcessing(None)

        fileName = "test_file_not_enough_collums.txt"
        # Act
        try:
            dp.load_old_file(fileName)
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual(e.message, "Načítaný súbor nie je v správnom formáte. Namerané údaje sú v zlom formáte.")

    def test_load_measurement_from_file_not_float(self):
        # Arrange
        dp = DataProcessing(None)

        fileName = "test_file_not_float.txt"
        # Act
        try:
            dp.load_old_file(fileName)
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual(e.message, "Načítaný súbor nie je v správnom formáte. Namerané údaje sú v zlom formáte.")

    def test_load_measurement_from_file_right_data(self):
        # Arrange
        dp = DataProcessing(None)

        fileName = "test_file_right_data.txt"
        # Act
        legend, listOfMeasurements = dp.load_old_file(fileName)
        # Assert
        self.assertEqual([[13.2, 92], [2.03, 3.00001]], listOfMeasurements)

    def test_load_measurement_from_file_without_start_of_measurments(self):
        # Arrange
        dp = DataProcessing(None)

        fileName = "test_file_without_start_of_measurments.txt"
        # Act
        try:
            dp.load_old_file(fileName)
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual(e.message, "Načítaný súbor nie je v správnom formáte. Neobsahuje nameraná údaje.")

    def test_load_measurement_from_file_wrong_legend(self):
        # Arrange
        dp = DataProcessing(None)

        fileName = "test_file_wrong_legend.txt"
        # Act
        try:
            dp.load_old_file(fileName)
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual(e.message, "Legenda v načítanom súbore je v nespravnom formáte.")

    def test_load_measurement_from_file_no_legend(self):
        # Arrange
        dp = DataProcessing(None)

        fileName = "test_file_no_legend.txt"
        # Act
        try:
            dp.load_old_file(fileName)
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual(e.message, "Legenda v načítanom súbore je v nespravnom formáte.")

if __name__ == "__main__":
    unittest.main()