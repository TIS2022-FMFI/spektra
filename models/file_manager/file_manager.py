import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileSystemModel

from settings import Settings




class FileManager(QFileSystemModel):
    def __init__(self, root_path=None, file_extension=Settings.DATA_FILE_EXTENSION, parent=None):
        super(FileManager, self).__init__(parent=parent)
        self._set_root_path(root_path)
        super(FileManager, self).setRootPath(
            self.root_file_path)  # to automatically refresh the view when new files are added
        self.file_extension = file_extension

    def _set_root_path(self, root_path):
        self.root_file_path = root_path
        if root_path is None or not os.path.exists(root_path):
            self.root_file_path = os.path.join(os.getcwd(), Settings.SAVED_MEASUREMENTS_FOLDER)
            if not os.path.exists(self.root_file_path):
                os.makedirs(self.root_file_path)

    def flags(self, index) -> Qt.ItemFlag:
        return super(FileManager, self).flags(index) | Qt.ItemFlag.ItemIsDragEnabled

    def change_current_directory(self, directory):
        self._set_root_path(directory)
        return self.index(self.root_file_path)