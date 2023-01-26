class DisperseElement:
    defaultMinAngle = 16
    defaultMaxAngle = 28
    
    def __init__(self, name):
        self.minAngle = self.defaultMinAngle
        self.maxAngle = self.defaultMaxAngle
        self.name = name
        self.angleDelta = None
        
        self.kalib = self.load()
        
    def IsCalib(self):
        return self.kalib

    def load(self):
        try:
            with open(f'models/elements/{self.name}.txt') as subor:
                self.angleDelta = int(subor.readline().strip())
                self.steps = int(subor.readline().strip())
                self.minAngle = int(subor.readline().strip())
                self.maxAngle = int(subor.readline().strip())
                
        except FileNotFoundError:
            print('info o mriezke nenajdene')
            return False
        return True

    def save(self):
        if self.angleDelta is not None:
            with open(f'models/elements/{self.name}.txt', 'w') as subor:
                subor.write(str(self.angleDelta) + '\n')
                subor.write(str(self.steps) + '\n')
                subor.write(str(self.minAngle) + '\n')
                subor.write(str(self.maxAngle) + '\n')

    def angleToSteps(self, ang):
        pass

    def stepsToAngle(self, steps):
        pass

    def canMove(self, cur_ang):
        return self.maxAngle >= cur_ang >= self.minAngle
    
class Grating(DisperseElement):
    def angleToSteps(self, ang):
        return int(ang * self.steps / self.angleDelta)

    def stepsToAngle(self, steps):
        return steps * self.angleDelta / self.steps

    def calibrateAngStep(self, start, end, steps):
        self.angleDelta = end - start
        self.steps = steps
    def angleToWavelength(self, ang):
        pass
        
class Hranol(DisperseElement):
    def angleToWavelength(self, ang):
        pass
    
