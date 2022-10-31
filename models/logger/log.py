from datetime import datetime
from models.logger.log_level import LogLevel


class Log:
    def __init__(self, message: str, level: LogLevel):
        self.message = message
        self.level = level
        self.timestamp = datetime.now()
        self.next = None
        self.previous = None

    def __str__(self):
        return f'{self.timestamp.strftime("%d. %m. %Y %H:%M:%S")} - {self.level}: {self.message}'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.timestamp == other.timestamp and self.level == other.level and self.message == other.message

    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def __gt__(self, other):
        return self.timestamp > other.timestamp

    def __le__(self, other):
        return self.timestamp <= other.timestamp

    def __ge__(self, other):
        return self.timestamp >= other.timestamp

    def __ne__(self, other):
        return not self == other
