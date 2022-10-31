from PySide6.QtCore import QObject

from models.lockin.lockin import Lockin


class MeasurementController(QObject):
    def __init__(self, key):
        # TODO implement measurement controller (Lockin) - Sebo -> due to 21.11.2022
        super(MeasurementController, self).__init__()
        self._key = key
        self._lockin = Lockin()

    def get_model(self, key):
        if key == self._key:
            return self._lockin
        else:
            raise ValueError("Invalid key")
