class DisperseElement:
    def __init__(self, nazov):
        self.nazov = nazov
        self.kalib = self.load()

    def IsCalib(self):
        return self.kalib
    
class Grating(DisperseElement):
    def __init__(self, nazov):
        self.krok = None
        super().__init__(nazov)
    def canMove(self, pos):
        return self.maxValue > pos > self.minValue
    
    def load(self):
        try:
            with open(f'elements/{self.nazov}.txt') as subor:
                self.krok = float(subor.readline().strip())
                self.minValue = 16
                self.maxValue = 28
        except FileNotFoundError:
            return False
        return True

    def save(self):
        if self.krok is not None:
            with open(f'elements/{self.nazov}.txt', 'w') as subor:
                subor.write(str(self.krok))
                
    def res(self, start, end, kroky):
        self.krok = (end-start)/kroky
        return self.krok
        
    def posun(self, kroky):
        return self.krok * kroky


    def vlnaNaKroky(self, d):
        return int(d / self.krok)

    def krokyNaVlna(self, pocet_krokov, round_val=3):
        return round(pocet_krokov * self.krok, round_val)

class Hranol(DisperseElement):
    def f(self):
        pass
