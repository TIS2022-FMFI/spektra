from PySide6.QtCore import QObject, Signal

from models.data_processing.dataProcessing import DataProcessing
from models.data_processing.constants import *

class DataProcessingController(QObject):
    settings_changed_s = Signal(dict)

    def __init__(self, view):
        super(DataProcessingController, self).__init__()
        self._data_processing = DataProcessing()
        self.view = view

        self.data_processing = DataProcessing()

        self.view.widgets.saple_name_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(NAME_SAMPLE_KEY, self.view.widgets.saple_name_ledit.text()))

        self.view.widgets.sample_temperature_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(TEMPERATURE_KEY,
                                                          self.view.widgets.sample_temperature_ledit.text()))

        # sample_width_dsbox - QDoubleSpinBox
        self.view.widgets.sample_width_dsbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(THICKNESS_KEY, self.view.widgets.sample_width_dsbox.value())
        )
        # sample_note_ledit = QLineEdit
        self.view.widgets.sample_note_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(NOTE_TO_TECH_KEY, self.view.widgets.sample_note_ledit.text()))

        # sample_measurement_ledit = QLineEdit
        self.view.widgets.sample_measurement_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(MEASURE_OF_SAMPLE_KEY,
                                                          self.view.widgets.sample_measurement_ledit.text()))

        # measurement_config_menu_filename_ledit = QLineEdit
        self.view.widgets.measurement_config_menu_filename_ledit.editingFinished.connect(
            lambda: self.data_processing.set_file_name(self.view.widgets.measurement_config_menu_filename_ledit.text()))

        # measurement_config_menu_end_sbox = QDoubleSpinBox
        self.view.widgets.measurement_config_menu_end_sbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(START_POSITION_KEY,
                                                          self.view.widgets.measurement_config_menu_end_sbox.value())
        )
        # .measurement_config_menu_start_sbox = QDoubleSpinBox
        self.view.widgets.measurement_config_menu_start_sbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(END_POSITION_KEY,
                                                          self.view.widgets.measurement_config_menu_start_sbox.value())
        )
        # measurement_integrations_sbox = QSpinBox
        self.view.widgets.measurement_integrations_sbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(NUM_OF_INTEGRATIONS_KEY,
                                                          self.view.widgets.measurement_integrations_sbox.value())
        )
        # measurement_correction_sbox = QDoubleSpinBox
        self.view.widgets.measurement_correction_sbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(CORRECTION_KEY,
                                                          self.view.widgets.measurement_correction_sbox.value())
        )
        # measurement_motor_step = QSpinBox
        self.view.widgets.measurement_motor_step.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(STEP_OF_MOTOR_KEY,
                                                          self.view.widgets.measurement_motor_step.value())
        )
        # measurement_config_menu_ref_sbox = QSpinBox
        self.view.widgets.measurement_config_menu_ref_sbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(LOCK_IN_REFERENCE_KEY,
                                                          self.view.widgets.measurement_config_menu_ref_sbox.value())
        )
        # measurement_config_menu_span_dsbox = QDoubleSpinBox
        self.view.widgets.measurement_config_menu_span_dsbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(RANGE_KEY,
                                                          self.view.widgets.measurement_config_menu_span_dsbox.value())
        )
        # measurement_config_menu_span_auto_check = QCheckBox
        self.view.widgets.measurement_config_menu_span_auto_check.stateChanged.connect(
            self.set_auto_check_value)

        # measurement_config_menu_time_const_dsbox = QDoubleSpinBox
        self.view.widgets.measurement_config_menu_time_const_dsbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(TIME_CONSTANT_KEY,
                                                          self.view.widgets.measurement_config_menu_time_const_dsbox.value())
        )
        # measurement_config_menu_angle_sbox = QSpinBox
        self.view.widgets.measurement_config_menu_angle_sbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(PHASE_SHIFT_KEY,
                                                          self.view.widgets.measurement_config_menu_angle_sbox.value())
        )
        # measurement_config_menu_laser_ledit = QLineEdit
        self.view.widgets.measurement_config_menu_laser_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(NAME_LIGHT_KEY,
                                                          self.view.widgets.measurement_config_menu_laser_ledit.text()))

        # measurement_config_menu_halogen_cbox = QComboBox
        self.view.widgets.measurement_config_menu_halogen_cbox.currentIndexChanged.connect(
            lambda: self.data_processing.set_legend_field(TYPE_LIGHT_KEY,
                                                          self.view.widgets.measurement_config_menu_halogen_cbox.currentText()))
        # detector_pmt_ledit = QLineEdit
        self.view.widgets.detector_pmt_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(TYPE_OF_DETECTOR_KEY,
                                                          self.view.widgets.detector_pmt_ledit.text()))

        # detector_voltage_ledit = QLineEdit
        self.view.widgets.detector_voltage_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(ADDITIONAL_INFO_DETECTOR_KEY,
                                                          self.view.widgets.detector_voltage_ledit.text()))

        # monochromator_in_in_start = QDoubleSpinBox
        self.view.widgets.monochromator_in_in_start.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(INPUT_CREVICE_BEGIN_KEY,
                                                          self.view.widgets.monochromator_in_in_start.value())
        )
        # monochromator_in_in_start_2 = QDoubleSpinBox
        self.view.widgets.monochromator_in_in_start_2.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(INPUT_CREVICE_END_KEY,
                                                          self.view.widgets.monochromator_in_in_start_2.value())
        )
        # monochromator_out_out_start = QDoubleSpinBox
        self.view.widgets.monochromator_out_out_start.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(OUTPUT_CREVICE_BEGIN_KEY,
                                                          self.view.widgets.monochromator_out_out_start.value())
        )
        # monochromator_out_in_start = QDoubleSpinBox
        self.view.widgets.monochromator_out_in_start.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(OUTPUT_CREVICE_END_KEY,
                                                          self.view.widgets.monochromator_out_in_start.value())
        )
        # monochromator_optical_filter_ledit = QLineEdit
        self.view.widgets.monochromator_optical_filter_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(OPTICAL_FILTER_KEY,
                                                          self.view.widgets.monochromator_optical_filter_ledit.text()))

        # devices_controls_devices_selection_volt_cbox = QComboBox
        self.view.widgets.devices_controls_devices_selection_volt_cbox.currentIndexChanged.connect(
            lambda: self.data_processing.set_legend_field(LOCK_IN_KEY,
                                                          self.view.widgets.devices_controls_devices_selection_volt_cbox.currentText()))
        # devices_controls_devices_selection_disperse_cbox = QComboBox
        self.view.widgets.devices_controls_devices_selection_disperse_cbox.currentIndexChanged.connect(
            lambda: self.data_processing.set_legend_field(DISPERSE_ELEMENT,
                                                          self.view.widgets.devices_controls_devices_selection_disperse_cbox.currentText()))

        # radioButton = QRadioButton
        self.view.widgets.radioButton.toggled.connect(
            self.set_unit_type_angle)
        # radioButton_2 = QRadioButton
        self.view.widgets.radioButton_2.toggled.connect(
            self.set_unit_type_angstrom)

        self.initialize_formular()

    def initialize_formular(self):
        for key, value in self.data_processing.settings.items():
            if key == NAME_SAMPLE_KEY:
                pass
            elif key == NOTE_TO_TECH_KEY:
                pass
            elif key == THICKNESS_KEY:
                pass
            elif key == MEASURE_OF_SAMPLE_KEY:
                pass
            elif key == TEMPERATURE_KEY:
                pass
            elif key == TYPE_OF_DISPERS_ELEM_KEY:
                pass
            elif key == NAME_OF_DISPERS_ELEM_KEY:
                pass
            elif key == INPUT_CREVICE_BEGIN_KEY:
                pass
            elif key == INPUT_CREVICE_END_KEY:
                pass
            elif key == OUTPUT_CREVICE_BEGIN_KEY:
                pass
            elif key == OUTPUT_CREVICE_END_KEY:
                pass
            elif key == OPTICAL_FILTER_KEY:
                pass
            elif key == TYPE_OF_DETECTOR_KEY:
                pass
            elif key == ADDITIONAL_INFO_DETECTOR_KEY:
                pass
            elif key == TYPE_LIGHT_KEY:
                pass
            elif key == NAME_LIGHT_KEY:
                pass
            elif key == STEP_OF_MOTOR_KEY:
                pass
            elif key == NUM_OF_INTEGRATIONS_KEY:
                pass
            elif key == CORRECTION_KEY:
                pass
            elif key == LOCK_IN_KEY:
                pass
            elif key == TYPE_SENSITIVITY_KEY:
                pass
            elif key == LOCK_IN_REFERENCE_KEY:
                pass
            elif key == RANGE_KEY:
                pass
            elif key == PHASE_SHIFT_KEY:
                pass
            elif key == TIME_CONSTANT_KEY:
                pass
            elif key == START_POSITION_KEY:
                pass
            elif key == END_POSITION_KEY:
                pass

    def set_auto_check_value(self):
        if self.view.widgets.measurement_config_menu_span_auto_check.isChecked():
            self.data_processing.set_legend_field(TYPE_SENSITIVITY_KEY, AUTO)
        else:
            self.data_processing.set_legend_field(TYPE_SENSITIVITY_KEY, MANUAL)

    def set_unit_type_angle(self):
        if self.view.widgets.radioButton.isChecked():
            self.data_processing.set_unit_type_position(Unit.Uhol)

    def set_unit_type_angstrom(self):
        if self.view.widgets.radioButton_2.isChecked():
            self.data_processing.set_unit_type_position(Unit.Angstrom)

    def get_model(self, key):
        if key == self._key:
            return self._data_processing
        else:
            raise ValueError("Invalid key")

    def set_settings(self, settings):
        self._data_processing.set_settings(settings)
        self.settings_changed_s.emit(settings)


