from PySide6.QtCore import QObject, QRunnable, QThreadPool

from models.logger.log import Log
from view.main_ui import Ui_MainWindow
from widgets.log_widget import LogWidget


class View(QObject):
    widgets = None

    class _DisplayLog(QRunnable):
        def __init__(self, log: Log):
            super(View._DisplayLog, self).__init__()
            self.log = log

        def run(self):
            View.widgets.log_list_view.addItem(LogWidget(self.log))
            View.widgets.log_list_view.scrollToBottom()

    def __init__(self, parent=None):
        super(View, self).__init__()
        View.widgets = Ui_MainWindow()
        View.widgets.setupUi(parent)
        self.threadpool = QThreadPool.globalInstance()

    def display_log(self, log):
        task = View._DisplayLog(log)
        self.threadpool.start(task)
