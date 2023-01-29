import time
import serial
 
class Motor:
    STEP_DELAY = 0.16
    MOVING_CONSTANT = 100
    MIN_STEPS_FOR_ACCELERATED_MOVEMENT = 201
    
    def __init__(self, portName, delay=0.05):
        self.delay = delay
        self.motor = None
        self.connected = False

        try:
            self.motor = serial.Serial(portName, 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout=0.5)
            self.connected = True
        except Exception as e:
            print(e)
            print('MOTOR NOT CONNECTED')

    def moveForward(self, steps):
        return self.move(steps, "F")

    def moveReverse(self, steps):
        time.sleep(self.move(steps + self.MOVING_CONSTANT, "R"))
        self.move(self.MOVING_CONSTANT, "F")
        
    def move(self, steps, direction):
        command = f"!{steps:04d}{direction}"
 
        for char in command:
            log = self.motor.write(char.encode())
            time.sleep(self.delay)
            print(log, end=' ')

        if steps >= self.MIN_STEPS_FOR_ACCELERATED_MOVEMENT:
            moving_time = (12220 + (steps - 130) * 30)/1000
        else:
            moving_time = steps * self.STEP_DELAY

        return moving_time
    
