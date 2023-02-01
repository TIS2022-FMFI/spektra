from enum import Enum

END_POSITION_KEY = "endPosition"
START_POSITION_KEY = "startPosition"
TIME_KEY = "time"
DATE_KEY = "date"
TIME_CONSTANT_KEY = "timeConstante"
PHASE_SHIFT_KEY = "phaseShift"
RANGE_KEY = "range"
LOCK_IN_REFERENCE_KEY = "lockInReference"
TYPE_SENSITIVITY_KEY = "typeSensitivity"
LOCK_IN_KEY = "lockIn"
CORRECTION_KEY = "correction"
NUM_OF_INTEGRATIONS_KEY = "numberOfIntegrations"
STEP_OF_MOTOR_KEY = "stepOfMotor"
NAME_LIGHT_KEY = "nameOfLight"
TYPE_LIGHT_KEY = "typeOfLight"
ADDITIONAL_INFO_DETECTOR_KEY = "additionalInfoDetector"
TYPE_OF_DETECTOR_KEY = "typeOfDetector"
OPTICAL_FILTER_KEY = "opticalFilter"
# OUTPUT_CREVICE_END_KEY = "outputCreviceEnd"
OUTPUT_CREVICE_BEGIN_KEY = "outputCreviceBegin"
INPUT_CREVICE_END_KEY = "inputCreviceEnd"
INPUT_CREVICE_BEGIN_KEY = "inputCreviceBegin"
NAME_OF_DISPERS_ELEM_KEY = "nameOfDispersingElement"
TYPE_OF_DISPERS_ELEM_KEY = "typeOfDispersingElement"
TEMPERATURE_KEY = "temperature"
MEASURE_OF_SAMPLE_KEY = "measurementOfSample"
THICKNESS_KEY = "thickness"
NOTE_TO_TECH_KEY = "noteToTech"
NAME_SAMPLE_KEY = "nameSample"
MONOCHROMATOR_NAME_KEY = "monochromatorNameKey"
UNIT = "unit"

SAMPLE = "VZORKA"
DISPERSE_ELEMENT = "DISPERZNÝ ELEMENT"
MONOCHROMATOR = "MONOCHROMÁTOR"
DETECTOR = "DETEKTOR"
LIGHT = "BÚDIACE SVETLO"
MEASUREMENT = "MERANIE"
MILIVOLTMETER = "MILIVOLTMENTER"
NAME_SAMPLE = "názov vzorky"
NOTE_TO_TECH = "poznámka k technológií"
THICKNESS = "hrúbka"
MEASUREMENT_OF_SAMPLE = "meranie vzorky"
TEMPERATURE = "teplota"
INPUT_CREVICE = "vstupná štrbina (šírka, výška)"
OUTPUT_CREVICE = "výstupná štrbina (šírka)"
OPTICAL_FILTER = "optický filter"
TYPE_OF_DETECTOR = "PMT"
STEP_OF_MOTOR = "krok motora [v impulzoch]"
NUMBER_OF_INTEGRATIONS = "počet integrácií"
CORRECTION = "korekcia [A°]"
SENSITIVITY = "citlivosť"
LOCK_IN_REFERENCE = "referencia [Hz]"
RANGE = "range"
PHASE_SHIFT = "fázový posun"
TIME_CONSTANT = "časová konštanta"
END_OF_POSITION_LABEL = "]"
END_POSITION = "koncová ["
BEGIN_POSITION = "počiatočná ["
MONOCHROMATOR_NAME = "názov"


SAVED_MEASUREMENTS_DIR_NAME = "\\saved_measurements\\"
ROOT_DIR_NAME = "spektra"
INTENSITY_COLLUMN = "INTENZITA[mV]"
WAVE_LENGTH_COLLUMN = "VLNOVÁ DĹŽKA[A]"
ALFA_COLLUMN = "ALFA[A°]"
AUTO = "AUTO"
MANUAL = "manuálne"
GRID = "mriežka"
DEFAULT_LEGEND_FILENAME = "lastSettings.txt"


mandatory = [NAME_SAMPLE_KEY, NOTE_TO_TECH_KEY, THICKNESS_KEY,
                 MEASURE_OF_SAMPLE_KEY, TEMPERATURE_KEY,
                 TYPE_OF_DISPERS_ELEM_KEY, NAME_OF_DISPERS_ELEM_KEY,
                 MONOCHROMATOR_NAME_KEY,
                 INPUT_CREVICE_BEGIN_KEY, INPUT_CREVICE_END_KEY,
                 OUTPUT_CREVICE_BEGIN_KEY, #OUTPUT_CREVICE_END_KEY,
                 OPTICAL_FILTER_KEY, TYPE_OF_DETECTOR_KEY,
                 ADDITIONAL_INFO_DETECTOR_KEY,
                 TYPE_LIGHT_KEY, NAME_LIGHT_KEY,
                 START_POSITION_KEY, END_POSITION_KEY,
                 STEP_OF_MOTOR_KEY, NUM_OF_INTEGRATIONS_KEY,
                 CORRECTION_KEY, LOCK_IN_KEY, TYPE_SENSITIVITY_KEY,
                 LOCK_IN_REFERENCE_KEY,
                 RANGE_KEY, PHASE_SHIFT_KEY, TIME_CONSTANT_KEY,
                 ]
non_mandatory = [DATE_KEY, TIME_KEY, UNIT]

class Unit(Enum):
     Uhol = "°"
     Angstrom = "A°"