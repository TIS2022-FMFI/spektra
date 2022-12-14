import serial
import time
import serial.tools.list_ports
import lockin
import motor
from disp_elem import Grating

class Measurement:
    _motor = None
    _lockin = None
    _elem = None
    
    def __init__(self, lockin_type='sr510'):
        self.poloha = None
        element_nazov = 'ms732' #z gui
        
        print('Dostupne COM porty:')
        availableComPorts = serial.tools.list_ports.comports()
        for acp in availableComPorts:
               print(acp.name + '/'+ acp.description)
               
        if Measurement._lockin is None:
            Measurement._lockin = lockin.SR510()

        if Measurement._motor is None:
            Measurement._motor = motor.Motor('COM4')

        if Measurement._elem is None:
            Measurement._elem = Grating(element_nazov)
            if self._elem.IsCalib() is False:
                print('kal nexist. treba kalibrovat')

##        self.inicializuj(float(input('zadaj inicial. pol.: ')))

    def inicializuj(self, p):
        self.poloha = p

    def posunReverse(self, kroky):
        self._motor.moveReverse(kroky)

    def posunForward(self, kroky):
        self._motor.moveForward(kroky)

    def kalib(self, kroky=100):
        start = self.poloha
        self._motor.moveForward(kroky)

        end = float(input('zadaj polohu: '))

        res = (end-start)/kroky
        print('kroky', res)

        self._elem.krok = res


    def kalib_manual(self):
        start = float(input('zadaj start polohu: '))
        vstup = None
        kroky = 0
        while True:
            vstup = int(input('forward: '))
            if vstup == 0:
                break
            kroky += vstup
            self._motor.moveForward(vstup)

        if kroky <= 0:
            return
        
        self.poloha = end = float(input('zadaj konecnu polohu: '))

        print(self._elem.res(start, end, kroky))
        
    def save_kalib(self):
        self._elem.save()

    def getDistance(self, stop):
        return round(stop - self.poloha, 2)

    def getSteps(self, distance):
        return self._elem.vlnaNaKroky(abs(distance))

    def meraj(self, end=24.7, step_size=4):
        self._lockin.prepare()

        STEP_DELAY = 0.16
        SLEEP_TIME = 0.5
        DISTANCE = self.getDistance(end)
        NO_ATOMIC_STEPS = self.getSteps(DISTANCE)
        NO_STEPS = NO_ATOMIC_STEPS//step_size

        print(f"vzd: {DISTANCE} \nkroky atomicke: {NO_ATOMIC_STEPS} \nkroky: {NO_STEPS}")

        for iteration in range(NO_STEPS):
            self._motor.moveForward(step_size)
            print(f"iter: {iteration} steps: {NO_STEPS}")

            time.sleep(STEP_DELAY * step_size)
            measured_value = m._lockin.precitaj_hodnotu().decode('UTF-8')
            print(f"pos: {(self.poloha+ self._elem.krokyNaVlna((iteration+1)*step_size)):.3f} measurement: {measured_value}")
            time.sleep(SLEEP_TIME)
            
        time.sleep(SLEEP_TIME)
        self.poloha = None

    def posunNaPoz(self, stop):
        if self.poloha is None or self.poloha == stop or not self._elem.canMove(stop):
            return
        
        vzdialenost = stop - self.poloha
        kroky = self._elem.vlnaNaKroky(abs(vzdialenost))
        print("pocet ktokov", kroky)
        potvrdenie = input("potvrd kroky:")
        if potvrdenie == "suhlasim":
            self.poloha = stop
            if vzdialenost > 0:
                self._motor.moveForward(kroky)
            else:
                self._motor.moveReverse(kroky)

##    def meraj2(self, start, end):
##        lockin.prepare()
##
##        krok_delay = 0.16
##        kroky = 100
##           
##        motor.move(kroky, 'F')
##    ##    out = motor.read(7)
##    ##    print out
##        time.sleep(krok_delay * kroky)
##        lockin.write(b'Q\r')
##        print(lockin.readline())
##        time.sleep(0.5)
    
    def __enter__(self):
        return self

    def __exit__(self, *args):
        print(args)
        self._motor.motor.close()
        self._lockin.ser.close()




if __name__ == '__main__':
    with Measurement() as m:
        pass
##        m._motor.move(2, 'F')
##        m._motor.moveForward(1500)
##        m._motor.moveReverse(1500)

##        m.kalib_manual()
##        m.inicializuj(24.6)
##        m.meraj()
##        m.posunForward(1000)
##        m.posunReverse(1000)

        
##        while True:
##            m.posunNaPoz(float(input('zadaj polohu')))

