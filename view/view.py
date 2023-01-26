from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal
from PySide6.QtGui import QAction, QFont
from PySide6.QtWidgets import QApplication, QWidget, QSizePolicy
from qt_material import apply_stylesheet
from settings import Settings
from models.logger.log import Log
from view.file_manager_setup import setup_filemanager_view
from view.logs_view_setup import logs_view_setup
from view.main_ui import Ui_MainWindow
from widgets.log_widget import LogWidget
from view.constants import DAY_MODE, NIGHT_MODE


class View(QObject):
    widgets = None
    saved_measurements_path_s = Signal(str)
    voltmeter_connection_s = Signal(bool)

    class _DisplayLog(QRunnable):
        def __init__(self, log: Log):
            super(View._DisplayLog, self).__init__()
            self.log = log

        def run(self):
            View.widgets.log_list_view.addItem(LogWidget(self.log))
            View.widgets.log_list_view.scrollToBottom()

    def __init__(self, parent=None):
        super(View, self).__init__()
        self._voltmeter_connected = False
        View.widgets = Ui_MainWindow()
        View.widgets.setupUi(parent)
        setup_filemanager_view(View.widgets.comparative_file_dir_tree_view)
        logs_view_setup(View.widgets.log_list_view)
        View.widgets.action_stop.setVisible(False)
        self._decorate_toolbar(parent)
        self.mode = DAY_MODE
        self._icons = None
        self.display_theme()
        self.threadpool = QThreadPool.globalInstance()
        self.setup_connections()

    def display_log(self, log):
        task = View._DisplayLog(log)
        self.threadpool.start(task)

    def set_font(self, font: QFont):
        QApplication.instance().setFont(font)

    def _get_font(self):
        font = QFont()
        font.setFamilies([u"Nirmala UI Semilight"])
        font.setBold(True)
        return font

    def display_theme(self):
        if self.mode == DAY_MODE:
            theme = Settings.LIGHT_THEME + '.xml'
        elif self.mode == NIGHT_MODE:
            theme = Settings.DARK_THEME + '.xml'
        apply_stylesheet(QApplication.instance(), theme=theme, invert_secondary=True)
        self.display_icons()
        self.set_font(self._get_font())

    def update_status_bar(self, message):
        View.widgets.statusbar.showMessage(message)

    def _decorate_toolbar(self, main_window):
        def add_spacer():
            spacer = QWidget()
            spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.widgets.measurment_controls_toolbar.addWidget(spacer)

        def add_action(name):
            action = QAction(main_window)
            action.setObjectName(name)
            self.widgets.measurment_controls_toolbar.addAction(action)
            return action

        add_spacer()
        add_action("action_ui_mode")
        self.widgets.measurment_controls_toolbar.addSeparator()
        action = add_action(u"voltmeter_connect_action")
        action.setEnabled(False)

    def display_icons(self):
        if self._icons is None:
            from view.icons import Icons
            self._icons = Icons()
        enabled = self.widgets.action_play.isEnabled()
        self.widgets.action_play.setIcon(self._icons.get('start_measurement', self.mode, enabled))
        self.widgets.action_stop.setIcon(self._icons.get('stop_measurement', self.mode, True))
        enabled = self.widgets.action_save.isEnabled()
        self.widgets.action_save.setIcon(self._icons.get('save_measurement', self.mode, enabled))
        # enabled = self.widgets.action_measurement_file.isEnabled()
        # self.widgets.action_load.setIcon(self._icons.get('load_measurement', self.mode, enabled))
        # enabled = self.widgets.action_settings.isEnabled()
        # self.widgets.action_settings.setIcon(self._icons.get('settings', self.mode, enabled))
        # enabled = self.widgets.action_exit.isEnabled()
        # self.widgets.action_exit.setIcon(self._icons.get('exit', self.mode, enabled))
        # enabled = self.widgets.action_ui_mode.isEnabled()
        # self.widgets.action_switch_ui_mode.setIcon(self._icons.get('switch_ui_mode', self.mode, enabled))
        # enabled = self.widgets.action_about.isEnabled()
        # self.widgets.action_about.setIcon(self._icons.get('about', self.mode, enabled))
        # enabled = self.widgets.action_help.isEnabled()
        # self.widgets.action_help.setIcon(self._icons.get('help', self.mode, enabled))
        action_ui_mode = self._get_action('action_ui_mode')
        action_ui_mode.setIcon(self._icons.get('ui', self.mode))
        enabled = self.widgets.devices_controls_engine_positioning_left_btn.isEnabled()
        self.widgets.devices_controls_engine_positioning_left_btn.setIcon(self._icons.get('left_arrow', self.mode,
                                                                                          enabled))
        enabled = self.widgets.devices_controls_engine_positioning_right_btn.isEnabled()
        self.widgets.devices_controls_engine_positioning_right_btn.setIcon(self._icons.get('right_arrow', self.mode,
                                                                                           enabled))
        self.update_voltmeter_indicator()

    def setup_connections(self):
        self.voltmeter_connection_s.connect(lambda x: self._on_voltmeter_connection_change(x))
        action_ui_mode = self._get_action('action_ui_mode')
        action_ui_mode.triggered.connect(self._on_ui_mode_change)

    def _on_ui_mode_change(self):
        if self.mode == DAY_MODE:
            self.mode = NIGHT_MODE
        else:
            self.mode = DAY_MODE
        self.display_theme()

    def _on_voltmeter_connection_change(self, connected):
        self._voltmeter_connected = connected
        self.update_voltmeter_indicator()

    def update_voltmeter_indicator(self):
        if self._voltmeter_connected:
            self._display_voltmeter_connected()
        else:
            self._display_voltmeter_disconnected()

    def _get_action(self, name):
        for action in self.widgets.measurment_controls_toolbar.actions():
            if action.objectName() == name:
                return action

    def _display_voltmeter_disconnected(self):
        voltmeter_connect_action = self._get_action('voltmeter_connect_action')
        status_bar_message = "Voltmeter je odpojený"
        self.update_status_bar(status_bar_message)
        voltmeter_connect_action.setIcon(self._icons.get('voltmeter_disconnected', DAY_MODE, True))
        voltmeter_connect_action.setToolTip("Voltmeter odpojený")

    def _display_voltmeter_connected(self):
        voltmeter_connect_action = self._get_action('voltmeter_connect_action')
        status_bar_message = "Voltmeter je pripojený"
        self.update_status_bar(status_bar_message)
        voltmeter_connect_action.setIcon(self._icons.get('voltmeter_connected', DAY_MODE, True))
        voltmeter_connect_action.setToolTip("Voltmeter pripojený")

    def switch_play_button(self):
        self.widgets.action_play.setVisible(not self.widgets.action_play.isVisible())
        self.widgets.action_stop.setVisible(not self.widgets.action_stop.isVisible())
