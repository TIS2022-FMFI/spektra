from PySide6.QtCore import Signal, QObject

from models.file_manager.file_manager import FileManager


class FileManagerController(QObject):
    log_s = Signal(int, str, bool)
    #tu budem mat vsetky parametre hlavicky
    #vytvorim si settery na nastavenie konkretnej
    '''
    casti hlavicky - tp nereisim to kontrolery nastavia
    pootom ked sa da ze start meranie tal sa skontroluje ze je 
    cela hlavicka vyplnena
    a potom sa vytvori subor 
    '''

    def __init__(self, key):
        super(FileManagerController, self).__init__()
        self._file_manager = FileManager()
        self._key = key

    def get_model(self, key):
        if key == self._key:
            return self._file_manager
        else:
            raise ValueError("Invalid key")
