
from PySide6.QtCore import QObject
from models.data_processing.constants import *
from models.data_processing.measurementSettings import MeasurementSettings
from errors.data_processing_error import DataProcessingError
import os

class DataProcessing(QObject):

    def __init__(self):
        super(DataProcessing, self).__init__()
        self.file_name = ""
        self.path = self.get_default_path()
        self.begining_of_data = '{: <20s}\t{: <20s}\t{}\n'.format(ALFA_COLLUMN, WAVE_LENGTH_COLLUMN, INTENSITY_COLLUMN)
        self.settings = MeasurementSettings()
        self.settings.load_last_json_legend()

    def get_default_path(self):
        """
        finds out current path to "saved_measurements" directory
        @return: path to "saved_measurements" directory
        """
        path = os.path.dirname(os.path.abspath(__file__))
        dirs = path.split("\\")
        root_name = ROOT_DIR_NAME
        target_dir = SAVED_MEASUREMENTS_DIR_NAME
        index_root = len(dirs) - dirs[::-1].index(root_name) - 1
        return "\\".join(dirs[:index_root + 1]) + target_dir

    def set_legend_field(self, key, value):
        """
        inserts value under key in self.setting.

        @param key: key under which will be value stored in self.setting
        @param value: value which is an input from user to the measurement settings
        @raise data_processing_error: raises an exception when trying to insert value under not
                                        allowed key
        """
        self.settings.set_setting_field(key, value)
        print(key, value)

    def set_unit_type_position(self, unit_type):
        """
        sets which unit (A°/°) is used as start and end position
        of measurement

        @param unit_type: symbol of used unit for position, only ANGLE_SYMBOL and
                                    WAVE_LENGTH_SYMBOL are allowed as input
        @raise data_processing_error: raises an exception if unit_type_position is not one of
                                        two allowed values
        """
        self.settings.set_unit_type_position(unit_type)
        print(self.settings.unit_type_grid_position)

    def create_new_file(self):
        """
        Checks if measurement setting in self.setting is complete. If it is
        creates new file and writes legend to the file. At last stores current
        measurement setting to the json legend file.
        @raise data_processing_error: raises an exception if legend isn't complete or it's not
                                        possible to create new file
        """
        if not self.settings.check_completness_of_legend():
            raise DataProcessingError("Legenda nie je kompletne vyplnená. Nie je možne vytvoriť nový súbor pre meranie.")

        self.write_legend()
        self.settings.store_last_json_legend()

    def add_measurement(self, angle, wave_length, intensity):
        """
        Writes one line with the latest measured data at the end of the
        current file
        @param angle: current angle of rotation of grid
        @param wave_length: current wavelength
        @param intensity: intensity measured in lockin
        @raise data_processing_error: raises an exception if there was no name of the
                                    measurement file provided
        """
        if self.file_name == "":
            raise DataProcessingError("Nie je vyplnené meno súboru. Nie je možné pridať najnovšie meranie do súboru.")
        with open(self.path + self.file_name, 'a', encoding="utf-8") as current_file:
            line = '\n{: <20s}\t{: <20s}\t{}'.format(str(angle), str(wave_length), str(intensity))
            current_file.write(line)

    def write_legend(self):
        """
        creates new file and writes string representation of the measurement settings in it.
        @raise data_processing_error: raises an exception if there was no name of the
                                    measurement file provided
        """
        if self.file_name == "":
            raise DataProcessingError("Nie je vyplnené meno súboru. Nie je možné vytvoriť nový súbor pre meranie.")

        with open(self.path + self.file_name, 'w', encoding="utf-8") as current_file:
            current_file.write(str(self.settings) + "\n\n")
            current_file.write(self.begining_of_data)

    def set_file_name(self, file_name):
        """
        sets name of file of a current measurement and adds .txt at the end if needed
        @param file_name: name of a file
        """
        if file_name[-4:] != ".txt":
            file_name += ".txt"
        self.file_name = file_name
        print(self.file_name)

    def set_file_path(self, path):
        """
        sets path of file of a current measurement and adds \\ at the end if needed
        @param path: path of a file
        """
        if path[-1:] != "\\":
            path += "\\"
        self.path = path

    def load_old_file(self, file_name):
        """
        loads file of old measurement and reads sets of measurement data and legend
        @param file_name: name of file required to be loaded
        @return: measurement setting object loaded from file and a list of measurement data
        @raise data_processing_error: raises an exception if file is in wrong format (no data,
                                        wrong format of data, no legend or wromg format of the legend)
        """
        with open(file_name, 'r', encoding="utf-8") as f:
            string_legend = self.read_legend_from_file(f)
            loaded_settings = self.settings.load_string_legend(string_legend)
            measurements = self.read_measurements_from_file(f)

        if measurements == []:
            raise DataProcessingError("Načítaný súbor nie je v správnom formáte. Neobsahuje nameraná údaje.")

        return loaded_settings, measurements

    def read_measurements_from_file(self, file):
        """
        loads and reads list of measured data from file
        @param file: name of file required to be loaded
        @return: a list of measured data
        @raise data_processing_error: raises an exception if file is in wrong format (no data,
                                        wrong format of data)
        """
        measurement_line = file.readline()
        while measurement_line == "\n":
            measurement_line = file.readline()

        measurements = []

        while measurement_line != '':
            try:
                alfa, wave_length, intensity = measurement_line.split("\t")
                wave_length = wave_length.replace(" ", "")
                intensity = intensity.replace(" ", "")
                measurements.append([float(wave_length),
                                     float(intensity)])
                measurement_line = file.readline()
            except:
                raise DataProcessingError("Načítaný súbor nie je v správnom formáte. Namerané údaje sú v zlom formáte.")

        return measurements

    def read_legend_from_file(self, file):
        """
        reads legend from file
        @param file: name of file required to be loaded
        @return: string of legend loaded from file
        @raise data_processing_error: raises an exception if the file is in a wrong format (no legend, no data)
        """
        line = file.readline()
        string_legend = ""
        while line != '' and line != self.begining_of_data:
            string_legend += line + "\n"
            line = file.readline()

        if line == '':
            raise DataProcessingError("Načítaný súbor nie je v správnom formáte. Neobsahuje nameraná údaje.")

        return string_legend

