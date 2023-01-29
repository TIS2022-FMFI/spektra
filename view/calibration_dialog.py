from PySide6.QtWidgets import QDialog, QGridLayout, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, \
    QDoubleSpinBox, QSpinBox, QLCDNumber, QLineEdit
from PySide6.QtCore import Qt, Signal

from models.disperse_element import CalibrationData


class CalibrationDialog(QDialog):
    calibration_data_s = Signal(CalibrationData)

    def __init__(self, parent=None):
        super(CalibrationDialog, self).__init__(parent)
        self.setWindowTitle("Kalibrácia")
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addSpacing(20)
        self.main_layout.addLayout(self._create_name_form())
        self.main_layout.addSpacing(20)
        self.main_layout.addLayout(self._create_constants_form())
        self.main_layout.addSpacing(20)
        self.main_layout.addLayout(self._create_min_max_layout())
        self.main_layout.addSpacing(20)
        self.main_layout.addLayout(self._create_calibration_form())
        self.main_layout.addSpacing(20)
        self.main_layout.addLayout(self._create_confirm_layout())

    def _create_calibration_form(self):
        layout = QGridLayout()
        layout.addWidget(QLabel("Počiatočná pozícia"), 0, 0)
        self.start_pos = QDoubleSpinBox()
        layout.addWidget(self.start_pos, 0, 1)
        layout.addWidget(QLabel("Koncová pozícia"), 1, 0)
        self.end_pos = QDoubleSpinBox()
        layout.addWidget(self.end_pos, 1, 1)
        layout.addWidget(QLabel("Krok"), 2, 0)
        self.step_size = QSpinBox()
        self.step_size.setRange(1, 2000)
        layout.addWidget(self.step_size, 2, 1)
        self.step_button = QPushButton("Posunúť")
        layout.addWidget(self.step_button, 2, 2)
        layout.addWidget(QLabel("Počet krokov"), 3, 0)
        self.step_counter = QLCDNumber()
        self.step_button.clicked.connect(
            lambda: self.step_counter.display(self.step_counter.value() + self.step_size.value()))
        layout.addWidget(self.step_counter, 3, 1)
        return layout

    def _create_min_max_layout(self):
        layout = QGridLayout()
        layout.addWidget(QLabel("Minimálny uhol"), 0, 0)
        self.min_angle = QDoubleSpinBox()
        layout.addWidget(self.min_angle, 0, 1)
        layout.addWidget(QLabel("Maximálny uhol"), 1, 0)
        self.max_angle = QDoubleSpinBox()
        layout.addWidget(self.max_angle, 1, 1)
        return layout

    def _create_confirm_layout(self):
        layout = QHBoxLayout()
        close_btn = QPushButton("Zavrieť")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)
        self.confirm_btn = QPushButton("Potvrdiť")
        self.confirm_btn.clicked.connect(lambda: self.calibration_data_s.emit(self.get_calibration_data()))
        layout.addWidget(self.confirm_btn)
        layout.setAlignment(Qt.AlignRight)
        return layout

    def _create_constants_form(self):
        layout = QGridLayout()
        layout.addWidget(QLabel("Spektrálny rád"), 0, 0)
        self.spec_rad = QSpinBox()
        self.spec_rad.setMaximum(100)
        self.spec_rad.setValue(1)
        layout.addWidget(self.spec_rad, 0, 1)
        layout.addWidget(QLabel("G"), 1, 0)
        self.g = QDoubleSpinBox()
        self.g.setMaximum(10000)
        self.g.setValue(0)
        layout.addWidget(self.g, 1, 1)
        self.correction = QDoubleSpinBox()
        layout.addWidget(QLabel("Korekcia"), 2, 0)
        layout.addWidget(self.correction, 2, 1)
        layout.addWidget(QLabel("Násobok"), 3, 0)
        self.multiplier = QDoubleSpinBox()
        self.multiplier.setMaximum(10000)
        self.multiplier.setValue(2000)
        layout.addWidget(self.multiplier, 3, 1)
        return layout

    def _create_name_form(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Názov kalibrácie"))
        self.name = QLineEdit()
        layout.addWidget(self.name)
        return layout

    def get_calibration_data(self):
        """
        Returns calibration data from dialog window.
        :return: CalibrationData
        """
        return CalibrationData(self.name.text(),
                               self.spec_rad.value(),
                               self.g.value(),
                               self.correction.value(),
                               self.multiplier.value(),
                               self.min_angle.value(),
                               self.max_angle.value(),
                               self.start_pos.value(),
                               self.end_pos.value(),
                               self.step_counter.value())
