from time import sleep
from PySide6.QtCore import QObject, QRunnable, QThreadPool, QEventLoop, QMetaObject, QThread, Qt, QStringConverter, QGenericArgument, Q_ARG
import PySide6
from controllers.file_manager_controller import FileManagerController
from controllers.logger_controller import LoggerController
from controllers.measurement_controller.measurement_controller import MeasurementController

from functools import partial

class MainController(QObject):
    def __init__(self, view, key):
        super(MainController, self).__init__()
        self.workers = QThreadPool().globalInstance()
        self._key = key
        self.file_manager = FileManagerController(key)
        self.logger = LoggerController(key)
        self._measurement = MeasurementController(view)

    def _interconnect_file_manager_controller(self):
        # connects the file manager controller to other controllers
        self.file_manager.log_s.connect(lambda level, message, show_user: self.logger.log(level, message, show_user))

    def start_measurement(self, start, stop, stepSize):
        #self.measurement.addArgument(argument)
        QMetaObject.invokeMethod(
            self._measurement, "start",
            Qt.QueuedConnection,
            Q_ARG(float,start),
            Q_ARG(float,stop),
            Q_ARG(int,stepSize),
            )
            
    def stop_measurement(self):
        QMetaObject.invokeMethod(self._measurement, 'stop', Qt.QueuedConnection)
        
    def go_to_pos(self, pos):
        QMetaObject.invokeMethod(self._measurement, 'moveToPos', Qt.QueuedConnection, Q_ARG(float,pos))

    def initialization(self, pos):
        QMetaObject.invokeMethod(self._measurement, 'initialization', Qt.QueuedConnection, Q_ARG(float,pos))

    def move_forward(self, steps):
        QMetaObject.invokeMethod(self._measurement, 'moveForward', Qt.QueuedConnection, Q_ARG(int,steps))

    def move_reverse(self, steps):
        QMetaObject.invokeMethod(self._measurement, 'moveReverse', Qt.QueuedConnection, Q_ARG(int,steps))

    def test_method(self, a,b,c):
        print("a , b , c = ", a, b, c)
        #string = '100'
        #fromUtf16 = PySide6.QtCore.QStringEncoder(PySide6.QtCore.QStringEncoder.Utf16)
        #s = fromUtf16(string)
        #enc = partial(str.encode, encoding='utf-16')

        #alternative
        #enc = PySide6.QtCore.QStringEncoder(PySide6.QtCore.QStringConverter.Encoding.Utf8)
        #s = enc('text')
        #vstup = QMetaObject.newInstance()

        #QMetaObject.invokeMethod(self._measurement, 'moveTest', Qt.QueuedConnection, Q_ARG(float,steps))

    def exit_measurement(self, key):
        if key == self._key:
            self._measurement.exit()
            
    def update_measurement_settings(self, key, value):
        self.data_processing.set_legend_field(key, value)

