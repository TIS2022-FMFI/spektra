# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_final_draft.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDockWidget,
                               QDoubleSpinBox, QFormLayout, QFrame, QGraphicsView,
                               QGridLayout, QHBoxLayout, QHeaderView, QLCDNumber,
                               QLabel, QLineEdit, QListView, QMainWindow,
                               QMenu, QMenuBar, QPushButton, QRadioButton,
                               QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
                               QStatusBar, QTabWidget, QToolBar, QTreeView,
                               QVBoxLayout, QWidget, QListWidget)

from view.file_manager_setup import setup_filemanager_view
from view.logs_view_setup import logs_view_setup


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(1342, 975)
        MainWindow.setStyleSheet(u"")
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QMainWindow.AllowNestedDocks|QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks|QMainWindow.GroupedDragging|QMainWindow.VerticalTabs)
        self.action_play = QAction(MainWindow)
        self.action_play.setObjectName(u"action_play")
        icon = QIcon()
        icon.addFile(u"assets/icons/play_circle_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_play.setIcon(icon)
        self.action_stop = QAction(MainWindow)
        self.action_stop.setObjectName(u"action_stop")
        icon1 = QIcon()
        icon1.addFile(u"assets/icons/stop_circle_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_stop.setIcon(icon1)
        self.action_pause = QAction(MainWindow)
        self.action_pause.setObjectName(u"action_pause")
        icon2 = QIcon()
        icon2.addFile(u"assets/icons/pause_circle_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_pause.setIcon(icon2)
        self.action_new = QAction(MainWindow)
        self.action_new.setObjectName(u"action_new")
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_save_as = QAction(MainWindow)
        self.action_save_as.setObjectName(u"action_save_as")
        self.action_save_as_template = QAction(MainWindow)
        self.action_save_as_template.setObjectName(u"action_save_as_template")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.gridLayout = QGridLayout(self.central_widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.measurement_config_menu = QWidget(self.central_widget)
        self.measurement_config_menu.setObjectName(u"measurement_config_menu")
        self.gridLayout_7 = QGridLayout(self.measurement_config_menu)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, -1, 0, -1)
        self.measurement_config_menu_tabs = QTabWidget(self.measurement_config_menu)
        self.measurement_config_menu_tabs.setObjectName(u"measurement_config_menu_tabs")
        self.measurement_config_tab = QWidget()
        self.measurement_config_tab.setObjectName(u"measurement_config_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.measurement_config_tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.measurement_config_menu_meas_widget = QWidget(self.measurement_config_tab)
        self.measurement_config_menu_meas_widget.setObjectName(u"measurement_config_menu_meas_widget")
        self.measurement_config_menu_meas_widget.setStyleSheet(u"")
        self.formLayout = QFormLayout(self.measurement_config_menu_meas_widget)
        self.formLayout.setObjectName(u"formLayout")
        self.measurement_config_menu_filename_label = QLabel(self.measurement_config_menu_meas_widget)
        self.measurement_config_menu_filename_label.setObjectName(u"measurement_config_menu_filename_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.measurement_config_menu_filename_label)

        self.measurement_config_menu_filename_ledit = QLineEdit(self.measurement_config_menu_meas_widget)
        self.measurement_config_menu_filename_ledit.setObjectName(u"measurement_config_menu_filename_ledit")
        self.measurement_config_menu_filename_ledit.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.measurement_config_menu_filename_ledit)

        self.measurement_config_menu_sample_label = QLabel(self.measurement_config_menu_meas_widget)
        self.measurement_config_menu_sample_label.setObjectName(u"measurement_config_menu_sample_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.measurement_config_menu_sample_label)

        self.measurement_config_menu_sample_cbox = QComboBox(self.measurement_config_menu_meas_widget)
        self.measurement_config_menu_sample_cbox.setObjectName(u"measurement_config_menu_sample_cbox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.measurement_config_menu_sample_cbox)

        self.measurement_config_menu_width_label = QLabel(self.measurement_config_menu_meas_widget)
        self.measurement_config_menu_width_label.setObjectName(u"measurement_config_menu_width_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.measurement_config_menu_width_label)

        self.measurement_config_menu_width_sbox = QSpinBox(self.measurement_config_menu_meas_widget)
        self.measurement_config_menu_width_sbox.setObjectName(u"measurement_config_menu_width_sbox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.measurement_config_menu_width_sbox)

        self.measurement_config_menu_start_label = QLabel(self.measurement_config_menu_meas_widget)
        self.measurement_config_menu_start_label.setObjectName(u"measurement_config_menu_start_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.measurement_config_menu_start_label)

        self.measurement_config_menu_start_sbox = QSpinBox(self.measurement_config_menu_meas_widget)
        self.measurement_config_menu_start_sbox.setObjectName(u"measurement_config_menu_start_sbox")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.measurement_config_menu_start_sbox)

        self.measurement_config_menu_end_label = QLabel(self.measurement_config_menu_meas_widget)
        self.measurement_config_menu_end_label.setObjectName(u"measurement_config_menu_end_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.measurement_config_menu_end_label)

        self.measurement_config_menu_end_sbox = QSpinBox(self.measurement_config_menu_meas_widget)
        self.measurement_config_menu_end_sbox.setObjectName(u"measurement_config_menu_end_sbox")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.measurement_config_menu_end_sbox)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(5, QFormLayout.FieldRole, self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.measurement_config_menu_meas_widget)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.measurement_config_menu_tabs.addTab(self.measurement_config_tab, "")
        self.voltmeter_tab = QWidget()
        self.voltmeter_tab.setObjectName(u"voltmeter_tab")
        self.horizontalLayout_4 = QHBoxLayout(self.voltmeter_tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.measurement_config_menu_volt_widget = QWidget(self.voltmeter_tab)
        self.measurement_config_menu_volt_widget.setObjectName(u"measurement_config_menu_volt_widget")
        self.formLayout_2 = QFormLayout(self.measurement_config_menu_volt_widget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.measurement_config_menu_ref_label = QLabel(self.measurement_config_menu_volt_widget)
        self.measurement_config_menu_ref_label.setObjectName(u"measurement_config_menu_ref_label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.measurement_config_menu_ref_label)

        self.measurement_config_menu_ref_sbox = QSpinBox(self.measurement_config_menu_volt_widget)
        self.measurement_config_menu_ref_sbox.setObjectName(u"measurement_config_menu_ref_sbox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measurement_config_menu_ref_sbox.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_ref_sbox.setSizePolicy(sizePolicy)
        self.measurement_config_menu_ref_sbox.setMinimumSize(QSize(0, 0))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.measurement_config_menu_ref_sbox)

        self.measurement_config_menu_time_const_label = QLabel(self.measurement_config_menu_volt_widget)
        self.measurement_config_menu_time_const_label.setObjectName(u"measurement_config_menu_time_const_label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.measurement_config_menu_time_const_label)

        self.measurement_config_menu_time_const_dsbox = QDoubleSpinBox(self.measurement_config_menu_volt_widget)
        self.measurement_config_menu_time_const_dsbox.setObjectName(u"measurement_config_menu_time_const_dsbox")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.measurement_config_menu_time_const_dsbox)

        self.measurement_config_menu_span_label = QLabel(self.measurement_config_menu_volt_widget)
        self.measurement_config_menu_span_label.setObjectName(u"measurement_config_menu_span_label")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.measurement_config_menu_span_label)

        self.measurement_config_menu_span_dsbox = QDoubleSpinBox(self.measurement_config_menu_volt_widget)
        self.measurement_config_menu_span_dsbox.setObjectName(u"measurement_config_menu_span_dsbox")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.measurement_config_menu_span_dsbox)

        self.measurement_config_menu_span_auto_check = QCheckBox(self.measurement_config_menu_volt_widget)
        self.measurement_config_menu_span_auto_check.setObjectName(u"measurement_config_menu_span_auto_check")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.measurement_config_menu_span_auto_check)

        self.measurement_config_menu_angle_label = QLabel(self.measurement_config_menu_volt_widget)
        self.measurement_config_menu_angle_label.setObjectName(u"measurement_config_menu_angle_label")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.measurement_config_menu_angle_label)

        self.measurement_config_menu_angle_sbox = QSpinBox(self.measurement_config_menu_volt_widget)
        self.measurement_config_menu_angle_sbox.setObjectName(u"measurement_config_menu_angle_sbox")

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.measurement_config_menu_angle_sbox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_2.setItem(8, QFormLayout.FieldRole, self.verticalSpacer_2)


        self.horizontalLayout_4.addWidget(self.measurement_config_menu_volt_widget)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.measurement_config_menu_tabs.addTab(self.voltmeter_tab, "")
        self.light_source_tab = QWidget()
        self.light_source_tab.setObjectName(u"light_source_tab")
        self.horizontalLayout_5 = QHBoxLayout(self.light_source_tab)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.measurement_config_menu_light_widget = QWidget(self.light_source_tab)
        self.measurement_config_menu_light_widget.setObjectName(u"measurement_config_menu_light_widget")
        self.formLayout_3 = QFormLayout(self.measurement_config_menu_light_widget)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.measurement_config_menu_halogen_label = QLabel(self.measurement_config_menu_light_widget)
        self.measurement_config_menu_halogen_label.setObjectName(u"measurement_config_menu_halogen_label")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.measurement_config_menu_halogen_label)

        self.measurement_config_menu_halogen_cbox = QComboBox(self.measurement_config_menu_light_widget)
        self.measurement_config_menu_halogen_cbox.setObjectName(u"measurement_config_menu_halogen_cbox")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.measurement_config_menu_halogen_cbox)

        self.measurement_config_menu_deuterium_label = QLabel(self.measurement_config_menu_light_widget)
        self.measurement_config_menu_deuterium_label.setObjectName(u"measurement_config_menu_deuterium_label")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.measurement_config_menu_deuterium_label)

        self.measurement_config_menu_deuterium_cbox = QComboBox(self.measurement_config_menu_light_widget)
        self.measurement_config_menu_deuterium_cbox.setObjectName(u"measurement_config_menu_deuterium_cbox")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.measurement_config_menu_deuterium_cbox)

        self.measurement_config_menu_laser_label = QLabel(self.measurement_config_menu_light_widget)
        self.measurement_config_menu_laser_label.setObjectName(u"measurement_config_menu_laser_label")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.measurement_config_menu_laser_label)

        self.measurement_config_menu_laser_ledit = QLineEdit(self.measurement_config_menu_light_widget)
        self.measurement_config_menu_laser_ledit.setObjectName(u"measurement_config_menu_laser_ledit")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.measurement_config_menu_laser_ledit)

        self.measurement_config_menu_temp_label = QLabel(self.measurement_config_menu_light_widget)
        self.measurement_config_menu_temp_label.setObjectName(u"measurement_config_menu_temp_label")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.measurement_config_menu_temp_label)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_3.setItem(6, QFormLayout.FieldRole, self.verticalSpacer_4)

        self.measurement_config_menu_temp_qbox = QComboBox(self.measurement_config_menu_light_widget)
        self.measurement_config_menu_temp_qbox.setObjectName(u"measurement_config_menu_temp_qbox")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.measurement_config_menu_temp_qbox)

        self.measurement_config_menu_temp_sbox = QDoubleSpinBox(self.measurement_config_menu_light_widget)
        self.measurement_config_menu_temp_sbox.setObjectName(u"measurement_config_menu_temp_sbox")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.measurement_config_menu_temp_sbox)


        self.horizontalLayout_5.addWidget(self.measurement_config_menu_light_widget)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.measurement_config_menu_tabs.addTab(self.light_source_tab, "")
        self.monochromator_tab = QWidget()
        self.monochromator_tab.setObjectName(u"monochromator_tab")
        self.horizontalLayout_3 = QHBoxLayout(self.monochromator_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.widget_2 = QWidget(self.monochromator_tab)
        self.widget_2.setObjectName(u"widget_2")
        self.formLayout_5 = QFormLayout(self.widget_2)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.comboBox = QComboBox(self.widget_2)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.comboBox)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_4)


        self.horizontalLayout_3.addWidget(self.widget_2)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.measurement_config_menu_tabs.addTab(self.monochromator_tab, "")

        self.gridLayout_7.addWidget(self.measurement_config_menu_tabs, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.measurement_config_menu, 0, 0, 1, 1)

        self.graph_view = QGraphicsView(self.central_widget)
        self.graph_view.setObjectName(u"graph_view")

        self.gridLayout.addWidget(self.graph_view, 1, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 5)
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1342, 21))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_settings = QMenu(self.menubar)
        self.menu_settings.setObjectName(u"menu_settings")
        self.menu_windows = QMenu(self.menubar)
        self.menu_windows.setObjectName(u"menu_windows")
        self.menu_about = QMenu(self.menubar)
        self.menu_about.setObjectName(u"menu_about")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.showMessage("Prostredie bolo inicializované")
        self.statusbar.setStyleSheet("color: green")
        self.statusbar.setFont(QFont("Arial", 10))
        self.measurment_controls_toolbar = QToolBar(MainWindow)
        self.measurment_controls_toolbar.setObjectName(u"measurment_controls_toolbar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.measurment_controls_toolbar.sizePolicy().hasHeightForWidth())
        self.measurment_controls_toolbar.setSizePolicy(sizePolicy1)
        self.measurment_controls_toolbar.setLayoutDirection(Qt.RightToLeft)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.measurment_controls_toolbar)
        self.devices_controls_dock_widget = QDockWidget(MainWindow)
        self.devices_controls_dock_widget.setObjectName(u"devices_controls_dock_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.devices_controls_dock_widget.sizePolicy().hasHeightForWidth())
        self.devices_controls_dock_widget.setSizePolicy(sizePolicy2)
        self.devices_controls_dock_widget.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.devices_controls_dock_widget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.verticalLayout_5 = QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.devices_controls_devices_selection_label = QLabel(self.dockWidgetContents_3)
        self.devices_controls_devices_selection_label.setObjectName(u"devices_controls_devices_selection_label")

        self.verticalLayout_5.addWidget(self.devices_controls_devices_selection_label)

        self.devices_controls_devices_selection_widget = QWidget(self.dockWidgetContents_3)
        self.devices_controls_devices_selection_widget.setObjectName(u"devices_controls_devices_selection_widget")
        self.formLayout_4 = QFormLayout(self.devices_controls_devices_selection_widget)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.devices_controls_devices_selection_volt_label = QLabel(self.devices_controls_devices_selection_widget)
        self.devices_controls_devices_selection_volt_label.setObjectName(u"devices_controls_devices_selection_volt_label")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.devices_controls_devices_selection_volt_label)

        self.devices_controls_devices_selection_volt_cbox = QComboBox(self.devices_controls_devices_selection_widget)
        self.devices_controls_devices_selection_volt_cbox.setObjectName(u"devices_controls_devices_selection_volt_cbox")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.devices_controls_devices_selection_volt_cbox)

        self.devices_controls_devices_selection_disperse_label = QLabel(self.devices_controls_devices_selection_widget)
        self.devices_controls_devices_selection_disperse_label.setObjectName(u"devices_controls_devices_selection_disperse_label")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.devices_controls_devices_selection_disperse_label)

        self.devices_controls_devices_selection_disperse_cbox = QComboBox(self.devices_controls_devices_selection_widget)
        self.devices_controls_devices_selection_disperse_cbox.setObjectName(u"devices_controls_devices_selection_disperse_cbox")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.devices_controls_devices_selection_disperse_cbox)


        self.verticalLayout_5.addWidget(self.devices_controls_devices_selection_widget)

        self.line_2 = QFrame(self.dockWidgetContents_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.dockWidgetContents_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.radioButton = QRadioButton(self.dockWidgetContents_3)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.dockWidgetContents_3)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.line = QFrame(self.dockWidgetContents_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.devices_controls_engine_positioning_label = QLabel(self.dockWidgetContents_3)
        self.devices_controls_engine_positioning_label.setObjectName(u"devices_controls_engine_positioning_label")

        self.verticalLayout_5.addWidget(self.devices_controls_engine_positioning_label)

        self.devices_controls_engine_positioning_widget = QWidget(self.dockWidgetContents_3)
        self.devices_controls_engine_positioning_widget.setObjectName(u"devices_controls_engine_positioning_widget")
        self.verticalLayout_6 = QVBoxLayout(self.devices_controls_engine_positioning_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.devices_controls_devices_engine_controls_widget = QWidget(self.devices_controls_engine_positioning_widget)
        self.devices_controls_devices_engine_controls_widget.setObjectName(u"devices_controls_devices_engine_controls_widget")
        self.horizontalLayout_6 = QHBoxLayout(self.devices_controls_devices_engine_controls_widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.devices_controls_engine_positioning_left_btn = QPushButton(self.devices_controls_devices_engine_controls_widget)
        self.devices_controls_engine_positioning_left_btn.setObjectName(u"devices_controls_engine_positioning_left_btn")
        self.devices_controls_engine_positioning_left_btn.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        icon3 = QIcon()
        icon3.addFile(u"assets/icons/keyboard_arrow_left_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.devices_controls_engine_positioning_left_btn.setIcon(icon3)

        self.horizontalLayout_6.addWidget(self.devices_controls_engine_positioning_left_btn)

        self.devices_controls_engine_positioning_step_sbox = QDoubleSpinBox(self.devices_controls_devices_engine_controls_widget)
        self.devices_controls_engine_positioning_step_sbox.setObjectName(u"devices_controls_engine_positioning_step_sbox")

        self.horizontalLayout_6.addWidget(self.devices_controls_engine_positioning_step_sbox)

        self.devices_controls_engine_positioning_right_btn = QPushButton(self.devices_controls_devices_engine_controls_widget)
        self.devices_controls_engine_positioning_right_btn.setObjectName(u"devices_controls_engine_positioning_right_btn")
        self.devices_controls_engine_positioning_right_btn.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        icon4 = QIcon()
        icon4.addFile(u"assets/icons/keyboard_arrow_right_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.devices_controls_engine_positioning_right_btn.setIcon(icon4)

        self.horizontalLayout_6.addWidget(self.devices_controls_engine_positioning_right_btn)


        self.verticalLayout_6.addWidget(self.devices_controls_devices_engine_controls_widget)

        self.devices_controls_devices_goto_widget = QWidget(self.devices_controls_engine_positioning_widget)
        self.devices_controls_devices_goto_widget.setObjectName(u"devices_controls_devices_goto_widget")
        self.gridLayout_2 = QGridLayout(self.devices_controls_devices_goto_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.devices_controls_goto_label = QLabel(self.devices_controls_devices_goto_widget)
        self.devices_controls_goto_label.setObjectName(u"devices_controls_goto_label")

        self.gridLayout_2.addWidget(self.devices_controls_goto_label, 1, 0, 1, 1)

        self.devices_controls_goto_sbox = QSpinBox(self.devices_controls_devices_goto_widget)
        self.devices_controls_goto_sbox.setObjectName(u"devices_controls_goto_sbox")

        self.gridLayout_2.addWidget(self.devices_controls_goto_sbox, 1, 1, 1, 1)

        self.devices_controls_goto_btn = QPushButton(self.devices_controls_devices_goto_widget)
        self.devices_controls_goto_btn.setObjectName(u"devices_controls_goto_btn")

        self.gridLayout_2.addWidget(self.devices_controls_goto_btn, 1, 2, 1, 1)


        self.verticalLayout_6.addWidget(self.devices_controls_devices_goto_widget)


        self.verticalLayout_5.addWidget(self.devices_controls_engine_positioning_widget)

        self.line_3 = QFrame(self.dockWidgetContents_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_3)

        self.devices_controls_engine_settings_label = QLabel(self.dockWidgetContents_3)
        self.devices_controls_engine_settings_label.setObjectName(u"devices_controls_engine_settings_label")

        self.verticalLayout_5.addWidget(self.devices_controls_engine_settings_label)

        self.devices_controls_engine_settings_widget = QWidget(self.dockWidgetContents_3)
        self.devices_controls_engine_settings_widget.setObjectName(u"devices_controls_engine_settings_widget")
        self.gridLayout_3 = QGridLayout(self.devices_controls_engine_settings_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.devices_controls_calibration_btn = QPushButton(self.devices_controls_engine_settings_widget)
        self.devices_controls_calibration_btn.setObjectName(u"devices_controls_calibration_btn")

        self.gridLayout_3.addWidget(self.devices_controls_calibration_btn, 1, 1, 1, 1)

        self.devices_controls_calibration_label = QLabel(self.devices_controls_engine_settings_widget)
        self.devices_controls_calibration_label.setObjectName(u"devices_controls_calibration_label")

        self.gridLayout_3.addWidget(self.devices_controls_calibration_label, 1, 0, 1, 1)

        self.label = QLabel(self.devices_controls_engine_settings_widget)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.devices_controls_engine_settings_widget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.gridLayout_3.addWidget(self.doubleSpinBox, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.devices_controls_engine_settings_widget)

        self.line_4 = QFrame(self.dockWidgetContents_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_4)

        self.devices_controls_current_wavelength_widget = QWidget(self.dockWidgetContents_3)
        self.devices_controls_current_wavelength_widget.setObjectName(u"devices_controls_current_wavelength_widget")
        self.horizontalLayout_7 = QHBoxLayout(self.devices_controls_current_wavelength_widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.devices_controls_angle_label = QLabel(self.devices_controls_current_wavelength_widget)
        self.devices_controls_angle_label.setObjectName(u"devices_controls_angle_label")

        self.horizontalLayout_7.addWidget(self.devices_controls_angle_label)

        self.lcdNumber = QLCDNumber(self.devices_controls_current_wavelength_widget)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.horizontalLayout_7.addWidget(self.lcdNumber)


        self.verticalLayout_5.addWidget(self.devices_controls_current_wavelength_widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.devices_controls_dock_widget.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.devices_controls_dock_widget)
        self.log_dock_widget = QDockWidget(MainWindow)
        self.log_dock_widget.setObjectName(u"log_dock_widget")
        self.log_dock_widget.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidgetContents_5 = QWidget()
        self.dockWidgetContents_5.setObjectName(u"dockWidgetContents_5")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.log_scroll_area = QScrollArea(self.dockWidgetContents_5)
        self.log_scroll_area.setObjectName(u"log_scroll_area")
        self.log_scroll_area.setMinimumSize(QSize(1304, 0))
        self.log_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1322, 210))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.log_list_view = QListWidget(self.scrollAreaWidgetContents)
        logs_view_setup(self.log_list_view)
        self.log_list_view.setObjectName(u"log_list_view")

        self.verticalLayout_4.addWidget(self.log_list_view)

        self.log_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.log_scroll_area)

        self.log_dock_widget.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.log_dock_widget)
        self.comparative_file_dock_widget = QDockWidget(MainWindow)
        self.comparative_file_dock_widget.setObjectName(u"comparative_file_dock_widget")
        self.comparative_file_dock_widget.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.comparative_file_info_widget = QWidget(self.dockWidgetContents)
        self.comparative_file_info_widget.setObjectName(u"comparative_file_info_widget")
        self.gridLayout_6 = QGridLayout(self.comparative_file_info_widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.comparative_file_light_value_label = QLabel(self.comparative_file_info_widget)
        self.comparative_file_light_value_label.setObjectName(u"comparative_file_light_value_label")

        self.gridLayout_6.addWidget(self.comparative_file_light_value_label, 6, 2, 1, 1)

        self.comparative_file_filename_label = QLabel(self.comparative_file_info_widget)
        self.comparative_file_filename_label.setObjectName(u"comparative_file_filename_label")

        self.gridLayout_6.addWidget(self.comparative_file_filename_label, 1, 0, 1, 1)

        self.comparative_file_sample_value_label = QLabel(self.comparative_file_info_widget)
        self.comparative_file_sample_value_label.setObjectName(u"comparative_file_sample_value_label")

        self.gridLayout_6.addWidget(self.comparative_file_sample_value_label, 2, 2, 1, 1)

        self.comparative_file_sample_label = QLabel(self.comparative_file_info_widget)
        self.comparative_file_sample_label.setObjectName(u"comparative_file_sample_label")

        self.gridLayout_6.addWidget(self.comparative_file_sample_label, 2, 0, 1, 1)

        self.comparative_file_width_value_label = QLabel(self.comparative_file_info_widget)
        self.comparative_file_width_value_label.setObjectName(u"comparative_file_width_value_label")

        self.gridLayout_6.addWidget(self.comparative_file_width_value_label, 3, 2, 1, 1)

        self.comparative_file_angle_value_label = QLabel(self.comparative_file_info_widget)
        self.comparative_file_angle_value_label.setObjectName(u"comparative_file_angle_value_label")

        self.gridLayout_6.addWidget(self.comparative_file_angle_value_label, 5, 2, 1, 1)

        self.comparative_file_width_label = QLabel(self.comparative_file_info_widget)
        self.comparative_file_width_label.setObjectName(u"comparative_file_width_label")

        self.gridLayout_6.addWidget(self.comparative_file_width_label, 3, 0, 1, 1)

        self.comparative_file_unload_btn = QPushButton(self.comparative_file_info_widget)
        self.comparative_file_unload_btn.setObjectName(u"comparative_file_unload_btn")

        self.gridLayout_6.addWidget(self.comparative_file_unload_btn, 0, 2, 1, 1)

        self.comparative_file_angle_label = QLabel(self.comparative_file_info_widget)
        self.comparative_file_angle_label.setObjectName(u"comparative_file_angle_label")

        self.gridLayout_6.addWidget(self.comparative_file_angle_label, 5, 0, 1, 1)

        self.comparative_file_filename_value_label = QLabel(self.comparative_file_info_widget)
        self.comparative_file_filename_value_label.setObjectName(u"comparative_file_filename_value_label")

        self.gridLayout_6.addWidget(self.comparative_file_filename_value_label, 1, 2, 1, 1)

        self.comparative_file_light_label = QLabel(self.comparative_file_info_widget)
        self.comparative_file_light_label.setObjectName(u"comparative_file_light_label")

        self.gridLayout_6.addWidget(self.comparative_file_light_label, 6, 0, 1, 1)

        self.comparative_file_widget_title_label = QLabel(self.comparative_file_info_widget)
        self.comparative_file_widget_title_label.setObjectName(u"comparative_file_widget_title_label")

        self.gridLayout_6.addWidget(self.comparative_file_widget_title_label, 0, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_8, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.comparative_file_info_widget)

        self.comparative_file_dir_view_widget = QWidget(self.dockWidgetContents)
        self.comparative_file_dir_view_widget.setObjectName(u"comparative_file_dir_view_widget")
        self.verticalLayout = QVBoxLayout(self.comparative_file_dir_view_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.comparative_file_dir_tree_view = QTreeView(self.comparative_file_dir_view_widget)
        setup_filemanager_view(self.comparative_file_dir_tree_view)
        self.comparative_file_dir_tree_view.setObjectName(u"comparative_file_dir_tree_view")

        self.verticalLayout.addWidget(self.comparative_file_dir_tree_view)


        self.verticalLayout_2.addWidget(self.comparative_file_dir_view_widget)

        self.comparative_file_dock_widget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.comparative_file_dock_widget)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_windows.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_save_as)
        self.menu_file.addAction(self.action_save_as_template)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.measurment_controls_toolbar.addAction(self.action_stop)
        self.measurment_controls_toolbar.addAction(self.action_pause)
        self.measurment_controls_toolbar.addAction(self.action_play)

        self.retranslateUi(MainWindow)

        self.measurement_config_menu_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ARTKEPS", None))
        self.action_play.setText(QCoreApplication.translate("MainWindow", u"play", None))
        self.action_stop.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.action_pause.setText(QCoreApplication.translate("MainWindow", u"pause", None))
        self.action_new.setText(QCoreApplication.translate("MainWindow", u"Nov\u00fd", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"Otvor", None))
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017ei\u0165", None))
        self.action_save_as.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017ei\u0165 ako", None))
        self.action_save_as_template.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017ei\u0165 ako \u0161abl\u00f3nu", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Ukon\u010di\u0165", None))
        self.measurement_config_menu_filename_label.setText(QCoreApplication.translate("MainWindow", u"N\u00e1zov suboru", None))
        self.measurement_config_menu_sample_label.setText(QCoreApplication.translate("MainWindow", u"Vzorka", None))
        self.measurement_config_menu_width_label.setText(QCoreApplication.translate("MainWindow", u"Hr\u00fabka", None))
        self.measurement_config_menu_start_label.setText(QCoreApplication.translate("MainWindow", u"Za\u010diatok", None))
        self.measurement_config_menu_end_label.setText(QCoreApplication.translate("MainWindow", u"Koniec", None))
        self.measurement_config_menu_tabs.setTabText(self.measurement_config_menu_tabs.indexOf(self.measurement_config_tab), QCoreApplication.translate("MainWindow", u"Meranie", None))
        self.measurement_config_menu_ref_label.setText(QCoreApplication.translate("MainWindow", u"Ref", None))
        self.measurement_config_menu_time_const_label.setText(QCoreApplication.translate("MainWindow", u"Tc", None))
        self.measurement_config_menu_span_label.setText(QCoreApplication.translate("MainWindow", u"Rozsah", None))
        self.measurement_config_menu_span_auto_check.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.measurement_config_menu_angle_label.setText(QCoreApplication.translate("MainWindow", u"Uhol", None))
        self.measurement_config_menu_tabs.setTabText(self.measurement_config_menu_tabs.indexOf(self.voltmeter_tab), QCoreApplication.translate("MainWindow", u"Milivoltmeter", None))
        self.measurement_config_menu_halogen_label.setText(QCoreApplication.translate("MainWindow", u"Halogen", None))
        self.measurement_config_menu_deuterium_label.setText(QCoreApplication.translate("MainWindow", u"Deuterium", None))
        self.measurement_config_menu_laser_label.setText(QCoreApplication.translate("MainWindow", u"Laser", None))
        self.measurement_config_menu_temp_label.setText(QCoreApplication.translate("MainWindow", u"Teplota", None))
        self.measurement_config_menu_tabs.setTabText(self.measurement_config_menu_tabs.indexOf(self.light_source_tab), QCoreApplication.translate("MainWindow", u"Zdroj svetla", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PMT", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Napatie", None))
        self.measurement_config_menu_tabs.setTabText(self.measurement_config_menu_tabs.indexOf(self.monochromator_tab), QCoreApplication.translate("MainWindow", u"Monochrom\u00e1tor", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"S\u00fabor", None))
        self.menu_settings.setTitle(QCoreApplication.translate("MainWindow", u"Nastavenia", None))
        self.menu_windows.setTitle(QCoreApplication.translate("MainWindow", u"Okn\u00e1", None))
        self.menu_about.setTitle(QCoreApplication.translate("MainWindow", u"O programe", None))
        self.measurment_controls_toolbar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.devices_controls_devices_selection_label.setText(QCoreApplication.translate("MainWindow", u"Zariadenia", None))
        self.devices_controls_devices_selection_volt_label.setText(QCoreApplication.translate("MainWindow", u"Milivoltmeter", None))
        self.devices_controls_devices_selection_disperse_label.setText(QCoreApplication.translate("MainWindow", u"Disperzn\u00fd prvok", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Jednotky", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Uhol", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Angstrom", None))
        self.devices_controls_engine_positioning_label.setText(QCoreApplication.translate("MainWindow", u"Polohovanie motora", None))
        self.devices_controls_engine_positioning_left_btn.setText("")
        self.devices_controls_engine_positioning_right_btn.setText("")
        self.devices_controls_goto_label.setText(QCoreApplication.translate("MainWindow", u"Cho\u010f na", None))
        self.devices_controls_goto_btn.setText(QCoreApplication.translate("MainWindow", u"Nastav", None))
        self.devices_controls_engine_settings_label.setText(QCoreApplication.translate("MainWindow", u"Inicializovanie polohy motora", None))
        self.devices_controls_calibration_btn.setText(QCoreApplication.translate("MainWindow", u"Spusti", None))
        self.devices_controls_calibration_label.setText(QCoreApplication.translate("MainWindow", u"Inicializ\u00e1cia", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Uhol", None))
        self.devices_controls_angle_label.setText(QCoreApplication.translate("MainWindow", u"Vlnov\u00e1 d\u013a\u017eka", None))
        self.comparative_file_light_value_label.setText("")
        self.comparative_file_filename_label.setText(QCoreApplication.translate("MainWindow", u"N\u00e1zov", None))
        self.comparative_file_sample_value_label.setText("")
        self.comparative_file_sample_label.setText(QCoreApplication.translate("MainWindow", u"Vzorka", None))
        self.comparative_file_width_value_label.setText("")
        self.comparative_file_angle_value_label.setText("")
        self.comparative_file_width_label.setText(QCoreApplication.translate("MainWindow", u"Hr\u00fabka", None))
        self.comparative_file_unload_btn.setText(QCoreApplication.translate("MainWindow", u"Zru\u0161", None))
        self.comparative_file_angle_label.setText(QCoreApplication.translate("MainWindow", u"Uhol", None))
        self.comparative_file_filename_value_label.setText("")
        self.comparative_file_light_label.setText(QCoreApplication.translate("MainWindow", u"Zdroj svetla", None))
        self.comparative_file_widget_title_label.setText(QCoreApplication.translate("MainWindow", u"Porovn\u00e1van\u00e9 meranie", None))
    # retranslateUi

