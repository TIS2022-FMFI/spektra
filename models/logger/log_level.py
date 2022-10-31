from PySide6.QtGui import QColor
from models.logger.constants import COLORS, STR, ALL


class LogLevel:
    def __init__(self, level: int):
        if level not in ALL:
            raise ValueError('Invalid log level')
        self.level = level
        self._str = STR[level]
        self._color = QColor(*COLORS[level])

    def __str__(self):
        return self._str

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, LogLevel):
            return self.level == other.level
        elif other in ALL:
            return self.level == other
        else:
            raise TypeError('Invalid type')

    def __lt__(self, other):
        if isinstance(other, LogLevel):
            return self.level > other.level
        elif other in ALL:
            return self.level > other
        else:
            raise TypeError('Invalid type')

    def __gt__(self, other):
        if isinstance(other, LogLevel):
            return self.level < other.level
        elif other in ALL:
            return self.level < other
        else:
            raise TypeError('Invalid type')

    def __le__(self, other):
        if isinstance(other, LogLevel):
            return self.level >= other.level
        elif other in ALL:
            return self.level >= other
        else:
            raise TypeError('Invalid type')

    def __ge__(self, other):
        if isinstance(other, LogLevel):
            return self.level <= other.level
        elif other in ALL:
            return self.level <= other
        else:
            raise TypeError('Invalid type')

    def color(self):
        return self._color
