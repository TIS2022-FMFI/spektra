import random
import sys
import os
from datetime import datetime

from PySide6.QtCore import QThread
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QHeaderView
from qtpy import QtGui, QtCore, QtWidgets

from controllers.main_controller import MainController
from view.view import View
from settings import Settings
from controllers.measurement_controller.data_processing_controller import DataProcessingController

os.environ["QT_STYLE_OVERRIDE"] = "Fusion"


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        random.seed(datetime.now().microsecond)
        self._secret = random.random()
        self.view = View(self)
        self.controller = MainController(self.view, self._secret)

        self.view.widgets.graph_view.add_views(self.view)
        self.view.widgets.graph_view.add_logger(self.controller.logger)
        self.view.widgets.graph_view.plotGraph()
        self.view.widgets.actionPorovnanie.triggered.connect(self.change_current_directory)
        self.view.widgets.action_save_as.triggered.connect(self.file_save)
        self.view.widgets.action_exit.triggered.connect(lambda: self.controller.exit_measurement(self._secret))
        self.data_processing_controller = DataProcessingController(self.view, self._secret)
        self.data_processing_controller.add_logger(self.controller.logger)

        self._connect_view_controller()
        self.setWindowTitle(Settings.TITLE)

        self.show()

    def _connect_view_controller(self):
        # connect the view with controllers
        self._connect_file_manager_controller()
        self._connect_logger_controller()
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

    def file_save(self):
        """
        saves measurement file to a location and with name specified by user
        """
        name = QtWidgets.QFileDialog.getSaveFileName(self, self.data_processing_controller.get_file_name())[0]
        self.data_processing_controller.save_as(name)

    def change_current_directory(self):
        """
        changes current directory from which can user choose older measurement file for comparision
        this directory is chosen by user
        """
        idx, directory = self.controller.file_manager.change_current_directory(QFileDialog.getExistingDirectory())
        if idx is not None:
            self.view.widgets.comparative_file_dir_tree_view.setRootIndex(idx)

    def _connect_logger_controller(self):
        self.controller.logger.display_log_s.connect(lambda log: self.view.display_log(log))
        # example only to show functionality
        self.view.widgets.comparative_file_unload_btn.clicked.connect(
            lambda: self.controller.logger.log(40, 'User clicked on btn Zrus', True))

    def _connect_measurement_controller(self):
        widgets = self.view.widgets
        ms_controller = self.controller._measurement

        ms_controller.link_data_processing_controller(self.data_processing_controller)
        ms_controller.link_logger(self.controller.logger)

        ms_controller.state_s.connect(lambda x: self.controller.logger.log(40, x, True))

        widgets.comparative_file_unload_btn.clicked.connect(self.test)

       
        # switch units
        unitAngstromActive = lambda : Widgets.radioButton_2.isChecked()
        
        # moveForward/moveReverse
        steps_box = Widgets.devices_controls_engine_positioning_step_sbox
        steps_box.setRange(0, 1000)
        steps_box.setSingleStep(1)
        noStepsValue = lambda : int(steps_box.value())
        Widgets.devices_controls_engine_positioning_right_btn.clicked.connect(
            lambda:self.controller.move_reverse(noStepsValue()))
        Widgets.devices_controls_engine_positioning_left_btn.clicked.connect(
            lambda:self.controller.move_forward(noStepsValue()))

        gotoValueInRightUnits = lambda : self.mriezka.get_angle_from_wawe(gotoValue()) if unitAngstromActive() else gotoValue()
        
        # moveToPosition
        gotoValue = lambda : Widgets.devices_controls_goto_sbox.value()
        Widgets.devices_controls_goto_btn.clicked.connect(
            lambda:self.controller.go_to_pos(
                gotoValueInRightUnits()))
        
        # init position
        initValue = lambda : Widgets.doubleSpinBox.value()
        initValueInRightUnits = lambda : self.mriezka.get_angle_from_wawe(initValue()) if unitAngstromActive() else initValue()
        Widgets.devices_controls_calibration_btn.clicked.connect(
            lambda:self.controller.initialization(initValueInRightUnits()))

        # meranie
        endValue = lambda : Widgets.measurement_config_menu_start_sbox.value()
        endValueInRightUnits = lambda : self.mriezka.get_angle_from_wawe(endValue()) if unitAngstromActive() else endValue()

        startValue = lambda : Widgets.measurement_config_menu_end_sbox.value()
        startValueInRightUnits = lambda : self.mriezka.get_angle_from_wawe(startValue()) if unitAngstromActive() else startValue()

        motorStepValue = lambda : Widgets.measurement_motor_step.value()

        Widgets.action_play.triggered.connect(
            lambda:self.controller.start_measurement(startValueInRightUnits(), endValueInRightUnits(), motorStepValue()))

        widgets.action_play.triggered.connect(
            lambda: self.controller.start_measurement(startValue(), endValue(), motorStepValue()))

        widgets.action_play.triggered.connect(self.view.switch_play_button)
        widgets.action_stop.triggered.connect(self.view.switch_play_button)
        widgets.action_stop.triggered.connect(self.controller.stop_measurement)

        widgets.actionKalibr_cia.triggered.connect(self.view.show_calibration_dialog)
        widgets.calibration_dialog.calibration_data_s.connect(
            lambda data: self.controller.create_calibration(data))
        widgets.calibration_dialog.step_button.clicked.connect(
            lambda: self.controller.move_forward(widgets.calibration_dialog.step_size.value()))

        self.view.update_disperse_elements_list()

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
