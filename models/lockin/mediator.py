from serial import Serial, PARITY_NONE, EIGHTBITS, STOPBITS_TWO
from abc import ABC, abstractmethod

from .constants import *


class Mediator(ABC):
    def __init__(self, port):
        self.can_set_gain = False
        self.lowest_auto_settable_gain = None
        self.serial_connection = None
        self.get_command_or_method_map = {}
        self.connect(port)

    @abstractmethod
    def connect(self, port):
        """
        Method that connects to passed comport
        @param port:
        @return: None
        """
        ...

    @abstractmethod
    def read_value(self):
        """
        Read voltage
        @return: float
        """
        ...

    @abstractmethod
    def get_command(self, data_type, command):
        """
        Sends command over serial connection and returns the returned value as type data_type
        @param data_type: type
        @param command: str
        @return:
        """
        ...

    def disconnect(self):
        if self.serial_connection is not None:
            self.serial_connection.close()

    def is_setting_gain_possible(self):
        return self.can_set_gain

    def read_setting(self, setting):
        """
        Read passed setting from lockin if possible
        @param setting:
        @return:
        """
        if setting in self.get_command_or_method_map:
            getter = self.get_command_or_method_map[setting]
        else:
            raise Exception(f"Reading setting '{setting}' is not supported")

        if type(getter) is tuple:
            data_type, command = getter
            return self.get_command(data_type, command)
        return getter()


class SR510(Mediator):
    def __init__(self, port):
        super().__init__(port)
        self.can_set_gain = True
        self.lowest_auto_settable_gain = LOWEST_AUTO_SETTABLE_GAIN_DEFAULT
        self.get_command_or_method_map = {
            GAIN: (int, 'G'),
            PRE_TIME_CONST: (int, 'T 1'),
            POST_TIME_CONST: (int, 'T 2'),
            PHASE_SHIFT: (float, 'P'),
            REFERENCE_FREQUENCY: (float, 'F'),
            BANDPASS_FILTER: (int, 'B'),
            LINE_FILTER: (int, 'L 1'),
            LINE2_FILTER: (int, 'L 2'),
            DYNAMIC_RESERVE: (int, 'D')
        }

    def connect(self, port):
        self.serial_connection = Serial(port, 9600, EIGHTBITS, PARITY_NONE, STOPBITS_TWO, timeout=0.5)

    def get_command(self, data_type, command):
        return data_type(self.rcom(command))

    def rcom(self, command, read=True):
        """
        Command converted to needed format to send over serial connection
        @param command: str
        @param read: bool - wait for return value from serial connection ?
        @return:
        """
        command += '\r'
        self.serial_connection.write(command.encode())
        if read:
            return self.serial_connection.readline()[:-1]

    def set_gain(self, new_gain):
        """
        Set sensitivity
        @param new_gain: int
        @return: true/false whether gain was changed
        """
        if self.lowest_auto_settable_gain <= new_gain <= 24:
            self.rcom(f'G {new_gain}', False)
            return True
        return False

    def read_value(self):
        return float(self.rcom('Q'))


class Metex(Mediator):
    def connect(self, port):
        raise NotImplementedError

    def read_value(self):
        raise NotImplementedError

    def get_command(self, data_type, command):
        raise NotImplementedError
