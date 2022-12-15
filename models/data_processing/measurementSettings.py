import json
from datetime import datetime
import os
from errors.data_processing_error import DataProcessingError
from models.data_processing.Constants import *

class measurementSettings:
    mandatory = [NAME_SAMPLE_KEY, NOTE_TO_TECH_KEY, THICKNESS_KEY,
                 MEASURE_OF_SAMPLE_KEY, TEMPERATURE_KEY,
                 TYPE_OF_DISPERS_ELEM_KEY, NAME_OF_DISPERS_ELEM_KEY,
                 INPUT_CREVICE_BEGIN_KEY, INPUT_CREVICE_END_KEY,
                 OUTPUT_CREVICE_BEGIN_KEY, OUTPUT_CREVICE_END_KEY,
                 OPTICAL_FILTER_KEY, TYPE_OF_DETECTOR_KEY,
                 ADDITIONAL_INFO_DETECTOR_KEY,
                 TYPE_LIGHT_KEY, NAME_LIGHT_KEY,
                 STEP_OF_MOTOR_KEY, NUM_OF_INTEGRATIONS,
                 CORRECTION_KEY, LOCK_IN_KEY, TYPE_SENSITIVITY_KEY,
                 LOCK_IN_REFERENCE_KEY,
                 RANGE_KEY, PHASE_SHIFT_KEY, TIME_CONSTANT_KEY,
                 ]
    nonMandatory = [DATE_KEY, TIME_KEY]
    KEY_BEFORE_ALTERNATIVES = NAME_LIGHT_KEY
    ANGLE_INDEX = 0
    ANGSTROM_INDEX = 1
    SYMBOLS = [ANGLE_SYMBOL, WAVE_LENGTH_SYMBOL]
    alternatives = [(START_ANGLE_KEY, END_ANGLE_KEY),
                    (START_ANGSTROM_KEY, END_ANGSTROM_KEY)]


    def __init__(self):
        self.legend = dict()
        self.setSetting(TYPE_OF_DISPERS_ELEM_KEY, "mriežka")
        self.setSetting(TYPE_SENSITIVITY_KEY, "AUTO")

        script_dir = os.path.dirname(__file__)
        rel_path = "lastSettings.txt"
        self.jsonName = os.path.join(script_dir, rel_path)



    def setSetting(self, key, param):
        all = self.mandatory + [key for alter in self.alternatives
                                for key in alter] + self.nonMandatory
        if key in all:
            self.legend[key] = str(param)
            return True
        return False


    def checkLegend(self):
        for legendType in self.mandatory:
            if legendType not in self.legend.keys():
                return False
        for alt in self.alternatives:
            if all(map(lambda key : key in self.legend.keys(), alt)):
                return True
        return False


    def __str__(self):
        alternativeIndex = self.ANGSTROM_INDEX
        if START_ANGLE_KEY in self.legend.keys():
            alternativeIndex = self.ANGLE_INDEX

        dateCurrent = self.setCurrentDate()
        timeCurrent = self.setCurrentTime()

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
               dateCurrent + ", " + timeCurrent + "\n" + \
               BEGIN_POSITION \
               + self.SYMBOLS[alternativeIndex] + END_OF_POSITION_LABEL + \
               self.legend[self.alternatives[alternativeIndex][0]] + "\n" + \
               END_POSITION \
               + self.SYMBOLS[alternativeIndex] + END_OF_POSITION_LABEL \
               + self.legend[self.alternatives[alternativeIndex][1]] + "\n" + \
               STEP_OF_MOTOR + \
               self.legend[STEP_OF_MOTOR_KEY] + "\n" + \
               NUMBER_OF_INTEGRATIONS + \
               self.legend[NUM_OF_INTEGRATIONS] + "\n" + \
               CORRECTION + \
               self.legend[CORRECTION_KEY] + "\n" + \
               MILIVOLTMETER + \
               self.legend[LOCK_IN_KEY] + "\n" + \
               SENSITIVITY + self.legend[TYPE_SENSITIVITY_KEY] + "\n" + \
               LOCK_IN_REFERENCE + self.legend[LOCK_IN_REFERENCE_KEY] + "\n" + \
               RANGE + self.legend[RANGE_KEY] + "\n" + \
               PHASE_SHIFT + self.legend[PHASE_SHIFT_KEY] + "\n" + \
               TIME_CONSTANT + self.legend[TIME_CONSTANT_KEY]

    def setCurrentTime(self):
        today = datetime.now()
        timeCurrent = today.strftime("%H:%M:%S")
        if TIME_KEY in self.legend.keys():
            timeCurrent = self.legend[TIME_KEY]
        return timeCurrent

    def setCurrentDate(self):
        now = datetime.now()
        dateCurrent = now.strftime('%d-%m-%Y')
        if DATE_KEY in self.legend.keys():
            dateCurrent = self.legend[DATE_KEY]
        return dateCurrent

    def loadStringLegend(self, strLegend):
        strLegend = strLegend.replace(":\n", ": \n")
        linesOfLegend = strLegend.split("\n")

        alternative, settingField = self.settingFieldsFromLines(linesOfLegend)
        oldSettings = self.settingFieldsToMeasurSetting(alternative, settingField)

        if not oldSettings.checkLegend():
            raise DataProcessingError("Legenda v načítanom súbore je v nespravnom formáte.")
        return oldSettings

    def settingFieldsFromLines(self, linesOfLegend):
        alternative = self.ANGLE_INDEX
        settingField = []
        for i in range(len(linesOfLegend)):
            line = linesOfLegend[i]
            if "počiatočná" in line and WAVE_LENGTH_SYMBOL in line:
                alternative = self.ANGSTROM_INDEX
            if ": " in line:
                line = line.strip()
                line = line[line.index(":") + 2:]
            if len(line) > 0:
                settingField.extend(line.split(", "))
        return alternative, settingField

    def settingFieldsToMeasurSetting(self, alternative, settingField):
        oldSettings = measurementSettings()
        iMandatory = 0
        iSettings = 0
        while iSettings < len(settingField):
            key = self.mandatory[iMandatory]
            value = settingField[iSettings]
            oldSettings.setSetting(key, value)
            iSettings += 1
            iMandatory += 1
            if key == self.KEY_BEFORE_ALTERNATIVES:
                value = settingField[iSettings]
                oldSettings.setSetting(DATE_KEY, value)
                iSettings += 1
                value = settingField[iSettings]
                oldSettings.setSetting(TIME_KEY, value)
                iSettings += 1
                key = self.alternatives[alternative][0]
                value = settingField[iSettings]
                oldSettings.setSetting(key, value)
                iSettings += 1
                key = self.alternatives[alternative][1]
                value = settingField[iSettings]
                oldSettings.setSetting(key, value)
                iSettings += 1
        return oldSettings

    def loadLastJsonLegend(self):
        with open(self.jsonName, 'r') as f:
            self.legend = json.load(f)
            if NAME_SAMPLE_KEY in self.legend.keys():
                del self.legend[NAME_SAMPLE_KEY]

    def storeLastJsonLegend(self):
        with open(self.jsonName, 'w') as f:
            json.dump(self.legend, f, indent=2)



