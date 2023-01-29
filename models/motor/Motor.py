from time import sleep
from serial import Serial, EIGHTBITS, STOPBITS_ONE, PARITY_NONE


class Motor:
    STEP_DELAY = 0.16
    FORWARD_PREPARATION_STEPS = 40
    MIN_STEPS_FOR_ACCELERATED_MOVEMENT = 201

    def __init__(self, delay=0.05):
        '''
        initializes stepped motor object
        @param port_name: name of port, where motor is connected
        @param delay: time delay for connection sending
        '''
        self.delay = delay
        self.motor = None
        self.connected = False

    def connect(self, comport):
        self.motor = Serial(comport, 9600, EIGHTBITS, PARITY_NONE, STOPBITS_ONE, timeout=0.5)
        self.connected = True

    def move_forward(self, steps):
        '''
        move motor forward
        @param steps: number of steps
        @return moving time for given steps
        '''
        return self.move(steps, "F")

    def move_reverse(self, steps, prepare_forward_movement=True):
        '''
        move motor reverse (with overlap if more that SPEED_UP_STEP_BORDER number of steps)
        @param steps: number of steps
        @return moving time for given steps
        '''
        if prepare_forward_movement:
            sleep(self.move(steps + self.FORWARD_PREPARATION_STEPS, "R"))
            return self.move(self.FORWARD_PREPARATION_STEPS, "F")
        return self.move(steps, "R")

    def move(self, steps, direction):
        '''
        move motor in given direction (with speed up if more that SPEED_UP_STEP_BORDER number of steps)
        @param steps: number of steps
        @return moving time for given steps
        '''
        command = f"!{steps:04d}{direction}"

        for char in command:
            log = self.motor.write(char.encode())
            sleep(self.delay)
            print(log, end=' ')

        if steps >= self.MIN_STEPS_FOR_ACCELERATED_MOVEMENT:
            moving_time = (12220 + (steps - 130) * 30)/1000
        else:
            moving_time = steps * self.STEP_DELAY

        return moving_time

