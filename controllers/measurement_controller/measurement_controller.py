from PySide6 import QtCore
from PySide6.QtCore import QObject, Signal, QThread

from models.data_processing.data_processing import data_processing
from PySide6.QtCore import QEventLoop


class MeasurementController(QObject):
    state_s = Signal(str)
    progress_s = Signal(float)

    def __init__(self):
        super(MeasurementController, self).__init__()
        self._lockin = None
        self._motor = None
        self._data_processing = data_processing()
        self._measurement_thread = QThread()
        self._measurement_thread.setPriority(QThread.HighestPriority)
        self._measurement_thread.finished.connect(self._measurement_thread.deleteLater)
        self.moveToThread(self._measurement_thread)
        self._measurement_thread.start()

    @QtCore.Slot()
    def start(self):
        # TODO: implement method to handle measurement from start to finish
        # method should report progress
        # method should be able to be stopped, therefore it should check event loop for requests during execution
        pass

    @QtCore.Slot()
    def stop(self):
        # TODO: implement method to stop measurement. Checks if measurement is running and if so, stops it and emits signal that state changed
        pass

    def exit(self):
        self._measurement_thread.quit()
        self._measurement_thread.wait()
