from dataclasses import dataclass
import math
@dataclass
class CalibrationData:
    name: str
    spectral: float
    G: float
    correction: float
    multiplier: float
    min_angle: float
    max_angle: float
    start_pos: float
    end_pos: float
    steps: int

class DisperseElement:
    defaultMinAngle = 16
    defaultMaxAngle = 28
    
    def __init__(self, name=None):
        '''
        initializes disperse element object
        @param name: the name of particular disperse element
        '''
        self.minAngle = self.defaultMinAngle
        self.maxAngle = self.defaultMaxAngle
        self.name = name
        self.angleDelta = None

        self.constant = 2000
        self.riadky_per_mm = None
        self.correction = 0
        self.spectral_order = 1

        if name is not None:
            self._load()

    def _load(self):
        '''
        load parameters of disperse element
        @return return true if load successful, else false
        '''
        try:
            with open(f'models/elements/{self.name}.txt') as subor:
                self.angleDelta = float(subor.readline().strip())
                self.steps = int(subor.readline().strip())
                self.minAngle = float(subor.readline().strip())
                self.maxAngle = float(subor.readline().strip())
                self.constant = float(subor.readline().strip())
                self.riadky_per_mm = float(subor.readline().strip())
                self.correction = float(subor.readline().strip())
                self.spectral_order = int(subor.readline().strip())
        except FileNotFoundError:
            print('Info o mriezke nenajdene')
            return False
        except ValueError:
            print('Zly format ulozenej mriezky')
            return False
        return True

    def _save(self):
        '''
        save disperse element object
        '''
        if self.angleDelta is not None:
            with open(f'models/elements/{self.name}.txt', 'w') as subor:
                subor.write(str(self.angleDelta) + '\n')
                subor.write(str(self.steps) + '\n')
                subor.write(str(self.minAngle) + '\n')
                subor.write(str(self.maxAngle) + '\n')
                subor.write(str(self.constant) + '\n')
                subor.write(str(self.riadky_per_mm) + '\n')
                subor.write(str(self.correction) + '\n')
                subor.write(str(self.spectral_order) + '\n')

    def save_calibration(self, data):
        '''
        save calibration data of disperse element object
        @param data: calibration data
        '''
        self.minAngle = data.min_angle
        self.maxAngle = data.max_angle
        self.name = data.name
        self.angleDelta = data.end_pos - data.start_pos
        self.steps = int(data.steps)

        self.constant = data.multiplier
        self.riadky_per_mm = data.G
        self.correction = data.correction
        self.spectral_order = int(data.spectral)

        self._save()
        
    def canMoveTo(self, ang):
        '''
        inform about possibility to move at given angle
        @param ang: angle, where to move
        '''
        return self.maxAngle >= ang >= self.minAngle
    
class Grating(DisperseElement):
    def angleToSteps(self, ang):
        '''
        transform angle to number of steps
        @param ang: angle to transform
        @return: resulting number of steps
        '''
        return int(ang * self.steps / self.angleDelta)

    def stepsToAngle(self, steps):
        '''
        transform number of steps to angle
        @param steps: steps to transform
        @return: resulting angle
        '''
        return steps * self.angleDelta / self.steps

    def angleToWavelength(self, ang):
        '''
        transform angle value to wave length
        @param ang: angle to transform
        @return: resulting wavelength (in Angstrom)
        '''
        rad = ((ang - self.correction) * math.pi) / 180
        riadky_per_m = self.riadky_per_mm / 1000

        prva_cast = self.constant / (self.spectral_order * riadky_per_m)
        wavelength = prva_cast * math.sin(rad)

        return wavelength * 10

    def wavelengthToAngle(self, angstroms):
        '''
        transform angle to number of steps
        @param ang: angle (in Angstrom) to transform
        @return: resulting wavelength
        '''
        nm = angstroms / 10
        riadky_per_m = self.riadky_per_mm / 1000
        rad = math.asin((nm * self.spectral_order * riadky_per_m) / self.constant)

        return rad * 180 / math.pi + self.correction
        
class Hranol(DisperseElement):
    def __new__(self):
        '''
        placeholder for future implementation (optional)
        '''
        raise NotImplementedError
