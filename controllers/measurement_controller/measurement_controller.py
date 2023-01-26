from PySide6 import QtCore
from PySide6.QtCore import QObject, Signal, QThread, QTimer

from errors.data_processing_error import DataProcessingError
from models.motor.Motor import Motor
from models.lockin.lockin import SR510
from models.disp_elem import Grating
from models.data_processing.grid import Grid465645
from models.logger.constants import *
from models.data_processing.dataProcessing import DataProcessing
from PySide6.QtCore import QEventLoop

import time
from serial.tools import list_ports

class MeasurementController(QObject):
    state_s = Signal(str)
    progress_s = Signal(float)
    
    def __init__(self, view):
        super(MeasurementController, self).__init__()
        self.view = view
        Widgets = self.view.widgets
        self.fazovy_posun_btn = Widgets.measurement_config_menu_angle_sbox
        self.casova_konstanta = Widgets.measurement_config_menu_time_const_dsbox
        self.fazovy_posun_btn = Widgets.measurement_config_menu_angle_sbox
        self.fazovy_posun_btn = Widgets.measurement_config_menu_angle_sbox

        self.dispElemCBox = view.widgets.devices_controls_devices_selection_disperse_cbox
        self.dispElemCBox.activated.connect(
            lambda: self.disp_elem_change(self.dispElemCBox.currentText()))

        self.disp_elem_change(self.dispElemCBox.currentText())

        self.angle = None
        self.running = False
        self._lockin = None
        self._motor = None
        self._elem = None

        self.sr510_sn = 'A7CB1935A'
        self.lockin_comport = None

        self.timer = QTimer()
        self.timer.timeout.connect(self.check_lockin_availability)
        self.timer.start(1000)

        if self._motor is None:
            #self.check_motor_availability()
            self._motor = Motor('COM4')

        self._measurement_thread = QThread()
        self._measurement_thread.setPriority(QThread.HighestPriority)
        self._measurement_thread.finished.connect(self._measurement_thread.deleteLater)
        self.moveToThread(self._measurement_thread)
        self._measurement_thread.start()
    def check_motor_availability(self):
        availableComPorts = list_ports.comports()
        for acp in availableComPorts:
            for i in acp:
                print(i)
    def check_lockin_availability(self):
        availableComPorts = list_ports.comports()
        for acp in availableComPorts:
            if acp.serial_number == self.sr510_sn:
                print(acp.name)
                self.lockin_comport = acp.name
                if self._lockin is not None:
                    self.connect_lockin()
                self.view.on_voltmeter_connection_change(True)
                return
        self.view.on_voltmeter_connection_change(False)

    def connect_lockin(self):
        self._lockin = SR510(self.lockin_comport)
    def set_dataproc_ref(self, dp, gr, log):
        self.dataproc = dp
        self.graph = gr
        self.logger = log

    #@QtCore.Slot(str)
    def disp_elem_change(self, name):
        print(name)
        self._elem = Grating(name)
        if self._elem.IsCalib() is False:
            print('Kal nexist. treba kalibrovat')

    def adjust_sensitivity(self, measuredValue):
        cur_gain = self._lockin.current_gain_value()
        if measuredValue < 0:
            return

        print(f'namerana hodnota: {measuredValue}, current sensitivity {cur_gain} ')

        if measuredValue >= 0.85 * cur_gain:  # ak je hodnota vacsia nez 85% rozsahu
            self._lockin.lower_gain()
            print(f'Zosilnenie sa znizilo na {self._lockin.current_gain_value()}')

        if measuredValue <= 0.1 * cur_gain:  # ak je hodnota mensia nez 10% rozsahu
            self._lockin.higher_gain()
            print(f'Zosilnenie sa zvysilo na {self._lockin.current_gain_value()}')

    def sendMeasurement(self, angle, value):
        wavelength = Grid465645().get_wave_length(angle)

        try:
            self.dataproc.data_processing.add_measurement(angle, wavelength, value)
        except DataProcessingError as e:
            self.logger.log(WARNING, e.message, True)
            return
        self.graph.addMeasurement([[wavelength, value]], True)
        self.graph.plotGraph()

    # TODO: implement method to handle measurement from start to finish
    # method should report progress
    # method should be able to be stopped, therefore it should check event loop for requests during execution    
    @QtCore.Slot(float, float, int)
    def start(self, start, end, stepsPerDataPoint):
        if self.angle is None:
            return

        distance = end - self.angle
        assert distance > 0 #assert for now

        self._lockin.prepare()

        try:
            self.dataproc.data_processing.create_new_file()
        except DataProcessingError as e:
            self.logger.log(WARNING, e.message, True)
            return
        self.graph.initialize()
        self.graph.plotGraph()
        
        self.running = True

        elem = self._elem   
        steps = elem.angleToSteps(distance)
        last_step = steps % stepsPerDataPoint
        data_points = steps // stepsPerDataPoint

        print(f"dist: {distance} \nsteps: {steps} \nvalues: {data_points}")

        d = elem.stepsToAngle(stepsPerDataPoint)

        measured_value = self._lockin.read_value()
        self.sendMeasurement(self.angle, measured_value)

        for i in range(data_points):
            if self.running == False:
                break

            self.view.progressBar.setValue(i // data_points)
            print(f"iter: {i}")
                
            duration = self._motor.moveForward(stepsPerDataPoint)
            time.sleep(duration)
            self.angle += d
            
            measured_value = self._lockin.read_value()
            self.sendMeasurement(self.angle, measured_value)
            self.adjust_sensitivity(measured_value)
            
            print(f"pos: {self.angle:.3f} measurement: {measured_value}")

        if last_step > 0 and self.running:
            duration = self._motor.moveForward(last_step)
            time.sleep(duration)
            self.angle += elem.stepsToAngle(last_step)
            
            measured_value = self._lockin.read_value()
            self.sendMeasurement(self.angle, measured_value)
            
            print(f"pos: {self.angle:.3f} measurement: {measured_value}")
            
        self.running = False

##    @QtCore.Slot()
    def stop(self):
        self.running = False

    @QtCore.Slot(float)
    def moveTest(self, steps=20):
        print(f'move je uspesny, pocet krokov: {steps}')
        self._motor.moveForward(int(steps))

    @QtCore.Slot(float)
    def moveToPos(self, stop):
        if self.angle is None or self.angle == stop or not self._elem.canMove(stop) or self.running:
            return

        distance = stop - self.angle
        steps = self._elem.angleToSteps(abs(distance))
        print("number of steps", steps)
        ack = input("write 'go' if agree:")
        if ack == "go":
            self.angle = stop
            if distance > 0:
                self.moveForward(steps)
            else:
                self.moveReverse(steps)

    @QtCore.Slot(int)
    def moveForward(self, steps):
        print(f'moveF je uspesny, pocet krokov: {steps}')
        self._motor.moveForward(steps)

    @QtCore.Slot(int)
    def moveReverse(self, steps):
        print(f'moveR je uspesny, pocet krokov: {steps}')
        self._motor.moveReverse(steps)
        
    @QtCore.Slot(float)
    def initialization(self, pos):
        self.angle = pos
    
    def exit(self):
        self._measurement_thread.quit()
        self._measurement_thread.wait()
