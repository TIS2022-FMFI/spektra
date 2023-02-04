from PySide6.QtWidgets import QListWidget


def logs_view_setup(logs_view: QListWidget):
    """Setup logs view.
    @param logs_view: QListWidget instance to set up.
    """
    logs_view.setWordWrap(True)
    logs_view.setUniformItemSizes(True)
    logs_view.setResizeMode(QListWidget.Adjust)
    logs_view.setFlow(QListWidget.TopToBottom)
    logs_view.setDragDropMode(QListWidget.NoDragDrop)
