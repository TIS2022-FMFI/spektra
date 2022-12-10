'''
465645
b_0 = 0.10270493630650668
b_1 = 0.09962097363739941
[0.09962097 0.10270494]
b[1] * xx[i] + b[0]
'''

'''
456039
b_0 = 0.05135246815325334        
b_1 = 0.049810486818699706
[0.04981049 0.05135247]
'''
class Grid:
    def __init__(self):
        self.a = 0
        self.b = 0

    def getWaveLength(self, angle):
        return self.a * angle + self.b


class Grid465645(Grid):
    def __init__(self):
        super(Grid465645, self).__init__()
        self.a = 0.09962097363739941
        self.b = 0.10270493630650668


class Grid456039(Grid):
    def __init__(self):
        super(Grid456039, self).__init__()
        self.a = 0.049810486818699706
        self.b = 0.05135246815325334