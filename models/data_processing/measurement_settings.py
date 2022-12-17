import json
from datetime import datetime
import os
from errors.data_processing_error import data_processing_error
from models.data_processing.Constants import *

class measurement_settings:
    mandatory = [NAME_SAMPLE_KEY, NOTE_TO_TECH_KEY, THICKNESS_KEY,
                 MEASURE_OF_SAMPLE_KEY, TEMPERATURE_KEY,
                 TYPE_OF_DISPERS_ELEM_KEY, NAME_OF_DISPERS_ELEM_KEY,
                 INPUT_CREVICE_BEGIN_KEY, INPUT_CREVICE_END_KEY,
                 OUTPUT_CREVICE_BEGIN_KEY, OUTPUT_CREVICE_END_KEY,
                 OPTICAL_FILTER_KEY, TYPE_OF_DETECTOR_KEY,
                 ADDITIONAL_INFO_DETECTOR_KEY,
                 TYPE_LIGHT_KEY, NAME_LIGHT_KEY,
                 START_POSITION_KEY, END_POSITION_KEY,
                 STEP_OF_MOTOR_KEY, NUM_OF_INTEGRATIONS_KEY,
                 CORRECTION_KEY, LOCK_IN_KEY, TYPE_SENSITIVITY_KEY,
                 LOCK_IN_REFERENCE_KEY,
                 RANGE_KEY, PHASE_SHIFT_KEY, TIME_CONSTANT_KEY,
                 ]
    non_mandatory = [DATE_KEY, TIME_KEY]
    KEY_BEFORE_ALTERNATIVES = NAME_LIGHT_KEY

    unit_type_grid_position = WAVE_LENGTH_SYMBOL

    def __init__(self):
        self.legend = dict()
        self.set_setting_field(TYPE_OF_DISPERS_ELEM_KEY, "mriežka")
        self.set_setting_field(TYPE_SENSITIVITY_KEY, "AUTO")

        script_dir = os.path.dirname(__file__)
        rel_path = "lastSettings.txt"
        self.json_name = os.path.join(script_dir, rel_path)


    def set_unit_type_position(self, unit_type_position):
        """
        sets which unit (A°/°) is used as start and end position
        of measurement

        @param unit_type_position: symbol of used unit for position, only ANGLE_SYMBOL and
                                    WAVE_LENGTH_SYMBOL are allowed as input
        @raise data_processing_error: raises an exception if unit_type_position is not one of
                                        two allowed values
        """
        if unit_type_position != ANGLE_SYMBOL and unit_type_position != WAVE_LENGTH_SYMBOL:
            raise data_processing_error("Do legendy je vkladaná nesprávna jednotka počiatočnej/koncovej pozície merania.")
        self.unit_type_grid_position = unit_type_position

    def set_setting_field(self, key, value):
        """
        inserts value under key in self.legend. Inserts only values,
        under one of the allowed keys

        @param key: key under which will be value stored in self.legend
        @param value: value which is an input from user to the legend of a measurement
        @raise data_processing_error: raises an exception when trying to insert value under not
                                        allowed key
        """
        all_setting_keys = self.mandatory  + self.non_mandatory
        if key in all_setting_keys:
            self.legend[key] = str(value)
            return

        raise data_processing_error("Do legendy je vkladaná neexistujúca položka (zly key).")


    def check_completness_of_legend(self):
        """
        check if the legend contains all mandatory fields needed
        to work with legend
        @return: boolean value based on whether self.legend contains all
                mandatory fields of measurement settings
        """
        for legend_type in self.mandatory:
            if legend_type not in self.legend.keys():
                return False
        return True


    def __str__(self):
        """
        creates string version of the measurement settings easily understandable to
        the user of the system. Also sets current date and time in case that
        self.legend doesnt already contains date and time
        @return: string version of the measurement settings
        """
        self.set_current_date()
        self.set_current_time()

        return SAMPLE + \
               NAME_SAMPLE + self.legend[NAME_SAMPLE_KEY] + "\n" + \
               NOTE_TO_TECH + self.legend[NOTE_TO_TECH_KEY] + "\n" + \
               THICKNESS + self.legend[THICKNESS_KEY] + "\n" + \
               MEASUREMENT_OF_SAMPLE + self.legend[MEASURE_OF_SAMPLE_KEY] + "\n" + \
               TEMPERATURE + self.legend[TEMPERATURE_KEY] + "\n" + \
               DISPERSE_ELEMENT + \
               self.legend[TYPE_OF_DISPERS_ELEM_KEY] + ", " + \
               self.legend[NAME_OF_DISPERS_ELEM_KEY] + "\n" + \
               MONOCHROMATOR + \
               INPUT_CREVICE + \
               self.legend[INPUT_CREVICE_BEGIN_KEY] + ", " + \
               self.legend[INPUT_CREVICE_END_KEY] + "\n" + \
               OUTPUT_CREVICE + \
               self.legend[OUTPUT_CREVICE_BEGIN_KEY] + ", " + \
               self.legend[OUTPUT_CREVICE_END_KEY] + "\n" + \
               OPTICAL_FILTER + self.legend[OPTICAL_FILTER_KEY] + "\n" + \
               DETECTOR + \
               TYPE_OF_DETECTOR + self.legend[TYPE_OF_DETECTOR_KEY] + ", " + \
               self.legend[ADDITIONAL_INFO_DETECTOR_KEY] + "\n" + \
               LIGHT + \
               self.legend[TYPE_LIGHT_KEY] + ", " + \
               self.legend[NAME_LIGHT_KEY] + "\n" + \
               MEASUREMENT + \
               self.legend[DATE_KEY] + ", " + self.legend[TIME_KEY] + "\n" + \
               BEGIN_POSITION \
               + self.unit_type_grid_position + END_OF_POSITION_LABEL + \
               self.legend[START_POSITION_KEY] + "\n" + \
               END_POSITION \
               + self.unit_type_grid_position + END_OF_POSITION_LABEL \
               + self.legend[END_POSITION_KEY] + "\n" + \
               STEP_OF_MOTOR + \
               self.legend[STEP_OF_MOTOR_KEY] + "\n" + \
               NUMBER_OF_INTEGRATIONS + \
               self.legend[NUM_OF_INTEGRATIONS_KEY] + "\n" + \
               CORRECTION + \
               self.legend[CORRECTION_KEY] + "\n" + \
               MILIVOLTMETER + \
               self.legend[LOCK_IN_KEY] + "\n" + \
               SENSITIVITY + self.legend[TYPE_SENSITIVITY_KEY] + "\n" + \
               LOCK_IN_REFERENCE + self.legend[LOCK_IN_REFERENCE_KEY] + "\n" + \
               RANGE + self.legend[RANGE_KEY] + "\n" + \
               PHASE_SHIFT + self.legend[PHASE_SHIFT_KEY] + "\n" + \
               TIME_CONSTANT + self.legend[TIME_CONSTANT_KEY]

    def set_current_time(self):
        """
        set current time in self.legend if measurement setting doesnt already have time field
        """

        if TIME_KEY not in self.legend.keys():
            today = datetime.now()
            self.legend[TIME_KEY] = today.strftime("%H:%M:%S")

    def set_current_date(self):
        """
        set current date in self.legend if measurement setting doesnt already have date field
        """
        if DATE_KEY not in self.legend.keys():
            now = datetime.now()
            self.legend[DATE_KEY] = now.strftime('%d-%m-%Y')

    def load_string_legend(self, str_legend):
        """
        creates measurement setting object by loading fields of legend from a string
        representation of legend
        @param str_legend: string representation of legend
        @return: measurement setting object loaded from string
        @raise data_processing_error: raises an exception if string representation of legend
                                        isn't in right format or is missing some legend fields
        """
        str_legend = str_legend.replace(":\n", ": \n")
        lines_of_legend = str_legend.split("\n")

        alternative, setting_field = self.setting_fields_from_lines(lines_of_legend)
        old_settings = self.setting_fields_to_object_setting(alternative, setting_field)

        if not old_settings.check_completness_of_legend():
            raise data_processing_error("Legenda v načítanom súbore je v nespravnom formáte.")
        return old_settings

    def setting_fields_from_lines(self, lines_of_legend):
        """
        from list of lines of string representation of legend extracts exact values
        of the measurement setting which is being loaded
        @param lines_of_legend: list of lines of a string representation of a legend
        @return: unit_type - symbol of unit which is used to represent end and start position of grid,
                 setting_field - list of exact values of the measurement setting which is being loaded
        """
        unit_type = ANGLE_SYMBOL
        setting_field = []
        for i in range(len(lines_of_legend)):
            line = lines_of_legend[i]
            if "počiatočná" in line and WAVE_LENGTH_SYMBOL in line:
                unit_type = WAVE_LENGTH_SYMBOL
            if ": " in line:
                line = line.strip()
                line = line[line.index(":") + 2:]
            if len(line) > 0:
                setting_field.extend(line.split(", "))
        return unit_type, setting_field

    def setting_fields_to_object_setting(self, unit_type, setting_field):
        """
        creates measurement settings object from a list of exact values
        of the measurement setting which is being loaded and from symbol of
        unit which is used to represent end and start position of grid
        @param unit_type: symbol of unit which is used to represent end and start position of grid
        @param setting_field: list of exact values of the measurement setting which is being loaded
        @return: measurement settings object
        """
        old_settings = measurement_settings()
        old_settings.set_unit_type_position(unit_type)
        index_mandatory_keys = 0
        index_setting_fields = 0
        while index_setting_fields < len(setting_field):
            key = self.mandatory[index_mandatory_keys]
            value = setting_field[index_setting_fields]
            old_settings.set_setting_field(key, value)
            index_setting_fields += 1
            index_mandatory_keys += 1
            if key == self.KEY_BEFORE_ALTERNATIVES:
                value = setting_field[index_setting_fields]
                old_settings.set_setting_field(DATE_KEY, value)
                index_setting_fields += 1
                value = setting_field[index_setting_fields]
                old_settings.set_setting_field(TIME_KEY, value)
                index_setting_fields += 1
        return old_settings

    def load_last_json_legend(self):
        """
        loads measurement setting from the last time this system was used
        from json file stored in the app.
        """
        with open(self.json_name, 'r') as f:
            self.legend = json.load(f)
            if NAME_SAMPLE_KEY in self.legend.keys():
                del self.legend[NAME_SAMPLE_KEY]
            if TIME_KEY in self.legend.keys():
                del self.legend[TIME_KEY]
            if DATE_KEY in self.legend.keys():
                del self.legend[DATE_KEY]

    def store_last_json_legend(self):
        """
        stores measurement setting this system is currently using in json file in the app
        """
        with open(self.json_name, 'w') as f:
            json.dump(self.legend, f, indent=2)



