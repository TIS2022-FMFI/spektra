import unittest

from models.data_processing.measurementSettings import MeasurementSettings
from errors.data_processing_error import DataProcessingError
from models.data_processing.constants import *

class SettingsTests(unittest.TestCase):

    def test_check_correct_setParam(self):
        # Arrange
        s = MeasurementSettings()
        # Act
        try:
            s.set_setting_field("nameSample", "utorkajsia vzorka")
            # Assert
            self.assertEqual("utorkajsia vzorka", s.legend["nameSample"])
        except DataProcessingError:
            self.assertTrue(False)


    def test_check_incorrect_setParam(self):
        # Arrange
        s = MeasurementSettings()
        # Act
        try:
            s.set_setting_field("name", "utorkajsia vzorka")
            # Assert
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual("Do legendy je vkladaná neexistujúca položka (zly key).", e.message)


    def test_check_correct_settings(self):
        # Arrange
        settingsDict = {
            NAME_SAMPLE_KEY: 'utorkajsia vzorka',
            NOTE_TO_TECH_KEY: 'blabla', THICKNESS_KEY: '11.3',
            MEASURE_OF_SAMPLE_KEY: 'ref', TEMPERATURE_KEY: '15.4',
            NAME_OF_DISPERS_ELEM_KEY: 'M465645',
            MONOCHROMATOR_NAME_KEY: 'nazov monochromatora',
            INPUT_CREVICE_END_KEY: '3.4',
            INPUT_CREVICE_BEGIN_KEY: '2.4',
            OUTPUT_CREVICE_BEGIN_KEY: '3.4', OPTICAL_FILTER_KEY: 'filter',
            TYPE_OF_DETECTOR_KEY: 'Si-fotodioda', ADDITIONAL_INFO_DETECTOR_KEY: 'nazov',
            TYPE_LIGHT_KEY: 'Laser', NAME_LIGHT_KEY: 'nadupany',
            START_POSITION_KEY: '340', END_POSITION_KEY: '200',
            STEP_OF_MOTOR_KEY: '1.3', NUM_OF_INTEGRATIONS_KEY: '1',
            CORRECTION_KEY: '2', LOCK_IN_KEY: 'Lockin nano voltmeter type 232',
            LOCK_IN_REFERENCE_KEY: '1.4', RANGE_KEY: '2.44',
            PHASE_SHIFT_KEY: '1', TIME_CONSTANT_KEY: '1'
        }

        s = MeasurementSettings()
        for key, value in settingsDict.items():
            s.set_setting_field(key, value)

        # Act
        result = s.check_completness_of_legend()
        # Assert
        self.assertTrue(result)

    def test_check_missing_mandatory(self):
        # Arrange
        settingsDict = {
            NOTE_TO_TECH_KEY: 'blabla', THICKNESS_KEY: '11.3',
            MEASURE_OF_SAMPLE_KEY: 'ref', TEMPERATURE_KEY: '15.4',
            NAME_OF_DISPERS_ELEM_KEY: 'M465645',
            MONOCHROMATOR_NAME_KEY: 'nazov monochromatora',
            INPUT_CREVICE_END_KEY: '3.4',
            INPUT_CREVICE_BEGIN_KEY: '2.4',
            OUTPUT_CREVICE_BEGIN_KEY: '3.4', OPTICAL_FILTER_KEY: 'filter',
            TYPE_OF_DETECTOR_KEY: 'Si-fotodioda', ADDITIONAL_INFO_DETECTOR_KEY: 'nazov',
            TYPE_LIGHT_KEY: 'Laser', NAME_LIGHT_KEY: 'nadupany',
            START_POSITION_KEY: '340', END_POSITION_KEY: '200',
            STEP_OF_MOTOR_KEY: '1.3', NUM_OF_INTEGRATIONS_KEY: '1',
            CORRECTION_KEY: '2', LOCK_IN_KEY: 'Lockin nano voltmeter type 232',
            LOCK_IN_REFERENCE_KEY: '1.4', RANGE_KEY: '2.44',
            PHASE_SHIFT_KEY: '1', TIME_CONSTANT_KEY: '1'
        }

        s = MeasurementSettings()
        for key, value in settingsDict.items():
            s.set_setting_field(key, value)

        # Act
        result = s.check_completness_of_legend()
        # Assert
        self.assertFalse(result)

    def test_check_missing_alternatives(self):
        # Arrange
        settingsDict = {
            NAME_SAMPLE_KEY: 'utorkajsia vzorka',
            NOTE_TO_TECH_KEY: 'blabla', THICKNESS_KEY: '11.3',
            MEASURE_OF_SAMPLE_KEY: 'ref', TEMPERATURE_KEY: '15.4',
            NAME_OF_DISPERS_ELEM_KEY: 'M465645', INPUT_CREVICE_END_KEY: '3.4',
            MONOCHROMATOR_NAME_KEY: 'nazov monochromatora',
            INPUT_CREVICE_BEGIN_KEY: '2.4',
            OUTPUT_CREVICE_BEGIN_KEY: '3.4', OPTICAL_FILTER_KEY: 'filter',
            TYPE_OF_DETECTOR_KEY: 'Si-fotodioda', ADDITIONAL_INFO_DETECTOR_KEY: 'nazov',
            TYPE_LIGHT_KEY: 'Laser', NAME_LIGHT_KEY: 'nadupany',
            END_POSITION_KEY: '200',
            STEP_OF_MOTOR_KEY: '1.3', NUM_OF_INTEGRATIONS_KEY: '1',
            CORRECTION_KEY: '2', LOCK_IN_KEY: 'Lockin nano voltmeter type 232',
            LOCK_IN_REFERENCE_KEY: '1.4', RANGE_KEY: '2.44',
            PHASE_SHIFT_KEY: '1', TIME_CONSTANT_KEY: '1'
        }


        s = MeasurementSettings()
        for key, value in settingsDict.items():
            s.set_setting_field(key, value)

        # Act
        result = s.check_completness_of_legend()
        # Assert
        self.assertFalse(result)

    def test_check_correct_load(self):
        # Arrange
        settingsDict = {
            NAME_SAMPLE_KEY: 'utorkajsia vzorka',
            NOTE_TO_TECH_KEY: 'blabla', THICKNESS_KEY: '11.3',
            MEASURE_OF_SAMPLE_KEY: 'ref', TEMPERATURE_KEY: '15.4',
            NAME_OF_DISPERS_ELEM_KEY: 'M465645', INPUT_CREVICE_END_KEY: '3.4',
            MONOCHROMATOR_NAME_KEY: 'nazov monochromatora',
            INPUT_CREVICE_BEGIN_KEY: '2.4',
            OUTPUT_CREVICE_BEGIN_KEY: '3.4', OPTICAL_FILTER_KEY: 'filter',
            TYPE_OF_DETECTOR_KEY: 'Si-fotodioda', ADDITIONAL_INFO_DETECTOR_KEY: 'nazov',
            TYPE_LIGHT_KEY: 'Laser', NAME_LIGHT_KEY: 'nadupany',
            START_POSITION_KEY: '340', END_POSITION_KEY: '200',
            STEP_OF_MOTOR_KEY: '1.3', NUM_OF_INTEGRATIONS_KEY: '1',
            CORRECTION_KEY: '2', LOCK_IN_KEY: 'Lockin nano voltmeter type 232',
            LOCK_IN_REFERENCE_KEY: '1.4', RANGE_KEY: '2.44',
            PHASE_SHIFT_KEY: '1', TIME_CONSTANT_KEY: '1'
        }
        s = MeasurementSettings()
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

        s = MeasurementSettings()
        # Act
        try:

            loadedSetttings = s.load_string_legend(stringLegend)
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
        s = MeasurementSettings()
        # Act
        try:
            s.load_string_legend(stringLegend)
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual("Legenda v načítanom súbore je v nespravnom formáte.",
                             e.message)

    def test_check_load_from_empty_string(self):
        # Arrange
        stringLegend = "\n \n"
        s = MeasurementSettings()
        s.legend = dict()
        # Act
        try:
            s.load_string_legend(stringLegend)
            self.assertTrue(False)
        except DataProcessingError as e:
            self.assertEqual("Legenda v načítanom súbore je v nespravnom formáte.",
                             e.message)



if __name__ == "__main__":
    unittest.main()