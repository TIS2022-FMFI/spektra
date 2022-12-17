from PySide6.QtCore import QObject

from models.data_processing.data_processing import data_processing


class GraphController(QObject):
    def __init__(self, key):
        # TODO implement graph controller - Lucka -> due to 21.11.2022
        super(GraphController, self).__init__()
        self._key = key
        self._data_processing = data_processing()

    def get_model(self, key):
        if key == self._key:
            return self._data_processing
        else:
            raise ValueError("Invalid key")
