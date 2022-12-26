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
        
        self.running = false

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
            STEP_DELAY = 0.16
            SLEEP_TIME = 0.5
            DISTANCE = self.getDistance(end)
            NO_ATOMIC_STEPS = self.getSteps(DISTANCE)
            NO_STEPS = NO_ATOMIC_STEPS // step_size

            print(f"dist: {DISTANCE} \natomic steps: {NO_ATOMIC_STEPS} \nsteps: {NO_STEPS}")

            for iteration in range(NO_STEPS):
                self._motor.moveForward(step_size)

                print(f"iter: {iteration}")

                time.sleep(STEP_DELAY * step_size)
                measured_value = m._lockin.precitaj_hodnotu().decode('UTF-8')
                actual_position = (self.position + self._elem.krokyNaVlna((iteration + 1) * step_size))
                print(f"pos: {actual_position:.3f} measurement: {measured_value}")
                time.sleep(SLEEP_TIME)

            time.sleep(SLEEP_TIME)
            self.position = actual_position 
    

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

            res = (end-start)/steps
            self._elem.krok = res
            
                
    def initialization(self, p):
        self.position = p
        

    def save_calibration(self):
        self._elem.save()
        
    
    def getDistance(self, stop):
        return round(stop - self.position, 2)

    
    def getSteps(self, distance):
        return self._elem.vlnaNaKroky(abs(distance))
        
    
    @QtCore.Slot()
    def stop(self):
        # TODO: implement method to stop measurement. Checks if measurement is running and if so, stops it and emits signal that state changed
        self.running = false

    def exit(self):
        if self._motor is not None:
            self._motor.motor.close()

        if self._lockin is not None:
            self._lockin.ser.close()
            
        self._measurement_thread.quit()
        self._measurement_thread.wait()
