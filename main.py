import random
import sys
import os
from datetime import datetime

from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QHeaderView
from qtpy import QtWidgets

from controllers.main_controller import MainController
from errors.data_processing_error import DataProcessingError
from models.data_processing.dataProcessing import DataProcessing
from view.view import View
from settings import Settings
from controllers.measurement_controller.data_processing_controller import DataProcessingController
from models.logger.constants import *

os.environ["QT_STYLE_OVERRIDE"] = "Fusion"


class MainWindow(QMainWindow):
    def __init__(self):
        """
        initializes main object
        """
        super().__init__()
        random.seed(datetime.now().microsecond)
        self._secret = random.random()

        self.view = View(self)
        self.controller = MainController(self.view, self._secret)

        self.view.widgets.graph_view.add_views(self.view)
        self.view.widgets.graph_view.add_logger(self.controller.logger)
        self.view.widgets.graph_view.plotGraph()

        self.view.widgets.actionPorovnanie.triggered.connect(self._load_comparative_file)
        self.view.widgets.action_save_as.triggered.connect(self.file_save)
        self.view.widgets.action_exit.triggered.connect(self.close)

        self.data_processing_controller = DataProcessingController(self.view, self._secret)
        self.data_processing_controller.add_logger(self.controller.logger)

        self._connect_view_controller()
        self.setWindowTitle(Settings.TITLE)

        self.show()

    def _load_comparative_file(self):
        file_name = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")[0]

        try:
            loaded_settings, measurements = DataProcessing(self.view).load_old_file(file_name)
        except DataProcessingError as e:
            self.controller.logger.log(WARNING, e.message, True)
            return
        self.view.widgets.graph_view.addMeasurement(measurements, False)
        name = file_name.split("\\")
        if "/" in file_name:
            name = file_name.split("/")
        name = name[-1]
        self.view.widgets.graph_view.change_label_name(name, False)
        self.view.widgets.graph_view.plotGraph()
        self.view.widgets.textBrowser.setText(str(loaded_settings))

    def _connect_view_controller(self):
        """
        connect the view with controllers
        """
        self._connect_file_manager_controller()
        self._connect_logger_controller()
        self._connect_measurement_controller()

    def _connect_file_manager_controller(self):
        """
        connect the view with file manager controller
        """
        
        def setup_file_manager_model(file_manager_model):
            """
            set up the file manager model
            @param file_manager_model: file manager model instance
            """
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
        changes current directory from which can user choose older measurement file for comparison
        this directory is chosen by user
        """
        idx_directory = self.controller.file_manager.change_current_directory(QFileDialog.getExistingDirectory())
        if idx_directory is None:
            return
        idx, directory = idx_directory
        if idx is not None:
            self.view.widgets.comparative_file_dir_tree_view.setRootIndex(idx)

    def _connect_logger_controller(self):
        """
        connect the view with logger controller
        """
        self.controller.logger.display_log_s.connect(lambda log: self.view.display_log(log))

    def _connect_measurement_controller(self):
        """
        connect the view with file measurement controller, binds all GUI objects concerning motor movement and
        measurement with backend
        """
        widgets = self.view.widgets
        self.controller._measurement.link_data_processing_controller(
            self.data_processing_controller.data_processing)

        widgets.actionO_programe.triggered.connect(widgets.about_dialog.show)
        widgets.actionDokument_cia.triggered.connect(self.view.open_documentation)
        widgets.actionDenn.triggered.connect(self.view.change_to_light_theme)
        widgets.actionNo_n.triggered.connect(self.view.change_to_dark_theme)

        self.view.update_disperse_elements_list()

    def closeEvent(self, event):
        """
        process to be done before closing
        @param event: event object
        """
        if not self.controller.logger.is_logger_empty():
            self.controller.logger.save_logs_to_file()
        self.controller.exit_measurement(self._secret)
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
