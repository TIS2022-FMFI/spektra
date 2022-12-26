import random
import sys
import os
from datetime import datetime

from PySide6.QtCore import QThread
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QHeaderView
from controllers.main_controller import MainController
from view.view import View
from settings import Settings

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
        
        # moveToPosition
        gotoValue = self.view.widgets.devices_controls_goto_sbox.text.value()
        self.view.widgets.devices_controls_goto_btn.clicked.connect(self.controller.measurement.moveToPos(gotoValue))

        numberOfSteps = self.view.widgets.devices_controls_engine_positioning_step_sbox.text.value()

        # moveForward
        self.view.widgets.devices_controls_engine_positioning_left_btn.clicked.connect(self.controller.measurement.moveForvard(numberOfSteps))

        # moverReverse
        self.view.widgets.devices_controls_engine_positioning_right_btn.clicked.connect(self.controller.measurement.moveReverse(numberOfSteps))

        # initialization
        init_position = self.view.widgets.doubleSpinBox.text.value() #TODO check if correct doubleSpinBox selected
        self.view.widgets.devices_controls_calibration_btn.clicked.connect(self.controller.initialization(init_position)) #TODO potentially rename as initialization in main


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
