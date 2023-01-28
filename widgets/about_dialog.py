from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QGridLayout

from settings import Settings


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        title = QLabel("O programe")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        version = QLabel(f"Verzia {Settings.VERSION}")
        version.setStyleSheet("font-size: 16px;")
        repository = QLabel("GitHub: <a href=https://github.com/TIS2022-FMFI/spektra/>")
        repository.setStyleSheet("font-size: 16px;")
        repository.setOpenExternalLinks(True)
        description = QLabel(Settings.DESCRIPTION)
        description.setStyleSheet("font-size: 13px;")
        description.setWordWrap(True)
        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(version)
        layout.addWidget(repository)
        layout.addWidget(description)
        layout.addStretch()
        self.setLayout(layout)
        self.setWindowTitle("O programe")
        self.setFixedSize(400, 200)
