from PySide6 import QtCore
from PySide6.QtCore import QObject, Signal, QThread

from models.data_processing.data_processing import DataProcessing
from PySide6.QtCore import QEventLoop


class MeasurementController(QObject):
    state_s = Signal(str)
    progress_s = Signal(float)
    _motor = None
    _lockin = None
    _elem = None

    def __init__(self):
        super(MeasurementController, self).__init__()
        
        self.running = False

        self.position = None
        disperse_element_name = 'ms732'  # z gui

        print('Dostupne COM porty:')
        availableComPorts = serial.tools.list_ports.comports()
        for acp in availableComPorts:
            print(acp.name + '/' + acp.description)

        if self._lockin is None:
            self._lockin = lockin.SR510()

        if self._motor is None:
            self._motor = motor.Motor('COM4')

        if self._elem is None:
            Measurement._elem = Grating(disperse_element_name)
            if self._elem.IsCalib() is False:
                print('kal nexist. treba kalibrovat')
        
        self._lockin = None
        self._motor = None
        self._data_processing = DataProcessing()
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
        while self.running:
            # self.progress_s.emit(0.5)
            # loop =QEventLoop()
            # loop.exec()

            self._lockin.prepare()

            #TODO read from gui
            stepsPerDataPoint = 32 
            end = None 
            
            distance = end - self.position
            assert distance > 0 #assert for now
                
            steps = self._elem.vlnaNaKroky(distance)
            last_step = steps % stepsPerDataPoint
            data_points = steps // stepsPerDataPoint + (1 if last_step != 0 else 0)

            print(f"dist: {distance} \nsteps: {steps} \nvalues: {data_points}")

            for i in range(data_points):
                print(f"iter: {i}")
                
                duration = self._motor.moveForward(stepsPerDataPoint)
                time.sleep(duration)
                
                measured_value = self._lockin.precitaj_hodnotu()
                cur_pos = self.position + self._elem.krokyNaVlna((i+1)*stepsPerDataPoint)
                print(f"pos: {cur_pos:.3f} measurement: {measured_value}")

            self.position = cur_pos 
    
    def moveReverse(self, steps):
        if not self.running:
            self._motor.moveReverse(steps)
            

    def moveForward(self, steps):
        if not self.running:
            self._motor.moveForward(steps)
            

    def moveToPos(self, stop):
        if self.position is None or self.position == stop or not self._elem.canMove(stop) or self.running:
            return

        distance = stop - self.position
        steps = self._elem.vlnaNaKroky(abs(distance))
        print("number of steps", steps)
        ack = input("write 'go' if agree:")
        if ack == "go":
            self.position = stop
            if distance > 0:
                self.moveForward(steps)
            else:
                self.moveReverse(steps)
                
    
    def calibration(self):
        if not self.running:
            start = float(input('zadaj startovaciu polohu: '))
            steps = 0
            while True:
                userInput = int(input('pocet krokov dopredu: '))
                if vstup == 0:
                    break
                steps += userInput
                self.moveForward(userInput)

            if steps <= 0:
                return

            self.position = end = float(input('zadaj koncovu polohu: '))

            res = (end - start) / steps
            self._elem.krok = res
            
                
    def initialization(self, p):
        self.position = p
        

    def save_calibration(self):
        self._elem.save()
        
    @QtCore.Slot()
    def stop(self):
        # TODO: implement method to stop measurement. Checks if measurement is running and if so, stops it and emits signal that state changed
        self.running = False

    def exit(self):
        if self._motor is not None:
            self._motor.motor.close()

        if self._lockin is not None:
            self._lockin.ser.close()
            
        self._measurement_thread.quit()
        self._measurement_thread.wait()
