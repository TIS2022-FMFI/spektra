import random
import sys
import os
from datetime import datetime

from PySide6.QtCore import QThread
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QHeaderView
from controllers.main_controller import MainController
from view.view import View
from settings import Settings
from models.data_processing.dataProcessing import DataProcessing
from models.data_processing.constants import *

os.environ["QT_STYLE_OVERRIDE"] = "Fusion"



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        random.seed(datetime.now().microsecond)
        self._secret = random.random()
        self.view = View(self)
        self.controller = MainController(self._secret)
        self._connect_view_controller()
        self.setWindowTitle(Settings.TITLE)
        self.show()

        self.data_processing = DataProcessing()

        self.view.widgets.saple_name_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(NAME_SAMPLE_KEY, self.view.widgets.saple_name_ledit.text()))

        self.view.widgets.sample_temperature_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(TEMPERATURE_KEY, self.view.widgets.sample_temperature_ledit.text()))

        #sample_width_dsbox - QDoubleSpinBox
        self.view.widgets.sample_width_dsbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(THICKNESS_KEY, self.view.widgets.sample_width_dsbox.value())
        )
        #sample_note_ledit = QLineEdit
        self.view.widgets.sample_note_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(NOTE_TO_TECH_KEY, self.view.widgets.sample_note_ledit.text()))

        #sample_measurement_ledit = QLineEdit
        self.view.widgets.sample_measurement_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(MEASURE_OF_SAMPLE_KEY, self.view.widgets.sample_measurement_ledit.text()))

        #measurement_config_menu_filename_ledit = QLineEdit
        self.view.widgets.measurement_config_menu_filename_ledit.editingFinished.connect(
            lambda: self.data_processing.set_file_name(self.view.widgets.measurement_config_menu_filename_ledit.text()))

        #measurement_config_menu_end_sbox = QDoubleSpinBox
        self.view.widgets.measurement_config_menu_end_sbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(START_POSITION_KEY, self.view.widgets.measurement_config_menu_end_sbox.value())
        )
        #.measurement_config_menu_start_sbox = QDoubleSpinBox
        self.view.widgets.measurement_config_menu_start_sbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(END_POSITION_KEY, self.view.widgets.measurement_config_menu_start_sbox.value())
        )
        #measurement_integrations_sbox = QSpinBox
        self.view.widgets.measurement_integrations_sbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(NUM_OF_INTEGRATIONS_KEY, self.view.widgets.measurement_integrations_sbox.value())
        )
        #measurement_correction_sbox = QDoubleSpinBox
        self.view.widgets.measurement_correction_sbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(CORRECTION_KEY, self.view.widgets.measurement_correction_sbox.value())
        )
        #measurement_motor_step = QSpinBox
        self.view.widgets.measurement_motor_step.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(STEP_OF_MOTOR_KEY, self.view.widgets.measurement_motor_step.value())
        )
        #measurement_config_menu_ref_sbox = QSpinBox
        self.view.widgets.measurement_config_menu_ref_sbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(LOCK_IN_REFERENCE_KEY, self.view.widgets.measurement_config_menu_ref_sbox.value())
        )
        #measurement_config_menu_span_dsbox = QDoubleSpinBox
        self.view.widgets.measurement_config_menu_span_dsbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(RANGE_KEY, self.view.widgets.measurement_config_menu_span_dsbox.value())
        )
        #measurement_config_menu_span_auto_check = QCheckBox
        #measurement_config_menu_time_const_dsbox = QDoubleSpinBox
        self.view.widgets.measurement_config_menu_time_const_dsbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(TIME_CONSTANT_KEY, self.view.widgets.measurement_config_menu_time_const_dsbox.value())
        )
        #measurement_config_menu_angle_sbox = QSpinBox
        self.view.widgets.measurement_config_menu_angle_sbox.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(PHASE_SHIFT_KEY, self.view.widgets.measurement_config_menu_angle_sbox.value())
        )
        #measurement_config_menu_laser_ledit = QLineEdit
        self.view.widgets.measurement_config_menu_laser_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(NAME_LIGHT_KEY, self.view.widgets.measurement_config_menu_laser_ledit.text()))

        #measurement_config_menu_halogen_cbox = QComboBox
        #detector_pmt_ledit = QLineEdit
        self.view.widgets.detector_pmt_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(TYPE_OF_DETECTOR_KEY, self.view.widgets.detector_pmt_ledit.text()))

        #detector_voltage_ledit = QLineEdit
        self.view.widgets.detector_voltage_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(ADDITIONAL_INFO_DETECTOR_KEY, self.view.widgets.detector_voltage_ledit.text()))

        #monochromator_in_in_start = QDoubleSpinBox
        self.view.widgets.monochromator_in_in_start.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(INPUT_CREVICE_BEGIN_KEY, self.view.widgets.monochromator_in_in_start.value())
        )
        #monochromator_in_in_start_2 = QDoubleSpinBox
        self.view.widgets.monochromator_in_in_start_2.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(INPUT_CREVICE_END_KEY, self.view.widgets.monochromator_in_in_start_2.value())
        )
        #monochromator_out_out_start = QDoubleSpinBox
        self.view.widgets.monochromator_out_out_start.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(OUTPUT_CREVICE_BEGIN_KEY, self.view.widgets.monochromator_out_out_start.value())
        )
        #monochromator_out_in_start = QDoubleSpinBox
        self.view.widgets.monochromator_out_in_start.valueChanged.connect(
            lambda: self.data_processing.set_legend_field(OUTPUT_CREVICE_END_KEY, self.view.widgets.monochromator_out_in_start.value())
        )
        #monochromator_optical_filter_ledit = QLineEdit
        self.view.widgets.monochromator_optical_filter_ledit.editingFinished.connect(
            lambda: self.data_processing.set_legend_field(OPTICAL_FILTER_KEY, self.view.widgets.monochromator_optical_filter_ledit.text()))

        #devices_controls_devices_selection_volt_cbox = QComboBox
        #devices_controls_devices_selection_disperse_cbox = QComboBox

        #asi uhol/angstrom
        #radioButton = QRadioButton
        #radioButton_2 = QRadioButton


    def set_legend_item(self, q_line_edit, key):
        print("sprava ", q_line_edit.text())

    def _connect_view_controller(self):
        # connect the view with controllers
        self._connect_file_manager_controller()
        self._connect_logger_controller()
        self._connect_graph_controller()
        self._connect_motor_controller()
        self._connect_measurement_controller()

    def _connect_file_manager_controller(self):
        def setup_file_manager_model(file_manager_model):
            self.view.widgets.comparative_file_dir_tree_view.setModel(file_manager_model)
            self.view.widgets.comparative_file_dir_tree_view.setRootIndex(
                file_manager_model.index(file_manager_model.root_file_path))
            self.view.widgets.comparative_file_dir_tree_view.hideColumn(1)
            self.view.widgets.comparative_file_dir_tree_view.hideColumn(2)
            self.view.widgets.comparative_file_dir_tree_view.setHeaderHidden(True)
            self.view.widgets.comparative_file_dir_tree_view.setAnimated(True)
            header = self.view.widgets.comparative_file_dir_tree_view.header()
            header.setSectionResizeMode(QHeaderView.ResizeToContents)

        setup_file_manager_model(self.controller.file_manager.get_model(self._secret))
        self.controller.file_manager.log_s.connect(
            lambda level, msg, show: self.controller.logger.log(level, msg, show))
        self.view.widgets.change_comparative_dir_btn.clicked.connect(self.change_current_directory)

    def change_current_directory(self):
        idx = self.controller.file_manager.change_current_directory(QFileDialog.getExistingDirectory())
        if idx is not None:
            self.view.widgets.comparative_file_dir_tree_view.setRootIndex(idx)

    def _connect_logger_controller(self):
        self.controller.logger.display_log_s.connect(lambda log: self.view.display_log(log))
        # example only to show functionality
        self.view.widgets.comparative_file_unload_btn.clicked.connect(
            lambda: self.controller.logger.log(40, 'User clicked on btn Zrus', True))

    def _connect_graph_controller(self):
        pass

    def _connect_motor_controller(self):
        pass

    def _connect_measurement_controller(self):
        self.controller._measurement.state_s.connect(lambda x: self.controller.logger.log(40, x, True))
        self.view.widgets.comparative_file_unload_btn.clicked.connect(self.test)

    def test(self):
        print("test() thread id: ")
        print(QThread.currentThread())

    def closeEvent(self, event):
        self.controller.logger.save_logs_to_file()
        self.controller.exit_measurement(self._secret)
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
