import time
import serial
 
class Motor:
    STEP_DELAY = 0.16
    MOVING_CONSTANT = 40
    
    def __init__(self, portName, delay=0.05):
        '''
        initializes stepped motor object
        @param port_name: name of port, where motor is connected
        @param delay: time delay for connection sending
        '''
        self.delay = delay

        try:
            self.motor = serial.Serial(portName, 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout=0.5)
        except:
            print('MOTOR NOT CONNECTED')

    def moveForward(self, steps):
        '''
        move motor forward
        @param steps: number of steps
        @return moving time for given steps
        '''
        return self.move(steps, "F")

    def moveReverse(self, steps):
        '''
        move motor reverse (with overlap if more that SPEED_UP_STEP_BORDER number of steps)
        @param steps: number of steps
        @return moving time for given steps
        '''
        added_steps = self.MOVING_CONSTANT if steps > 200 else 0            
        time.sleep(self.move(steps + added_steps, "R"))
        return self.move(added_steps, "F")
        
    def move(self, steps, direction):
        '''
        move motor in given direction (with speed up if more that SPEED_UP_STEP_BORDER number of steps)
        @param steps: number of steps
        @return moving time for given steps
        '''
        command = f"!{steps:04d}{direction}"
 
        for char in command:
            log = self.motor.write(char.encode())
            time.sleep(self.delay)
            print(log)

        if steps > 200:
            moving_time = (12220 + (steps - 130) * 30)/1000
        else:
            moving_time = steps * self.STEP_DELAY

        return moving_time

    def setDelay(self, delay):
        self.delay = delay

    def getDelay(self, delay):
        '''
        getter method
        @return connection delay constant
        '''
        return self.delay
 

    
