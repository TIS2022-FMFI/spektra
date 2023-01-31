from serial import Serial, PARITY_NONE
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
        Pripoji sa mediator cez seriovy port
        @param port:
        @return: None
        """
        ...

    @abstractmethod
    def read_value(self):
        """
        Citanie nameraneho napatia
        @return: float
        """
        ...

    @abstractmethod
    def get_command(self, data_type, command):
        """
        Vseobecna metoda na posielanie commandu na mediator a citanie hodnoty
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
        getter = self.get_command_or_method_map[setting]

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
        self.serial_connection = Serial(port, 9600, 8, PARITY_NONE, 2, timeout=0.5)

    def get_command(self, data_type, command):
        """
        Dostane typ, ktory ma vraciat a command, ktory vyziada nejaku hodnotu
        @param data_type: type
        @param command: str
        @return: data_type
        """
        return data_type(self.rcom(command))

    def rcom(self, command, read=True):
        """
        Command upraveny do potrebnej podoby pre sr510
        @param command: str
        @param read: bool urcujuci ci treba citat odpoved a nasledne vratit danu hodnotu
        @return:
        """
        command += '\r'
        self.serial_connection.write(command.encode())
        if read:
            return self.serial_connection.readline()[:-1]

    def set_gain(self, new_gain):
        """
        nastavit senzitivtu s obmedzenim
        @param new_gain: int
        @return: None
        """
        if self.lowest_auto_settable_gain <= new_gain <= 24:
            self.rcom(f'G {new_gain}', False)

    def read_value(self):
        """
        Poziadaj o precitanie napatia
        @return: float
        """
        return float(self.rcom('Q'))


class Metex(Mediator):
    def connect(self, port):
        raise NotImplementedError

    def read_value(self):
        raise NotImplementedError

    def get_command(self, data_type, command):
        raise NotImplementedError
