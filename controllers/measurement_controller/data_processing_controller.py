from PySide6 import QtWidgets
from PySide6.QtCore import QObject, Signal

from errors.data_processing_error import DataProcessingError
from models.data_processing.dataProcessing import DataProcessing
from models.data_processing.constants import *
from models.logger.constants import *


class DataProcessingController(QObject):
    settings_changed_s = Signal(dict)

    def __init__(self, view, key):
        '''
        initializes DataProcessingController
        @param view: reference to all widgets in the user interface
        @param key: secret key
        '''
        super(DataProcessingController, self).__init__()
        self._key = key
        self.data_processing = DataProcessing(view)
        self.view = view
        self.view.widgets.comparative_file_unload_btn.clicked.connect(self.clear_comparing_measurement)

        self.connect_formular()
        self.initialize_formular()

    def connect_formular(self):
        '''
        connects itself to each element in legend formular in the user interface, so it can
        automatically update stored legend of the measurement
        @return:
        '''

        self.view.widgets.saple_name_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(NAME_SAMPLE_KEY, self.view.widgets.saple_name_ledit.text()))

        self.view.widgets.sample_temperature_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(TEMPERATURE_KEY,
                                                          self.view.widgets.sample_temperature_ledit.text()))

        self.view.widgets.sample_width_dsbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(THICKNESS_KEY, self.view.widgets.sample_width_dsbox.value())
        )
        self.view.widgets.sample_note_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(NOTE_TO_TECH_KEY,
                                                          self.view.widgets.sample_note_ledit.text()))

        self.view.widgets.sample_measurement_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(MEASURE_OF_SAMPLE_KEY,
                                                          self.view.widgets.sample_measurement_ledit.text()))

        self.view.widgets.measurement_config_menu_filename_ledit.editingFinished.connect(
            lambda: self.data_processing.set_file_name(
                self.view.widgets.measurement_config_menu_filename_ledit.text()))
        self.view.widgets.measurement_config_menu_start_sbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(START_POSITION_KEY,
                                                          self.view.widgets.measurement_config_menu_start_sbox.value())
        )
        self.view.widgets.measurement_config_menu_end_sbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(END_POSITION_KEY,
                                                          self.view.widgets.measurement_config_menu_end_sbox.value())
        )
        self.view.widgets.measurement_integrations_sbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(NUM_OF_INTEGRATIONS_KEY,
                                                          self.view.widgets.measurement_integrations_sbox.value())
        )
        self.view.widgets.measurement_correction_sbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(CORRECTION_KEY,
                                                          self.view.widgets.measurement_correction_sbox.value())
        )
        self.view.widgets.measurement_motor_step.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(STEP_OF_MOTOR_KEY,
                                                          self.view.widgets.measurement_motor_step.value())
        )
        self.view.widgets.measurement_config_menu_ref_sbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(LOCK_IN_REFERENCE_KEY,
                                                          self.view.widgets.measurement_config_menu_ref_sbox.value())
        )
        self.view.widgets.measurement_config_menu_span_dsbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(RANGE_KEY,
                                                          self.view.widgets.measurement_config_menu_span_dsbox.value())
        )
        self.view.widgets.measurement_config_menu_span_auto_check.stateChanged.connect(
            self.set_auto_check_value)

        self.view.widgets.measurement_config_menu_time_const_dsbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(TIME_CONSTANT_KEY,
                                                          self.view.widgets.measurement_config_menu_time_const_dsbox.value())
        )
        self.view.widgets.measurement_config_menu_angle_sbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(PHASE_SHIFT_KEY,
                                                          self.view.widgets.measurement_config_menu_angle_sbox.value())
        )
        self.view.widgets.measurement_config_menu_laser_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(NAME_LIGHT_KEY,
                                                          self.view.widgets.measurement_config_menu_laser_ledit.text()))

        self.view.widgets.measurement_config_menu_halogen_cbox.currentIndexChanged.connect(
            lambda: self.data_processing.set_legend_field(TYPE_LIGHT_KEY,
                                                          self.view.widgets.measurement_config_menu_halogen_cbox.currentText()))
        self.view.widgets.detector_pmt_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(TYPE_OF_DETECTOR_KEY,
                                                          self.view.widgets.detector_pmt_ledit.text()))

        self.view.widgets.detector_voltage_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(ADDITIONAL_INFO_DETECTOR_KEY,
                                                          self.view.widgets.detector_voltage_ledit.text()))

        self.view.widgets.monochromator_in_in_start.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(INPUT_CREVICE_BEGIN_KEY,
                                                          self.view.widgets.monochromator_in_in_start.value())
        )
        self.view.widgets.monochromator_in_in_start_2.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(INPUT_CREVICE_END_KEY,
                                                          self.view.widgets.monochromator_in_in_start_2.value())
        )
        self.view.widgets.monochromator_out_out_start.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(OUTPUT_CREVICE_BEGIN_KEY,
                                                          self.view.widgets.monochromator_out_out_start.value())
        )
        # self.view.widgets.monochromator_out_in_start.valueChanged.connect(
        #     lambda: self.data_processing.set_legend_field(OUTPUT_CREVICE_END_KEY,
        #                                                   self.view.widgets.monochromator_out_in_start.value())
        # )
        self.view.widgets.monochromator_name_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(MONOCHROMATOR_NAME_KEY,
                                                          self.view.widgets.monochromator_name_ledit.text()))

        self.view.widgets.monochromator_optical_filter_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(OPTICAL_FILTER_KEY,
                                                          self.view.widgets.monochromator_optical_filter_ledit.text()))

        self.view.widgets.devices_controls_devices_selection_volt_cbox.currentIndexChanged.connect(
            lambda: self.data_processing.set_legend_field(LOCK_IN_KEY,
                                                          self.view.widgets.devices_controls_devices_selection_volt_cbox.currentText()))
        self.view.widgets.devices_controls_devices_selection_disperse_cbox.currentIndexChanged.connect(
            lambda: self.data_processing.set_legend_field(NAME_OF_DISPERS_ELEM_KEY,
                                                          self.view.widgets.devices_controls_devices_selection_disperse_cbox.currentText()))

        self.view.widgets.radioButton.toggled.connect(
            self.set_unit_type_angle)
        self.view.widgets.radioButton_2.toggled.connect(
            self.set_unit_type_angstrom)

    def initialize_formular(self):
        '''
        fills the legend formular in user interface with measurement settings used the last time
        the app was used
        @return:
        '''
        for key, value in self.data_processing.settings.legend.items():
            if key == NOTE_TO_TECH_KEY:
                self.view.widgets.sample_note_ledit.setText(self.data_processing.settings.legend[NOTE_TO_TECH_KEY])
            elif key == THICKNESS_KEY:
                self.view.widgets.sample_width_dsbox.setValue(
                    float(self.data_processing.settings.legend[THICKNESS_KEY]))
            elif key == MEASURE_OF_SAMPLE_KEY:
                self.view.widgets.sample_measurement_ledit.setText(
                    self.data_processing.settings.legend[MEASURE_OF_SAMPLE_KEY])
            elif key == TEMPERATURE_KEY:
                self.view.widgets.sample_temperature_ledit.setText(
                    self.data_processing.settings.legend[TEMPERATURE_KEY])
            elif key == NAME_OF_DISPERS_ELEM_KEY:
                index = self.view.widgets.devices_controls_devices_selection_disperse_cbox.findData(
                    self.data_processing.settings.legend[NAME_OF_DISPERS_ELEM_KEY])
                if index != -1:
                    self.view.widgets.devices_controls_devices_selection_disperse_cbox.setCurrentIndex(index)
            elif key == INPUT_CREVICE_BEGIN_KEY:
                self.view.widgets.monochromator_in_in_start.setValue(
                    float(self.data_processing.settings.legend[INPUT_CREVICE_BEGIN_KEY]))
            elif key == INPUT_CREVICE_END_KEY:
                self.view.widgets.monochromator_in_in_start_2.setValue(
                    float(self.data_processing.settings.legend[INPUT_CREVICE_END_KEY]))
            elif key == OUTPUT_CREVICE_BEGIN_KEY:
                self.view.widgets.monochromator_out_out_start.setValue(
                    float(self.data_processing.settings.legend[OUTPUT_CREVICE_BEGIN_KEY]))
            # elif key == OUTPUT_CREVICE_END_KEY:
            #     self.view.widgets.monochromator_out_in_start.setValue(
            #         float(self.data_processing.settings.legend[OUTPUT_CREVICE_END_KEY]))

            elif key == MONOCHROMATOR_NAME_KEY:
                self.view.widgets.monochromator_name_ledit.setText(
                    self.data_processing.settings.legend[MONOCHROMATOR_NAME_KEY])
            elif key == OPTICAL_FILTER_KEY:
                self.view.widgets.monochromator_optical_filter_ledit.setText(
                    self.data_processing.settings.legend[OPTICAL_FILTER_KEY])
            elif key == TYPE_OF_DETECTOR_KEY:
                self.view.widgets.detector_pmt_ledit.setText(
                    self.data_processing.settings.legend[TYPE_OF_DETECTOR_KEY])
            elif key == ADDITIONAL_INFO_DETECTOR_KEY:
                self.view.widgets.detector_voltage_ledit.setText(
                    self.data_processing.settings.legend[ADDITIONAL_INFO_DETECTOR_KEY])
            elif key == TYPE_LIGHT_KEY:
                index = self.view.widgets.measurement_config_menu_halogen_cbox.findData(
                    self.data_processing.settings.legend[TYPE_LIGHT_KEY])
                if index != -1:
                    self.view.widgets.measurement_config_menu_halogen_cbox.setCurrentIndex(index)
            elif key == NAME_LIGHT_KEY:
                self.view.widgets.measurement_config_menu_laser_ledit.setText(
                    self.data_processing.settings.legend[NAME_LIGHT_KEY])
            elif key == STEP_OF_MOTOR_KEY:
                self.view.widgets.measurement_motor_step.setValue(
                    float(self.data_processing.settings.legend[STEP_OF_MOTOR_KEY]))
            elif key == NUM_OF_INTEGRATIONS_KEY:
                self.view.widgets.measurement_integrations_sbox.setValue(
                    float(self.data_processing.settings.legend[NUM_OF_INTEGRATIONS_KEY]))
            elif key == CORRECTION_KEY:
                self.view.widgets.measurement_correction_sbox.setValue(
                    float(self.data_processing.settings.legend[CORRECTION_KEY]))
            elif key == LOCK_IN_KEY:
                index = self.view.widgets.devices_controls_devices_selection_volt_cbox.findData(
                    self.data_processing.settings.legend[LOCK_IN_KEY])
                if index != -1:
                    self.view.widgets.devices_controls_devices_selection_volt_cbox.setCurrentIndex(index)
            elif key == TYPE_SENSITIVITY_KEY:
                if self.data_processing.settings.legend[TYPE_SENSITIVITY_KEY] == AUTO:
                    self.view.widgets.measurement_config_menu_span_auto_check.setChecked(True)
                else:
                    self.view.widgets.measurement_config_menu_span_auto_check.setChecked(False)
            elif key == LOCK_IN_REFERENCE_KEY:
                self.view.widgets.measurement_config_menu_ref_sbox.setValue(
                    float(self.data_processing.settings.legend[LOCK_IN_REFERENCE_KEY]))
            elif key == RANGE_KEY:
                self.view.widgets.measurement_config_menu_span_dsbox.setValue(
                    float(self.data_processing.settings.legend[RANGE_KEY]))
            elif key == PHASE_SHIFT_KEY:
                self.view.widgets.measurement_config_menu_angle_sbox.setValue(
                    float(self.data_processing.settings.legend[PHASE_SHIFT_KEY]))
            elif key == TIME_CONSTANT_KEY:
                self.view.widgets.measurement_config_menu_time_const_dsbox.setValue(
                    float(self.data_processing.settings.legend[TIME_CONSTANT_KEY]))
            elif key == START_POSITION_KEY:
                self.view.widgets.measurement_config_menu_start_sbox.setValue(
                    float(self.data_processing.settings.legend[START_POSITION_KEY]))
            elif key == END_POSITION_KEY:
                self.view.widgets.measurement_config_menu_end_sbox.setValue(
                    float(self.data_processing.settings.legend[END_POSITION_KEY]))

        if self.data_processing.settings.legend[UNIT] == Unit.Uhol:
            self.view.widgets.radioButton.click()
        elif self.data_processing.settings.legend[UNIT] == Unit.Angstrom:
            self.view.widgets.radioButton_2.click()

    def add_logger(self, logger):
        '''
        stores reference to logger
        @param logger: reference to logger
        @return:
        '''
        self.logger = logger

    def get_file_name(self):
        '''
        getter of filename of the current measurement file
        @return: filename of the current measurement file
        '''
        return self.data_processing.file_name

    def clear_comparing_measurement(self):
        '''
        deletes data of compared old measurement from the graph and
        its measurement legend from the textBrowser
        @return:
        '''
        self.view.widgets.graph_view.addMeasurement([], False)
        self.view.widgets.graph_view.plotGraph()
        self.view.widgets.textBrowser.clear()

    def set_auto_check_value(self):
        '''
        stores the type of the sensitivity based on whether the elements displaying
        type of sensitivity is checked or not
        @return:
        '''
        try:
            if self.view.widgets.measurement_config_menu_span_auto_check.isChecked():
                self.data_processing.set_legend_field(TYPE_SENSITIVITY_KEY, AUTO)
            else:
                self.data_processing.set_legend_field(TYPE_SENSITIVITY_KEY, MANUAL)
        except DataProcessingError as e:
            self.logger.log(WARNING, e.message, True)

    def set_unit_type_angle(self):
        '''
        stores that the angle unit is used in measurement based on whether its
        radio button is checked
        @return:
        '''
        if self.view.widgets.radioButton.isChecked():
            try:
                self.data_processing.set_unit_type_position(Unit.Uhol)
            except DataProcessingError as e:
                self.logger.log(WARNING, e.message, True)
        self.data_processing.settings.store_last_json_legend()

    def set_unit_type_angstrom(self):
        '''
        stores that the angstrom unit is used in measurement based on whether its
        radio button is checked
        @return:
        '''
        if self.view.widgets.radioButton_2.isChecked():
            try:
                self.data_processing.set_unit_type_position(Unit.Angstrom)
            except DataProcessingError as e:
                self.logger.log(WARNING, e.message, True)

    def save_as(self, name):
        '''
        saves currently stored contents of a measurement file as a copy in a new location
        chosen by the user
        @param name: name of the new copy of the measurement file
        @return:
        '''
        try:
            if not self.data_processing.settings.check_completness_of_legend():
                raise DataProcessingError("Legenda nie je kompletne vyplnená. Nie je možne vytvoriť nový súbor pre meranie.")
        except DataProcessingError as e:
            self.logger.log(WARNING, e.message, True)
            return

        try:
            name = self.copy_of_current_file(name)
        except FileNotFoundError:
            self.save_legend_to_file(name)

    def save_legend_to_file(self, name):
        '''
        saves legend of a measurement file as a copy in a new location
        chosen by the user (if user haven't yet started measurment and stored measurement file)
        @param name: name of the new copy of the measurement file
        @return:
        '''
        path = "\\".join(name.split("/")[:-1])
        file_name = name.split("/")[-1:][0].replace(".txt", "")
        old_path = self.data_processing.path
        old_postfix = self.data_processing.postfix
        old_filename = self.data_processing.file_name.replace(old_postfix + ".txt", ".txt")
        self.data_processing.set_file_name(file_name)
        self.data_processing.set_file_path(path)
        try:
            self.data_processing.create_new_file()
        except DataProcessingError as e:
            self.logger.log(WARNING, e.message, True)
        self.data_processing.set_file_name(old_filename)
        self.data_processing.set_file_path(old_path)
        self.data_processing.set_postfix(old_postfix)
        self.view.widgets.measurement_config_menu_filename_ledit.setText(old_filename.replace(".txt", ""))

    def copy_of_current_file(self, name):
        '''
        saves currently stored contents of a measurement file as a copy in a new location
        chosen by the user
        @param name: name of the new copy of the measurement file
        @return:
        '''
        with open(self.data_processing.path + self.data_processing.file_name, 'r', encoding="utf-8") as current_file:
            text = current_file.read()
            if name[-4:] != ".txt":
                name += ".txt"
            with open(name, 'w', encoding="utf-8") as copy_file:
                copy_file.write(text)
        return name

    def get_model(self, key):
        '''
        returns model
        @param key: secret key
        @return: model
        @raise ValueError: when the key is invalid
        '''
        if key == self._key:
            return self.data_processing
        else:
            raise ValueError("Invalid key")

