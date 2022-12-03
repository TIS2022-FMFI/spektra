import random
import sys
import os
from datetime import datetime

from PySide6.QtWidgets import QMainWindow, QApplication
from pyqtgraph.Qt import QtCore

from controllers.main_controller import MainController
from models.data_processing.data_processing import DataProcessing
from models.data_processing.graph import Graph
from view.view import View
from settings import Settings
import pyqtgraph as pg

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%
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
        self.set_theme()
        self.show()

        #TOTO ESTE DOKONCIT TAK ABY BOL GRAF TAM KDE MA
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        graph = Graph(self.graphWidget)


    def set_theme(self):
        theme_file = "themes/" + Settings.THEME + ".qss"
        if os.path.exists(theme_file):
            with open(theme_file, "r") as f:
                self.setStyleSheet(f.read())

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

        setup_file_manager_model(self.controller.file_manager.get_model(self._secret))

    def _connect_logger_controller(self):
        self.controller.logger.display_log_s.connect(lambda log: self.view.display_log(log))
        # example only to show functionality
        self.view.widgets.comparative_file_unload_btn.clicked.connect(
            lambda: self.controller.logger.success('User clicked on btn Zrus', True))

    def _connect_graph_controller(self):
        pass

    def _connect_motor_controller(self):
        pass

    def _connect_measurement_controller(self):
        pass

    def closeEvent(self, event):
        self.controller.logger.save_logs_to_file()
        event.accept()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())




