from PySide6 import QtCore
from PySide6.QtCore import QObject, Signal, QThread, QTimer, QGenericArgument

from errors.data_processing_error import DataProcessingError
from models.motor.Motor import Motor
from models.lockin.lockin import SR510
from models.disperse_element import Grating
from models.logger.constants import *
from models.data_processing.dataProcessing import DataProcessing
from PySide6.QtCore import QEventLoop

import time
from serial.tools import list_ports

class MeasurementController(QObject):
    state_s = Signal(str)
    progress_s = Signal(float)
    voltmeter_status_s = Signal(bool)
    measured_value_s = Signal(float, float, bool)
    new_measurement_started_s = Signal()
    lockin_settings_s = Signal(dict)
    measurement_start_fail_s = Signal()

    def __init__(self):
        '''
        initializes measurement controller object
        '''
        super(MeasurementController, self).__init__()
        self.angle = None
        self.running = False
        self._lockin = None
        self._motor = None
        self._elem = None
        self.correction = 0
        self.integrations = 1

        self.sr510_sn = 'A7CB1935A'
        self.lockin_comport = None

        self.timer = QTimer()
        self.timer.timeout.connect(self.check_lockin_availability)
        self.timer.start(750)

        if self._motor is None:
            # self.check_motor_availability()
            self._motor = Motor('COM4')

        self._measurement_thread = QThread()
        self._measurement_thread.setPriority(QThread.HighestPriority)
        self._measurement_thread.finished.connect(self._measurement_thread.deleteLater)
        self.moveToThread(self._measurement_thread)
        self._measurement_thread.start()
        
    def check_motor_availability(self):
        '''
        check if motor is connected
        '''
        availableComPorts = list_ports.comports()
        for acp in availableComPorts:
            for i in acp:
                print(i)
                
    def check_lockin_availability(self):
        '''
        check if lockin is connected
        '''
        availableComPorts = list_ports.comports()
        for acp in availableComPorts:
            if acp.serial_number == self.sr510_sn:
                self.lockin_comport = acp.name
                if self._lockin is None:
                    self.connect_lockin()

                self.voltmeter_status_s.emit(True)
                return
        self._lockin = None
        self.voltmeter_status_s.emit(False)

    def get_important_lockin_values(self):
        '''
        get/load lockin parameters
        '''
        data = {
            'pre_time_const': self._lockin.get_pre_time_const(),
            'post_time_const': self._lockin.get_post_time_const(),
            'phase_shift': self._lockin.get_phase(),
            'ref_frequency': self._lockin.get_ref_frequency(),
            'bandpass_filter': self._lockin.get_bandpass_filter()
        }
        print(data)
        self.lockin_settings_s.emit(data)
        
    def connect_lockin(self):
        '''
        connect milivoltmeter device
        '''
        self._lockin = SR510(self.lockin_comport)
        self.get_important_lockin_values()

    def link_data_processing_controller(self, dpc):
        '''
        connect data processing controller object
        @param dpc: data processing controller
        '''
        self.data_processing_controller = dpc

    def link_logger(self, log):
        '''
        connect data logger controller object
        @param log: logger controller
        '''
        self.logger = log

    @QtCore.Slot(str)
    def set_disperse_element(self, name):
        '''
        set disperse element
        @param name: name of disperse element
        '''
        print('setting different disp elem')
        self._elem = Grating(name)

    def adjust_sensitivity(self, measuredValue):
        '''
        adjust lockin sensitivity, based on measured value
        @param measuredValue: current measured value
        '''
        #todo 3*pre_time_constant sleep after change

        if measuredValue < 0:
            return

        cur_gain = self._lockin.current_gain_value()
        print(f'namerana hodnota: {measuredValue}, current sensitivity {cur_gain} ')

        if measuredValue >= 0.7 * cur_gain:
            self._lockin.lower_gain()
            print(f'Zosilnenie sa znizilo na {self._lockin.current_gain_value()}')

        if measuredValue <= 0.2 * cur_gain:
            self._lockin.higher_gain()
            print(f'Zosilnenie sa zvysilo na {self._lockin.current_gain_value()}')

    def sendMeasurement(self, angle, elem, value, correction):
        '''
        send measurement to data processing controller
        @param angle: angle of grid (position of measurement)
        @param elem: used grid
        @param value: measured value at concrete angle
        @param correction: used correction of measurement
        @raise data_processing_error: raises an exception when trying to send measuremnt
        '''
        wavelength = elem.angleToWavelength(angle) + correction

        try:
            self.data_processing_controller.data_processing.add_measurement(angle, wavelength, value)
        except DataProcessingError as e:
            self.logger.log(WARNING, e.message, True)
            return

        self.measured_value_s.emit(wavelength, value, True)

    def failed_measurement(self, msg):
        '''
        failed measurement
        @param msg: message to show when failed measurement
        '''
        self.logger.log(WARNING, msg, True)
        self.measurement_start_fail_s.emit()

    @QtCore.Slot(float, int)
    def set_arguments(self, correction, integrations):
        '''
        set additional measurement arguments
        @param correction: correction value for given measurement
        @param integrations: integration value for given measurement
        '''
        self.correction = correction
        self.integrations = integrations

    @QtCore.Slot(float, float, int)
    def start(self, start, end, stepsPerDataPoint):
        '''
        start overall measurement
        @param start: start position of measurement (angle)
        @param end: end position of measurement (angle)
        @param stepsPerDataPoint: number of step per one measured value
        @raise data_processing_error: raises an exception when trying to start measurement
        '''
        print('lockin')
        if self._lockin is None:
            self.failed_measurement("Lockin nie je pripojený.")
            return
        print('elem')
        if self._elem is None:
            self.failed_measurement("Neexistuje žiadny disperzný prvok.")
            return

        print('angle')
        if self.angle is None:
            self.failed_measurement("Motor nie je inicializovaný.")
            return

        print('distance')
        distance = end - self.angle
        if distance <= 0:
            self.failed_measurement("Začiatok merania musí by menší ako koniec merania.")
            return

        self._lockin.prepare()
        self.get_important_lockin_values()

        print('try')
        try:
            self.data_processing_controller.data_processing.create_new_file()
        except DataProcessingError as e:
            self.failed_measurement(e.message)
            return

        print('try2')

        self.new_measurement_started_s.emit()
        self.running = True

        elem = self._elem
        correction = self.correction
        integrations = self.integrations
        steps = elem.angleToSteps(distance)
        last_step = steps % stepsPerDataPoint
        data_points = steps // stepsPerDataPoint

        print(f"dist: {distance} \nsteps: {steps} \nvalues: {data_points}")

        anglePerDataPoint = elem.stepsToAngle(stepsPerDataPoint)

        measured_value = self._lockin.read_value()
        self.sendMeasurement(self.angle, elem, measured_value, correction)

        for i in range(data_points):
            if self.running == False:
                return

            self.progress_s.emit(i / data_points * 100)
            print(f"iter: {i}")
                
            duration = self._motor.moveForward(stepsPerDataPoint)
            time.sleep(duration)
            self.angle += anglePerDataPoint

            measured_values = [self._lockin.read_value() for _ in range(integrations)]
            measured_value = sum(measured_values) / len(measured_values)

            self.sendMeasurement(self.angle, elem, measured_value, correction)
            self.adjust_sensitivity(measured_value)
            
            print(f"pos: {self.angle:.3f} measurement: {measured_value}")

        if last_step > 0 and self.running:
            duration = self._motor.moveForward(last_step)
            time.sleep(duration)
            self.angle += elem.stepsToAngle(last_step)

            measured_values = [self._lockin.read_value() for _ in range(integrations)]
            measured_value = sum(measured_values) / len(measured_values)

            self.sendMeasurement(self.angle, elem, measured_value, correction)
            
            print(f"pos: {self.angle:.3f} measurement: {measured_value}")

        self.progress_s.emit(100)
        self.running = False

    @QtCore.Slot()
    def stop(self):
        '''
        stop running measurement
        '''
        self.running = False

    @QtCore.Slot(float)
    def moveTest(self, steps=20):
        print(f'move je uspesny, pocet krokov: {steps}')
        self._motor.moveForward(int(steps))

    @QtCore.Slot(float)
    def moveToPos(self, stop):
        '''
        move to specified position
        @param stop: position, where to move (angle)
        '''
        if self.angle is None or self.angle == stop or not self._elem.canMoveTo(stop) or self.running:
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
        '''
        move forward given steps
        @param steps: number of steps
        '''
        print(f'moveF je uspesny, pocet krokov: {steps}')
        self._motor.moveForward(steps)

    @QtCore.Slot(int)
    def moveReverse(self, steps):
        '''
        move reverse given steps
        @param steps: number of steps
        '''
        print(f'moveR je uspesny, pocet krokov: {steps}')
        self._motor.moveReverse(steps)
        
    @QtCore.Slot(float)
    def initialization(self, pos):
        '''
        initialize position of stepped motor
        @param pos: position, which to be used for initialization (angle)
        '''
        self.angle = pos
    
    def exit(self):
        '''
        exit measurement
        '''
        self._measurement_thread.quit()
        self._measurement_thread.wait()
