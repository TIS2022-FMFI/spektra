import random
import sys
import os
from datetime import datetime

from PySide6.QtCore import QThread
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QHeaderView
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
        self.controller = MainController(self._secret)
        self.data_processing_controller = DataProcessingController(self.view)
        self._connect_view_controller()
        self.setWindowTitle(Settings.TITLE)
        
        self.show()

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
        Widgets = self.view.widgets
        de_cbox = Widgets.devices_controls_devices_selection_disperse_cbox
        ms_cont = self.controller._measurement

        ms_cont.set_dataproc_ref(self.data_processing_controller, self.view.widgets.graph_view)

        de_cbox.addItem('ms732')
        for i in range(5):
            de_cbox.addItem(f'mriezka{i}')
        
        de_cbox.activated.connect(
            lambda: ms_cont.disp_elem_change(de_cbox.currentText()))
        ms_cont.disp_elem_change(de_cbox.currentText())

        self.controller._measurement.state_s.connect(lambda x: self.controller.logger.log(40, x, True))
        Widgets.comparative_file_unload_btn.clicked.connect(self.test)

        # moveForward/moveReverse
        noStepsValue = lambda : Widgets.devices_controls_engine_positioning_step_sbox.value()
        Widgets.devices_controls_engine_positioning_right_btn.clicked.connect(
            lambda:self.controller.move_reverse(noStepsValue()))
        Widgets.devices_controls_engine_positioning_left_btn.clicked.connect(
            lambda:self.controller.move_forward(noStepsValue()))
        
        # moveToPosition
        gotoValue = lambda : Widgets.devices_controls_goto_sbox.value()
        Widgets.devices_controls_goto_btn.clicked.connect(
            lambda:self.controller.go_to_pos(gotoValue()))

        # init position
        initValue = lambda : Widgets.doubleSpinBox.value()
        Widgets.devices_controls_calibration_btn.clicked.connect(
            lambda:self.controller.initialization(initValue()))

        # meranie !!pozor start/end naopak v main_ui.py!!
        endValue = lambda : Widgets.measurement_config_menu_start_sbox.value()
        startValue = lambda : Widgets.measurement_config_menu_end_sbox.value()
        motorStepValue = lambda : Widgets.measurement_motor_step.value()

        Widgets.action_play.triggered.connect(
            lambda:self.controller.start_measurement(startValue(), endValue(), motorStepValue()))

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
