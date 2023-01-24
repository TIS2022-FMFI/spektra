import json
from datetime import datetime
import os
from errors.data_processing_error import DataProcessingError
from models.data_processing.constants import *


class MeasurementSettings:
    KEY_BEFORE_ALTERNATIVES = NAME_LIGHT_KEY

    def __init__(self):
        '''
        initializes measurementSettings
        '''
        self.legend = dict()
        self.all_setting_key = set(mandatory + non_mandatory)
        self.set_setting_field(TYPE_OF_DISPERS_ELEM_KEY, GRID)
        self.set_setting_field(TYPE_SENSITIVITY_KEY, AUTO)
        self.set_unit_type_position(Unit.Angstrom)

        script_dir = os.path.dirname(__file__)
        rel_path = DEFAULT_LEGEND_FILENAME
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
        if not isinstance(unit_type_position, Unit):
            raise DataProcessingError("Do legendy je vkladaná nesprávna jednotka počiatočnej/koncovej pozície merania.")
        self.legend[UNIT] = unit_type_position

    def set_setting_field(self, key, value):
        """
        inserts value under key in self.legend. Inserts only values,
        under one of the allowed keys

        @param key: key under which will be value stored in self.legend
        @param value: value which is an input from user to the legend of a measurement
        @raise data_processing_error: raises an exception when trying to insert value under not
                                        allowed key
        """
        if key in self.all_setting_key:
            self.legend[key] = str(value)
            return

        raise DataProcessingError("Do legendy je vkladaná neexistujúca položka (zly key).")


    def check_completness_of_legend(self):
        """
        check if the legend contains all mandatory fields needed
        to work with legend
        @return: boolean value based on whether self.legend contains all
                mandatory fields of measurement settings
        """
        for legend_type in mandatory:
            if legend_type not in self.legend:
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

        return f"{SAMPLE}:\n" \
               f"{NAME_SAMPLE}: {self.legend[NAME_SAMPLE_KEY]}\n" \
               f"{NOTE_TO_TECH}: {self.legend[NOTE_TO_TECH_KEY]}\n" \
               f"{THICKNESS}: {self.legend[THICKNESS_KEY]}\n" \
               f"{MEASUREMENT_OF_SAMPLE}: {self.legend[MEASURE_OF_SAMPLE_KEY]}\n" \
               f"{TEMPERATURE}: {self.legend[TEMPERATURE_KEY]}\n" \
               f"{DISPERSE_ELEMENT}:\n" \
               f"{self.legend[TYPE_OF_DISPERS_ELEM_KEY]}, {self.legend[NAME_OF_DISPERS_ELEM_KEY]}\n" \
               f"{MONOCHROMATOR}:\n" \
               f"{INPUT_CREVICE}: {self.legend[INPUT_CREVICE_BEGIN_KEY]}, {self.legend[INPUT_CREVICE_END_KEY]}\n" \
               f"{OUTPUT_CREVICE}: {self.legend[OUTPUT_CREVICE_BEGIN_KEY]}, {self.legend[OUTPUT_CREVICE_END_KEY]}\n" \
               f"{OPTICAL_FILTER}: {self.legend[OPTICAL_FILTER_KEY]}\n" \
               f"{DETECTOR}:\n" \
               f"{TYPE_OF_DETECTOR}: {self.legend[TYPE_OF_DETECTOR_KEY]}, {self.legend[ADDITIONAL_INFO_DETECTOR_KEY]}\n" \
               f"{LIGHT}:\n" \
               f"{self.legend[TYPE_LIGHT_KEY]}, {self.legend[NAME_LIGHT_KEY]}\n" \
               f"{MEASUREMENT}:\n" \
               f"{self.legend[DATE_KEY]}, {self.legend[TIME_KEY]}\n" \
               f"{BEGIN_POSITION}{self.legend[UNIT].value}{END_OF_POSITION_LABEL}: {self.legend[START_POSITION_KEY]}\n" \
               f"{END_POSITION}{self.legend[UNIT].value}{END_OF_POSITION_LABEL}: {self.legend[END_POSITION_KEY]}\n" \
               f"{STEP_OF_MOTOR}: {self.legend[STEP_OF_MOTOR_KEY]}\n" \
               f"{NUMBER_OF_INTEGRATIONS}: {self.legend[NUM_OF_INTEGRATIONS_KEY]}\n" \
               f"{CORRECTION}: {self.legend[CORRECTION_KEY]}\n" \
               f"{MILIVOLTMETER}:\n" \
               f"{self.legend[LOCK_IN_KEY]}\n" \
               f"{SENSITIVITY}: {self.legend[TYPE_SENSITIVITY_KEY]}\n" \
               f"{LOCK_IN_REFERENCE}: {self.legend[LOCK_IN_REFERENCE_KEY]}\n" \
               f"{RANGE}: {self.legend[RANGE_KEY]}\n" \
               f"{PHASE_SHIFT}: {self.legend[PHASE_SHIFT_KEY]}\n" \
               f"{TIME_CONSTANT}: {self.legend[TIME_CONSTANT_KEY]}"

    def set_current_time(self):
        """
        set current time in self.legend if measurement setting doesnt already have time field
        """

        if TIME_KEY not in self.legend:
            today = datetime.now()
            self.legend[TIME_KEY] = today.strftime("%H:%M:%S")

    def set_current_date(self):
        """
        set current date in self.legend if measurement setting doesnt already have date field
        """
        if DATE_KEY not in self.legend:
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
            raise DataProcessingError("Legenda v načítanom súbore je v nespravnom formáte.")
        return old_settings

    def setting_fields_from_lines(self, lines_of_legend):
        """
        from list of lines of string representation of legend extracts exact values
        of the measurement setting which is being loaded
        @param lines_of_legend: list of lines of a string representation of a legend
        @return: unit_type - symbol of unit which is used to represent end and start position of grid,
                 setting_field - list of exact values of the measurement setting which is being loaded
        """
        unit_type = Unit.Uhol
        setting_field = []
        for i in range(len(lines_of_legend)):
            line = lines_of_legend[i]
            if "počiatočná" in line and Unit.Angstrom.value in line:
                unit_type = Unit.Angstrom
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
        old_settings = MeasurementSettings()
        old_settings.set_unit_type_position(unit_type)
        index_mandatory_keys = 0
        index_setting_fields = 0
        while index_setting_fields < len(setting_field):
            key = mandatory[index_mandatory_keys]
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
        try:
            with open(self.json_name, 'r') as f:
                self.legend = json.load(f)
                if NAME_SAMPLE_KEY in self.legend:
                    del self.legend[NAME_SAMPLE_KEY]
                if TIME_KEY in self.legend:
                    del self.legend[TIME_KEY]
                if DATE_KEY in self.legend:
                    del self.legend[DATE_KEY]
                if UNIT not in self.legend:
                    self.set_unit_type_position(Unit.Angstrom)
                else:
                    if self.legend[UNIT] == Unit.Angstrom.value:
                        self.set_unit_type_position(Unit.Angstrom)
                    elif self.legend[UNIT] == Unit.Uhol.value:
                        self.set_unit_type_position(Unit.Uhol)
        except FileNotFoundError:
            pass


    def store_last_json_legend(self):
        """
        stores measurement setting this system is currently using in json file in the app
        """

        if self.legend[UNIT] == Unit.Angstrom:
            self.set_setting_field(UNIT, Unit.Angstrom.value)
        elif self.legend[UNIT] == Unit.Uhol:
            self.set_setting_field(UNIT, Unit.Uhol.value)

        try:
            with open(self.json_name, 'w') as f:
                json.dump(self.legend, f, indent=2)
        except FileNotFoundError:
            pass

        if self.legend[UNIT] == Unit.Angstrom.value:
            self.set_unit_type_position(Unit.Angstrom)
        elif self.legend[UNIT] == Unit.Uhol.value:
            self.set_unit_type_position(Unit.Uhol)



