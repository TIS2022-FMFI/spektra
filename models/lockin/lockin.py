import serial

from models.lockin.lockin_data import lockin_data
from models.lockin.constants import *

class Lockin:
    def __init__(self, name, port):
        ld = lockin_data[name]
        sc = ld['serial_connection']
        self.ser = None
        if sc:
            self.ser = serial.Serial(port, *sc.getsettings(), timeout=sc.timeout)

        self.name = name
        self.gain_values = ld['gain']
        self.pre_time_const = ld[PRE_TIME_CONST]
        self.post_time_const = ld[POST_TIME_CONST]
        self.cur_gain_index = None

    def current_gain_value(self):
        return self.gain_values[self.cur_gain_index]
    def rcom(self, com, read=False):
        """raw command"""
        if self.ser is not None:
            com += '\r'
            self.ser.write(com.encode())
            if read:
                return self.ser.readline()[:-1]

    def read_setting(self, setting):
        if setting == PRE_TIME_CONST:
            return self.get_pre_time_const()
        elif setting == POST_TIME_CONST:
            return self.get_post_time_const()
        elif setting == PHASE_SHIFT:
            return self.get_phase()
        elif setting == REFERENCE_FREQUENCY:
            return self.get_ref_frequency()
        elif setting == BANDPASS_FILTER:
            return self.get_bandpass_filter()

        raise Exception("Wrong setting")

class SR510(Lockin):
    def __init__(self, port):
        super().__init__('sr510', port)

    def lower_gain(self):
        self.cur_gain_index += 1
        self.rcom(f'G {self.cur_gain_index}')

    def higher_gain(self):
        if self.cur_gain_index >= 12:
            self.cur_gain_index -= 1
            self.rcom(f'G {self.cur_gain_index}')

    def prepare(self):
        self.rcom('Q', True)  # Prve citanie sa zahodi
        self.cur_gain_index = self.get_gain()

    # T m {,n} The T command sets and reads the status of the time constants.
    # If m is "1", the pre time constant is selected
    # if m is "2", the post time constant is selected.
    def get_pre_time_const(self):
        return self.pre_time_const[int(self.rcom('T 1', True))]

    def get_post_time_const(self):
        return self.post_time_const[int(self.rcom('T 2', True))]

    def get_gain(self):
        # G {n} If n is absent, the gain setting is returned.
        return int(self.rcom('G', True))  # uvodne nastavenie citlivosti

    def set_gain(self, n):
        if 11 <= n <= 24:
            self.rcom(f'G {n}')
            self.cur_gain_index = n

    def read_value(self):
        return float(self.rcom('Q', True))
    def get_auto_offset(self):
        return int(self.rcom('A', True))

    def get_bandpass_filter(self):
        return int(self.rcom('B', True))

    def get_refLCD_display(self):
        return int(self.rcom('C', True))

    def get_dynamic_reserve(self):
        return int(self.rcom('D', True))

    def get_ref_frequency(self):
        return float(self.rcom('F', True))

    def get_preamp_status(self):
        return int(self.rcom('H', True))

    def get_phase(self):
        return float(self.rcom('P', True))
