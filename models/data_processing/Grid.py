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