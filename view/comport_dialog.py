from PySide6.QtWidgets import QDialog, QGridLayout, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QComboBox
from PySide6.QtCore import Qt, Signal

from serial.tools import list_ports

class ComportDialog(QDialog):
    comports_confirmed_s = Signal(str, str)
    def __init__(self, parent=None):
        super(ComportDialog, self).__init__(parent)
        self.setWindowTitle("Výber comportov")

        self.main_layout = QVBoxLayout(self)

        self.main_layout.addSpacing(10)
        self.comport_list_text = QLabel("")
        self.main_layout.addWidget(self.comport_list_text)

        self.main_layout.addSpacing(20)
        self.main_layout.addLayout(self._create_comports_form())

        self.main_layout.addSpacing(20)
        self.main_layout.addLayout(self._create_confirm_layout())

        self.main_layout.addSpacing(10)
        self.error_text = QLabel("")
        self.error_text.setStyleSheet("color: red")
        self.main_layout.addWidget(self.error_text)

        self.update_comport_list()

    def _create_confirm_layout(self):
        layout = QHBoxLayout()

        close_btn = QPushButton("Zavrieť")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)

        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(self.update_comport_list)
        layout.addWidget(refresh_btn)

        self.confirm_btn = QPushButton("Potvrdiť")
        self.confirm_btn.clicked.connect(self.confirm_comports)
        layout.addWidget(self.confirm_btn)

        layout.setAlignment(Qt.AlignRight)
        return layout

    def _create_comports_form(self):
        layout = QGridLayout()

        layout.addWidget(QLabel("Milivoltmeter comport"), 0, 0)
        self.lockin_comport_cbox = QComboBox()
        self.lockin_comport_cbox.setFixedWidth(150)
        self.lockin_comport_cbox.activated.connect(self.clear_error)
        layout.addWidget(self.lockin_comport_cbox, 0, 1)

        layout.addWidget(QLabel("Motor comport"), 1, 0)
        self.motor_comport_cbox = QComboBox()
        self.motor_comport_cbox.activated.connect(self.clear_error)
        layout.addWidget(self.motor_comport_cbox, 1, 1)

        return layout

    def clear_error(self):
        self.error_text.setText("")
    def update_comport_list(self):
        comport_names = [' - ']
        comports = list_ports.comports()
        comport_names.extend([c.name for c in list_ports.comports()])

        self.comport_list_text.setText('\n'.join([f'{c.name} = {c.description}' for c in comports]))

        for cbox in (self.lockin_comport_cbox, self.motor_comport_cbox):
            cbox.clear()
            cbox.addItems(comport_names)

    def confirm_comports(self):
        lockin_port = self.lockin_comport_cbox.currentText()
        motor_port = self.motor_comport_cbox.currentText()


        if lockin_port == motor_port:
            if lockin_port == ' - ':
                self.error_text.setText("Nevybral si žiadne porty!")
            else:
                self.error_text.setText("Vyber rozdielne porty!")
            return

        self.comports_confirmed_s.emit(lockin_port, motor_port)





