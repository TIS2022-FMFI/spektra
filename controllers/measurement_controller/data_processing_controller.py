from PySide6.QtCore import QObject, Signal

from models.data_processing.dataProcessing import DataProcessing


class DataProcessingController(QObject):
    settings_changed_s = Signal(dict)

    def __init__(self, key, ):
        super(DataProcessingController, self).__init__()
        self._key = key
        self._data_processing = DataProcessing()

    def get_model(self, key):
        if key == self._key:
            return self._data_processing
        else:
            raise ValueError("Invalid key")

    def set_settings(self, settings):
        self._data_processing.set_settings(settings)
        self.settings_changed_s.emit(settings)


