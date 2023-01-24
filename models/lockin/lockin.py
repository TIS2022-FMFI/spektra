import time
import serial
from .lockin_data import lockin_data
 
class Lockin:
    def __init__(self, name):
        ld = lockin_data[name]
        sc = ld['serial_connection']
        if sc:
            pass
            #####ODKOMENTOVAT A ODSTRANIT PASS
            #self.ser = serial.Serial(*sc.getsettings(), timeout=sc.timeout)
 
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
        '''Stuff that needs to be done before using lockin'''
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
        return 100 #not sure how
 
class SR510(Lockin):
    def __init__(self):
        super().__init__('sr510')
 
    def lower_gain(self):
        self.g += 1
        self.ser.write((f'G {self.g}' + '\r').encode())
 
    def higher_gain(self):
        if self.g >= 12:
            self.g -= 1
            self.ser.write((f'G {self.g}' + '\r').encode())
 
    def prepare(self):
        self.ser.write(b'Q\r') #Prve citanie sa zahodi 
        self.ser.readline()
 
        self.g = self.get_gain()
 
    #T m {,n} The T command sets and reads the status of the time constants.
    #If m is "1", the pre time constant is selected
    #if m is "2", the post time constant is selected.
    def get_pre_time_const(self):
        self.ser.write(b'T 1\r') #uvodna casova konstanta T1
        return int(self.ser.readline()[:-1])
 
    def get_post_time_const(self):
        self.ser.write(b'T 2\r') #uvodna casova konstanta T2
        return int(self.ser.readline()[:-1])
 
    def get_gain(self):
        #G {n} If n is absent, the gain setting is returned.
        self.ser.write(b'G\r') #uvodne nastavenie citlivosti
        return int(self.ser.readline()[:-1])
 
    def precitaj_hodnotu(self):
        self.ser.write(b'Q\r') #prikaz, aby sa poslal udaj
        return self.ser.readline()[:-1] #nacitana hodnota bez CR na konci
 
 
##if __name__ == '__main__':
##    lockin = SR510()
##    lockin.prepare()
