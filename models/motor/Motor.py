import time
import serial
 
class Motor:
    step_delay = 0.16
    MOVING_CONSTANT = 100
    
    def __init__(self, portName, delay=0.05):
        self.delay = delay
        self.motor = serial.Serial(portName, 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout=0.5)
        
    def moveForward(self, steps):
        self.move(steps, "F")

    def moveReverse(self, steps):
        time.sleep(self.move(steps + self.MOVING_CONSTANT, "R"))
        self.move(self.MOVING_CONSTANT, "F")
        
    def move(self, steps, direction):
        command = f"!{steps:04d}{direction}"
 
        for char in command:
            log = self.motor.write(char.encode())
            time.sleep(self.delay)
            print(log)

        if steps > 200:
            t = (12220 + (steps - 130) * 30)/1000
        else:
            t = steps * self.step_delay

        return t

    def setDelay(self, delay):
        self.delay = delay

    def getDelay(self, delay):
        return self.delay
 

    
