from PySide6.QtCore import QObject

from models.motor.Motor import Motor


class MotorController(QObject):
    def __init__(self, key):
        # TODO implement motor controller - David -> due to 21.11.2022
        super(MotorController, self).__init__()
        self._key = key
        self._motor = Motor()

    def get_model(self, key):
        if key == self._key:
            return self._motor
        else:
            raise ValueError("Invalid key")
