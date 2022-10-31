from PySide6.QtGui import QColor
from PySide6.QtWidgets import QListWidgetItem

from models.logger.constants import ERROR


class LogWidget(QListWidgetItem):
    def __init__(self, log):
        super(LogWidget, self).__init__()
        self.log = log
        self.setText(str(log))
        self.setForeground(log.level.color())
        if self.log.level >= ERROR:
            font = self.font()
            font.setBold(True)
            self.setFont(font)
            self.setBackground(QColor(255, 180, 0, 50))
