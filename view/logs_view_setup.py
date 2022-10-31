from PySide6.QtWidgets import QListWidget


def logs_view_setup(logs_view: QListWidget):
    logs_view.setWordWrap(True)
    logs_view.setUniformItemSizes(True)
    logs_view.setResizeMode(QListWidget.Adjust)
    logs_view.setSpacing(2)
    logs_view.setFlow(QListWidget.TopToBottom)
    logs_view.setDragDropMode(QListWidget.NoDragDrop)
