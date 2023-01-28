from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QGridLayout, QMessageBox

from settings import Settings


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        version = QLabel(f"Verzia {Settings.VERSION}")
        version.setStyleSheet("font-size: 16px;")
        repository = QLabel(f"<a href={Settings.REPOSITORY_URL}>Github repozitár</a>")
        repository.setStyleSheet("font-size: 16px;")
        repository.setOpenExternalLinks(True)
        description = QLabel(Settings.DESCRIPTION)
        description.setStyleSheet("font-size: 13px;")
        description.setWordWrap(True)
        confirm_button = QPushButton("OK")
        confirm_button.clicked.connect(self.close)
        layout = QVBoxLayout()
        layout.addSpacing(20)
        layout.addWidget(version)
        layout.addSpacing(10)
        layout.addWidget(repository)
        layout.addWidget(description)
        layout.addSpacing(20)
        layout.addWidget(confirm_button)
        self.setLayout(layout)
        self.setWindowTitle("O programe")
        self.setFixedSize(400, 200)
