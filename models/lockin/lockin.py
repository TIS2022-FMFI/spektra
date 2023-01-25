import serial
from models.lockin.lockin_data import lockin_data


class Lockin:
    def __init__(self, name):
        ld = lockin_data[name]
        sc = ld['serial_connection']
        self.ser = None
        if sc:
            try:
                self.ser = serial.Serial(*sc.getsettings(), timeout=sc.timeout)
            except:
                print('no locking connected')

        self.name = name
        self.gain = ld['gain']
        self.pre_time_const = ld['pre_time_const']
        self.post_time_const = ld['post_time_const']
        self.g = None

    def current_gain(self):
        return self.gain[self.g]

    def lower_gain(self):
        self.g += 1
        input('Zmensi zisk a stlac klavesu pre pokracovanie')

    def higher_gain(self):
        self.g -= 1
        input('Zvacsi zisk a stlac klavesu pre pokracovanie')

    def prepare(self):
        """Stuff that needs to be done before using lockin"""
        self.g = self.get_gain()

    def get_pre_time_const(self):
        pre_t = float(input('Zadaj casovu konstantu 1'))
        return self.pre_time_const.index(pre_t)

    def get_post_time_const(self):
        post_t = float(input('Zadaj casovu konstantu 2'))
        return self.pre_time_const.index(post_t)

    def get_gain(self):
        cur_gain = float(input('Zadaj nastavenu citlivost'))
        return self.gain.index(cur_gain)

    def set_gain(self, gain_index):
        input(f'Nastav {self.gain[gain_index]} a potvrd')

    def precitaj_hodnotu(self):
        return 100  # not sure how

    def rcom(self, com, read=False):
        """raw command"""
        if self.ser is not None:
            com += '\r'
            self.ser.write(com.encode())
            if read:
                return self.ser.readline()[:-1]


class SR510(Lockin):
    def __init__(self):
        super().__init__('sr510')

    def lower_gain(self):
        self.g += 1
        self.rcom(f'G {self.g}')

    def higher_gain(self):
        if self.g >= 12:
            self.g -= 1
            self.rcom(f'G {self.g}')

    def prepare(self):
        self.rcom('Q', True)  # Prve citanie sa zahodi
        self.g = self.get_gain()

    # T m {,n} The T command sets and reads the status of the time constants.
    # If m is "1", the pre time constant is selected
    # if m is "2", the post time constant is selected.
    def get_pre_time_const(self):
        return int(self.rcom('T 1', True))  # uvodna casova konstanta T1

    def get_post_time_const(self):
        return int(self.rcom('T 2', True))  # uvodna casova konstanta T2

    def get_gain(self):
        # G {n} If n is absent, the gain setting is returned.
        return int(self.rcom('G', True))  # uvodne nastavenie citlivosti

    def set_gain(self, n):
        if 11 <= n <= 24:
            self.rcom(f'G {n}')
            self.g = n

    def precitaj_hodnotu(self):
        return float(self.rcom('Q', True))

    def get_auto_offset(self):
        return int(self.rcom('A', True))

    def set_auto_offset(self, n):
        self.rcom(f'A {n}')

    def get_bandpass_filter(self):
        return int(self.rcom('B', True))

    def set_bandpass_filter(self, n):
        self.rcom(f'B {n}')

    def get_refLCD_display(self):
        return int(self.rcom('C', True))

    # C 1 = show phase settings
    # C 0 = show reference frequency
    def set_refLCD_display(self, n):
        self.rcom(f'C {n}')

    def get_dynamic_reserve(self):
        return int(self.rcom('D', True))

    def set_dynamic_reserve(self, n):
        self.rcom(f'D {n}')

    def get_ref_frequency(self):
        return float(self.rcom('F', True))

    def get_preamp_status(self):
        return int(self.rcom('H', True))

    def get_phase(self):
        return float(self.rcom('P', True))

    def set_phase(self, v):
        self.rcom(f'P {v}')
