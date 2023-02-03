# -*- coding: utf-8 -*-
import sys

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
                               QMenu, QMenuBar, QProgressBar, QPushButton,
                               QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
                               QSpinBox, QStatusBar, QTabWidget, QTextBrowser,
                               QToolBar, QToolBox, QTreeView, QVBoxLayout,
                               QWidget, QListWidget, QMessageBox)
import pyqtgraph as pg

from view.calibration_dialog import CalibrationDialog
from view.comport_dialog import ComportDialog
from widgets.about_dialog import AboutDialog
from widgets.graph import Graph
from view.constants import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        '''
        setups user interface of the application
        @param MainWindow: mainWindow of the application
        @return:
        '''
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(1342, 975)
        font = QFont()
        font.setFamilies([u"Nirmala UI Semilight"])
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(
            QMainWindow.AllowNestedDocks | QMainWindow.AllowTabbedDocks | QMainWindow.AnimatedDocks | QMainWindow.GroupedDragging | QMainWindow.VerticalTabs)
        self.action_play = QAction(MainWindow)
        self.action_play.setObjectName(u"action_play")
        icon = QIcon()

        self.action_play.setIcon(icon)
        self.action_stop = QAction(MainWindow)
        self.action_stop.setObjectName(u"action_stop")
        icon1 = QIcon()

        self.action_stop.setIcon(icon1)
        self.action_new = QAction(MainWindow)
        self.action_new.setObjectName(u"action_new")
        self.about_dialog = AboutDialog(MainWindow)
        font1 = QFont()
        font1.setFamilies([u"Nirmala UI Semilight"])
        self.action_new.setFont(font1)
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_save_as = QAction(MainWindow)
        self.action_save_as.setObjectName(u"action_save_as")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.actionKalibr_cia = QAction(MainWindow)
        self.actionKalibr_cia.setObjectName(u"actionKalibr_cia")
        self.action_choose_comport = QAction(MainWindow)
        self.action_choose_comport.setObjectName(u"action_choose_comport")
        self.actionDokument_cia = QAction(MainWindow)
        self.actionDokument_cia.setObjectName(u"actionDokument_cia")
        self.actionO_programe = QAction(MainWindow)
        self.actionO_programe.setObjectName(u"actionO_programe")
        self.actionDenn = QAction(MainWindow)
        self.actionDenn.setObjectName(u"actionDenn")
        self.actionNo_n = QAction(MainWindow)
        self.actionNo_n.setObjectName(u"actionNo_n")
        self.actionPorovnanie = QAction(MainWindow)
        self.actionPorovnanie.setObjectName(u"actionPorovnanie")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setFont(font)
        self.gridLayout = QGridLayout(self.central_widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 0, 9, 9)
        self.graph_view = Graph(self.central_widget)
        self.graph_view.setObjectName(u"graph_view")
        font2 = QFont()
        font2.setBold(True)
        self.graph_view.setFont(font2)
        self.gridLayout.addWidget(self.graph_view, 2, 0, 1, 1)
        self.measurement_config_menu = QWidget(self.central_widget)
        self.measurement_config_menu.setObjectName(u"measurement_config_menu")
        self.measurement_config_menu.setFont(font)
        self.gridLayout_7 = QGridLayout(self.measurement_config_menu)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, -1, 0, -1)
        self.measurement_config_menu_tabs = QTabWidget(self.measurement_config_menu)
        self.measurement_config_menu_tabs.setObjectName(u"measurement_config_menu_tabs")
        self.measurement_config_menu_tabs.setFont(font2)
        self.sample_tab = QWidget()
        self.sample_tab.setObjectName(u"sample_tab")
        self.horizontalLayout_12 = QHBoxLayout(self.sample_tab)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_13 = QSpacerItem(73, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_13)

        self.widget_8 = QWidget(self.sample_tab)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_11 = QGridLayout(self.widget_8)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.widget_3 = QWidget(self.widget_8)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_8 = QVBoxLayout(self.widget_3)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.measurement_config_menu_sample_label = QLabel(self.widget_4)
        self.measurement_config_menu_sample_label.setObjectName(u"measurement_config_menu_sample_label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measurement_config_menu_sample_label.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_sample_label.setSizePolicy(sizePolicy)
        self.measurement_config_menu_sample_label.setFont(font)

        self.horizontalLayout_8.addWidget(self.measurement_config_menu_sample_label)

        self.saple_name_ledit = QLineEdit(self.widget_4)
        self.saple_name_ledit.setObjectName(u"saple_name_ledit")

        self.horizontalLayout_8.addWidget(self.saple_name_ledit)

        self.measurement_config_menu_width_label_4 = QLabel(self.widget_4)
        self.measurement_config_menu_width_label_4.setObjectName(u"measurement_config_menu_width_label_4")
        sizePolicy.setHeightForWidth(self.measurement_config_menu_width_label_4.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_width_label_4.setSizePolicy(sizePolicy)
        self.measurement_config_menu_width_label_4.setFont(font)

        self.horizontalLayout_8.addWidget(self.measurement_config_menu_width_label_4)

        self.sample_temperature_ledit = QLineEdit(self.widget_4)
        self.sample_temperature_ledit.setObjectName(u"sample_temperature_ledit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sample_temperature_ledit.sizePolicy().hasHeightForWidth())
        self.sample_temperature_ledit.setSizePolicy(sizePolicy1)
        self.horizontalLayout_8.addWidget(self.sample_temperature_ledit)
        self.measurement_config_menu_width_label = QLabel(self.widget_4)
        self.measurement_config_menu_width_label.setObjectName(u"measurement_config_menu_width_label")
        sizePolicy.setHeightForWidth(self.measurement_config_menu_width_label.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_width_label.setSizePolicy(sizePolicy)
        self.measurement_config_menu_width_label.setFont(font)

        self.horizontalLayout_8.addWidget(self.measurement_config_menu_width_label)

        self.sample_width_dsbox = QDoubleSpinBox(self.widget_4)
        self.sample_width_dsbox.setObjectName(u"sample_width_dsbox")
        self.horizontalLayout_8.addWidget(self.sample_width_dsbox)
        self.verticalLayout_8.addWidget(self.widget_4)

        self.gridLayout_11.addWidget(self.widget_3, 0, 0, 1, 1)
        self.calibration_dialog = CalibrationDialog(MainWindow)
        self.comport_choice_dialog = ComportDialog(MainWindow)
        self.sample_notes = QWidget(self.widget_8)
        self.sample_notes.setObjectName(u"sample_notes")
        self.formLayout_2 = QFormLayout(self.sample_notes)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.measurement_config_menu_width_label_2 = QLabel(self.sample_notes)
        self.measurement_config_menu_width_label_2.setObjectName(u"measurement_config_menu_width_label_2")
        sizePolicy.setHeightForWidth(self.measurement_config_menu_width_label_2.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_width_label_2.setSizePolicy(sizePolicy)
        self.measurement_config_menu_width_label_2.setFont(font)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.measurement_config_menu_width_label_2)

        self.sample_note_ledit = QLineEdit(self.sample_notes)
        self.sample_note_ledit.setObjectName(u"sample_note_ledit")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.sample_note_ledit)

        self.measurement_config_menu_width_label_3 = QLabel(self.sample_notes)
        self.measurement_config_menu_width_label_3.setObjectName(u"measurement_config_menu_width_label_3")
        sizePolicy.setHeightForWidth(self.measurement_config_menu_width_label_3.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_width_label_3.setSizePolicy(sizePolicy)
        self.measurement_config_menu_width_label_3.setFont(font)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.measurement_config_menu_width_label_3)

        self.sample_measurement_ledit = QLineEdit(self.sample_notes)
        self.sample_measurement_ledit.setObjectName(u"sample_measurement_ledit")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.sample_measurement_ledit)

        self.gridLayout_11.addWidget(self.sample_notes, 1, 0, 1, 1)

        self.horizontalLayout_12.addWidget(self.widget_8)

        self.horizontalSpacer_14 = QSpacerItem(73, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_14)

        self.measurement_config_menu_tabs.addTab(self.sample_tab, "")
        self.measurement_config_tab = QWidget()
        self.measurement_config_tab.setObjectName(u"measurement_config_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.measurement_config_tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.measurement_config_menu_meas_widget = QWidget(self.measurement_config_tab)
        self.measurement_config_menu_meas_widget.setObjectName(u"measurement_config_menu_meas_widget")
        self.measurement_config_menu_meas_widget.setFont(font2)
        self.measurement_config_menu_meas_widget.setStyleSheet(u"")
        self.horizontalLayout_9 = QHBoxLayout(self.measurement_config_menu_meas_widget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.widget_7 = QWidget(self.measurement_config_menu_meas_widget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setFont(font2)
        self.verticalLayout_12 = QVBoxLayout(self.widget_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_6 = QWidget(self.widget_7)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setFont(font2)
        self.horizontalLayout_11 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.measurement_config_menu_filename_label = QLabel(self.widget_6)
        self.measurement_config_menu_filename_label.setObjectName(u"measurement_config_menu_filename_label")
        sizePolicy.setHeightForWidth(self.measurement_config_menu_filename_label.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_filename_label.setSizePolicy(sizePolicy)
        self.measurement_config_menu_filename_label.setFont(font)

        self.horizontalLayout_11.addWidget(self.measurement_config_menu_filename_label)

        self.measurement_config_menu_filename_ledit = QLineEdit(self.widget_6)
        self.measurement_config_menu_filename_ledit.setObjectName(u"measurement_config_menu_filename_ledit")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.measurement_config_menu_filename_ledit.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_filename_ledit.setSizePolicy(sizePolicy2)
        self.measurement_config_menu_filename_ledit.setFont(font2)
        self.measurement_config_menu_filename_ledit.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.measurement_config_menu_filename_ledit)

        self.verticalLayout_12.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.widget_7)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setFont(font2)
        self.horizontalLayout_10 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.measurement_config_menu_start_label = QLabel(self.widget_5)
        self.measurement_config_menu_start_label.setObjectName(u"measurement_config_menu_start_label")
        sizePolicy.setHeightForWidth(self.measurement_config_menu_start_label.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_start_label.setSizePolicy(sizePolicy)
        self.measurement_config_menu_start_label.setFont(font)

        self.horizontalLayout_10.addWidget(self.measurement_config_menu_start_label)

        self.measurement_config_menu_start_sbox = QDoubleSpinBox(self.widget_5)
        self.measurement_config_menu_start_sbox.setObjectName(u"measurement_config_menu_start_sbox")
        sizePolicy1.setHeightForWidth(self.measurement_config_menu_start_sbox.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_start_sbox.setSizePolicy(sizePolicy1)
        self.measurement_config_menu_start_sbox.setFont(font2)
        self.measurement_config_menu_start_sbox.setRange(0, 20000)

        self.horizontalLayout_10.addWidget(self.measurement_config_menu_start_sbox)

        self.measurement_config_menu_end_label = QLabel(self.widget_5)
        self.measurement_config_menu_end_label.setObjectName(u"measurement_config_menu_end_label")
        sizePolicy.setHeightForWidth(self.measurement_config_menu_end_label.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_end_label.setSizePolicy(sizePolicy)
        self.measurement_config_menu_end_label.setFont(font)

        self.horizontalLayout_10.addWidget(self.measurement_config_menu_end_label)

        self.measurement_config_menu_end_sbox = QDoubleSpinBox(self.widget_5)
        self.measurement_config_menu_end_sbox.setObjectName(u"measurement_config_menu_end_sbox")
        sizePolicy1.setHeightForWidth(self.measurement_config_menu_end_sbox.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_end_sbox.setSizePolicy(sizePolicy1)
        self.measurement_config_menu_end_sbox.setFont(font2)
        self.measurement_config_menu_end_sbox.setRange(0, 20000)

        self.horizontalLayout_10.addWidget(self.measurement_config_menu_end_sbox)

        self.verticalLayout_12.addWidget(self.widget_5)

        self.horizontalLayout_9.addWidget(self.widget_7)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.widget = QWidget(self.measurement_config_menu_meas_widget)
        self.widget.setObjectName(u"widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
        self.widget.setFont(font2)
        self.gridLayout_9 = QGridLayout(self.widget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.gridLayout_9.addWidget(self.label_7, 0, 0, 1, 1)

        self.measurement_integrations_sbox = QSpinBox(self.widget)
        self.measurement_integrations_sbox.setObjectName(u"measurement_integrations_sbox")
        self.measurement_integrations_sbox.setFont(font2)
        self.measurement_integrations_sbox.setRange(1, 10)

        self.gridLayout_9.addWidget(self.measurement_integrations_sbox, 0, 1, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.gridLayout_9.addWidget(self.label_5, 1, 0, 1, 1)

        self.measurement_correction_sbox = QDoubleSpinBox(self.widget)
        self.measurement_correction_sbox.setObjectName(u"measurement_correction_sbox")
        self.measurement_correction_sbox.setFont(font2)
        self.measurement_correction_sbox.setDecimals(4)
        self.measurement_correction_sbox.setRange(-99, 99)

        self.gridLayout_9.addWidget(self.measurement_correction_sbox, 1, 1, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout_9.addWidget(self.label_6, 2, 0, 1, 1)

        self.measurement_motor_step = QSpinBox(self.widget)
        self.measurement_motor_step.setObjectName(u"measurement_motor_step")
        self.measurement_motor_step.setFont(font2)
        self.measurement_motor_step.setRange(1, 128)

        self.gridLayout_9.addWidget(self.measurement_motor_step, 2, 1, 1, 1)

        self.horizontalLayout_9.addWidget(self.widget)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)

        self.horizontalLayout_2.addWidget(self.measurement_config_menu_meas_widget)

        self.measurement_config_menu_tabs.addTab(self.measurement_config_tab, "")
        self.voltmeter_tab = QWidget()
        self.voltmeter_tab.setObjectName(u"voltmeter_tab")
        self.horizontalLayout_4 = QHBoxLayout(self.voltmeter_tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.measurement_config_menu_volt_widget = QWidget(self.voltmeter_tab)
        self.measurement_config_menu_volt_widget.setObjectName(u"measurement_config_menu_volt_widget")
        self.horizontalLayout_16 = QHBoxLayout(self.measurement_config_menu_volt_widget)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_6)

        self.widget_13 = QWidget(self.measurement_config_menu_volt_widget)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_6 = QGridLayout(self.widget_13)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.measurement_config_menu_ref_label = QLabel(self.widget_13)
        self.measurement_config_menu_ref_label.setObjectName(u"measurement_config_menu_ref_label")

        self.gridLayout_6.addWidget(self.measurement_config_menu_ref_label, 0, 0, 1, 1)

        self.measurement_config_menu_ref_sbox = QDoubleSpinBox(self.widget_13)
        self.measurement_config_menu_ref_sbox.setObjectName(u"measurement_config_menu_ref_sbox")
        sizePolicy2.setHeightForWidth(self.measurement_config_menu_ref_sbox.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_ref_sbox.setSizePolicy(sizePolicy2)
        self.measurement_config_menu_ref_sbox.setMinimumSize(QSize(0, 0))
        self.measurement_config_menu_ref_sbox.setRange(0, 1000)
        self.gridLayout_6.addWidget(self.measurement_config_menu_ref_sbox, 0, 1, 1, 1)

        self.measurement_config_menu_min_sensitivity_label = QLabel(self.widget_13)
        self.measurement_config_menu_min_sensitivity_label.setObjectName(u"measurement_config_menu_min_sensitivity_label")

        self.gridLayout_6.addWidget(self.measurement_config_menu_min_sensitivity_label, 1, 0, 1, 1)

        self.measurement_config_menu_min_sensitivity_sbox = QSpinBox(self.widget_13)
        self.measurement_config_menu_min_sensitivity_sbox.setObjectName(u"measurement_config_menu_min_sensitivity_sbox")
        sizePolicy2.setHeightForWidth(self.measurement_config_menu_min_sensitivity_sbox.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_min_sensitivity_sbox.setSizePolicy(sizePolicy2)
        self.measurement_config_menu_min_sensitivity_sbox.setMinimumSize(QSize(0, 0))
        self.measurement_config_menu_min_sensitivity_sbox.setRange(0, 20)
        self.gridLayout_6.addWidget(self.measurement_config_menu_min_sensitivity_sbox, 1, 1, 1, 1)

        self.measurement_config_menu_span_label = QLabel(self.widget_13)
        self.measurement_config_menu_span_label.setObjectName(u"measurement_config_menu_span_label")
        spacer = QLabel(self.widget_13)
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout_6.addWidget(spacer, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.measurement_config_menu_span_label, 2, 0, 1, 1)
        self.measurement_config_menu_span_dsbox = QDoubleSpinBox(self.widget_13)
        self.measurement_config_menu_span_dsbox.setObjectName(u"measurement_config_menu_span_dsbox")
        sizePolicy2.setHeightForWidth(self.measurement_config_menu_span_dsbox.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_span_dsbox.setSizePolicy(sizePolicy2)
        self.gridLayout_6.addWidget(self.measurement_config_menu_span_dsbox, 2, 1, 1, 1)
        self.measurement_config_menu_span_auto_check = QCheckBox(self.widget_13)
        self.measurement_config_menu_span_auto_check.setObjectName(u"measurement_config_menu_span_auto_check")
        self.gridLayout_6.addWidget(self.measurement_config_menu_span_auto_check, 1, 2, 1, 1)
        self.horizontalLayout_16.addWidget(self.widget_13)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(self.horizontalSpacer_8)
        self.widget_16 = QWidget(self.measurement_config_menu_volt_widget)
        self.widget_16.setObjectName(u"widget_16")
        self.gridLayout_5 = QGridLayout(self.widget_16)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.measurement_config_menu_time_const_label = QLabel(self.widget_16)
        self.measurement_config_menu_time_const_label.setObjectName(u"measurement_config_menu_time_const_label")
        self.gridLayout_5.addWidget(self.measurement_config_menu_time_const_label, 0, 0, 1, 1)


        self.measurement_config_menu_time_const_dsbox = QDoubleSpinBox(self.widget_16)
        self.measurement_config_menu_time_const_dsbox.setObjectName(u"measurement_config_menu_time_const_dsbox")
        sizePolicy2.setHeightForWidth(self.measurement_config_menu_time_const_dsbox.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_time_const_dsbox.setSizePolicy(sizePolicy2)
        self.gridLayout_5.addWidget(self.measurement_config_menu_time_const_dsbox, 0, 1, 1, 1)


        self.measurement_config_menu_time_const_label_post = QLabel(self.widget_16, text="Časová konštanta- post")
        self.measurement_config_menu_time_const_label_post.setObjectName(u"measurement_config_menu_time_const_label_post")
        self.gridLayout_5.addWidget(self.measurement_config_menu_time_const_label_post, 1, 0, 1, 1)
        self.measurement_config_menu_time_const_dsbox_post = QDoubleSpinBox(self.widget_16)
        self.measurement_config_menu_time_const_dsbox_post.setObjectName(u"measurement_config_menu_time_const_dsbox_post")
        sizePolicy2.setHeightForWidth(self.measurement_config_menu_time_const_dsbox_post.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_time_const_dsbox_post.setSizePolicy(sizePolicy2)
        self.gridLayout_5.addWidget(self.measurement_config_menu_time_const_dsbox_post, 1, 1, 1, 1)



        self.measurement_config_menu_angle_label = QLabel(self.widget_16)
        self.measurement_config_menu_angle_label.setObjectName(u"measurement_config_menu_angle_label")
        self.gridLayout_5.addWidget(self.measurement_config_menu_angle_label, 2, 0, 1, 1)
        self.measurement_config_menu_angle_sbox = QSpinBox(self.widget_16)
        self.measurement_config_menu_angle_sbox.setObjectName(u"measurement_config_menu_angle_sbox")
        self.gridLayout_5.addWidget(self.measurement_config_menu_angle_sbox, 2, 1, 1, 1)
        self.horizontalLayout_16.addWidget(self.widget_16)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_4.addWidget(self.measurement_config_menu_volt_widget)

        self.measurement_config_menu_tabs.addTab(self.voltmeter_tab, "")
        self.light_source_tab = QWidget()
        self.light_source_tab.setObjectName(u"light_source_tab")
        self.horizontalLayout_5 = QHBoxLayout(self.light_source_tab)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.measurement_config_menu_light_widget = QWidget(self.light_source_tab)
        self.measurement_config_menu_light_widget.setObjectName(u"measurement_config_menu_light_widget")
        self.gridLayout_8 = QGridLayout(self.measurement_config_menu_light_widget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_3, 0, 5, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)

        self.measurement_config_menu_halogen_cbox = QComboBox(self.measurement_config_menu_light_widget)
        self.measurement_config_menu_halogen_cbox.setObjectName(u"measurement_config_menu_halogen_cbox")
        sizePolicy1.setHeightForWidth(self.measurement_config_menu_halogen_cbox.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_halogen_cbox.setSizePolicy(sizePolicy1)

        self.gridLayout_8.addWidget(self.measurement_config_menu_halogen_cbox, 0, 2, 1, 1)

        self.measurement_config_menu_halogen_label = QLabel(self.measurement_config_menu_light_widget)
        self.measurement_config_menu_halogen_label.setObjectName(u"measurement_config_menu_halogen_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.measurement_config_menu_halogen_label.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_halogen_label.setSizePolicy(sizePolicy4)

        self.gridLayout_8.addWidget(self.measurement_config_menu_halogen_label, 0, 1, 1, 1)

        self.measurement_config_menu_laser_label = QLabel(self.measurement_config_menu_light_widget)
        self.measurement_config_menu_laser_label.setObjectName(u"measurement_config_menu_laser_label")

        self.gridLayout_8.addWidget(self.measurement_config_menu_laser_label, 0, 3, 1, 1)

        self.measurement_config_menu_laser_ledit = QLineEdit(self.measurement_config_menu_light_widget)
        self.measurement_config_menu_laser_ledit.setObjectName(u"measurement_config_menu_laser_ledit")
        sizePolicy2.setHeightForWidth(self.measurement_config_menu_laser_ledit.sizePolicy().hasHeightForWidth())
        self.measurement_config_menu_laser_ledit.setSizePolicy(sizePolicy2)

        self.gridLayout_8.addWidget(self.measurement_config_menu_laser_ledit, 0, 4, 1, 1)

        self.horizontalLayout_5.addWidget(self.measurement_config_menu_light_widget)

        self.measurement_config_menu_tabs.addTab(self.light_source_tab, "")
        self.detector_tab = QWidget()
        self.detector_tab.setObjectName(u"detector_tab")
        self.horizontalLayout_3 = QHBoxLayout(self.detector_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.widget_2 = QWidget(self.detector_tab)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.detector_pmt_ledit = QLineEdit(self.widget_2)
        self.detector_pmt_ledit.setObjectName(u"detector_pmt_ledit")

        self.gridLayout_4.addWidget(self.detector_pmt_ledit, 0, 1, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)

        self.detector_voltage_ledit = QLineEdit(self.widget_2)
        self.detector_voltage_ledit.setObjectName(u"detector_voltage_ledit")

        self.gridLayout_4.addWidget(self.detector_voltage_ledit, 1, 1, 1, 1)

        self.horizontalLayout_3.addWidget(self.widget_2)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.measurement_config_menu_tabs.addTab(self.detector_tab, "")
        self.monochromator_tab = QWidget()
        self.monochromator_tab.setObjectName(u"monochromator_tab")
        self.horizontalLayout_15 = QHBoxLayout(self.monochromator_tab)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_15)

        self.widget_14 = QWidget(self.monochromator_tab)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_10 = QGridLayout(self.widget_14)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.widget_10 = QWidget(self.widget_14)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.widget_9 = QWidget(self.widget_10)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_14 = QVBoxLayout(self.widget_9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_8 = QLabel(self.widget_9)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_14.addWidget(self.label_8)

        self.widget_12 = QWidget(self.widget_9)
        self.widget_12.setObjectName(u"widget_12")
        self.formLayout = QFormLayout(self.widget_12)
        self.formLayout.setObjectName(u"formLayout")
        self.label_9 = QLabel(self.widget_12)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.monochromator_in_in_start = QDoubleSpinBox(self.widget_12)
        self.monochromator_in_in_start.setObjectName(u"monochromator_in_in_start")
        self.monochromator_in_in_start.setSingleStep(0.01)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.monochromator_in_in_start)

        self.label_10 = QLabel(self.widget_12)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.monochromator_in_in_start_2 = QDoubleSpinBox(self.widget_12)
        self.monochromator_in_in_start_2.setObjectName(u"monochromator_in_in_start_2")
        self.monochromator_in_in_start_2.setSingleStep(0.01)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.monochromator_in_in_start_2)

        self.verticalLayout_14.addWidget(self.widget_12)

        self.horizontalLayout_13.addWidget(self.widget_9)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_18)

        self.output_widget = QWidget(self.widget_10)
        self.output_widget.setObjectName(u"output_widget")
        self.verticalLayout_15 = QVBoxLayout(self.output_widget)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_14 = QLabel(self.output_widget)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_15.addWidget(self.label_14)

        self.widget_15 = QWidget(self.output_widget)
        self.widget_15.setObjectName(u"widget_15")
        self.formLayout_3 = QFormLayout(self.widget_15)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_15 = QLabel(self.widget_15)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_15)

        self.monochromator_out_out_start = QDoubleSpinBox(self.widget_15)
        self.monochromator_out_out_start.setObjectName(u"monochromator_out_out_start")
        self.monochromator_out_out_start.setSingleStep(0.01)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.monochromator_out_out_start)



        self.verticalLayout_15.addWidget(self.widget_15)

        self.horizontalLayout_13.addWidget(self.output_widget)

        self.gridLayout_10.addWidget(self.widget_10, 1, 0, 1, 1)

        self.widget_11 = QWidget(self.widget_14)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")

        self.label_110 = QLabel(self.widget_11)
        self.label_110.setObjectName(u"label_110")

        self.horizontalLayout_14.addWidget(self.label_110)

        self.monochromator_name_ledit = QLineEdit(self.widget_11)
        self.monochromator_name_ledit.setObjectName(u"monochromator_name_ledit")

        self.horizontalLayout_14.addWidget(self.monochromator_name_ledit)



        self.label_11 = QLabel(self.widget_11)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_14.addWidget(self.label_11)

        self.monochromator_optical_filter_ledit = QLineEdit(self.widget_11)
        self.monochromator_optical_filter_ledit.setObjectName(u"monochromator_optical_filter_ledit")

        self.horizontalLayout_14.addWidget(self.monochromator_optical_filter_ledit)




        self.gridLayout_10.addWidget(self.widget_11, 0, 0, 1, 1)

        self.horizontalLayout_15.addWidget(self.widget_14)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_16)

        self.measurement_config_menu_tabs.addTab(self.monochromator_tab, "")

        self.gridLayout_7.addWidget(self.measurement_config_menu_tabs, 1, 0, 1, 1)

        self.gridLayout.addWidget(self.measurement_config_menu, 0, 0, 1, 1)

        self.progressBar = QProgressBar(self.central_widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 4))
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 4)
        self.gridLayout.setRowStretch(2, 12)
        self.gridLayout.setRowStretch(3, 1)
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1342, 21))
        font3 = QFont()
        font3.setFamilies([u"Nirmala UI Semilight"])
        font3.setBold(False)
        self.menubar.setFont(font3)
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_file.setFont(font1)
        self.menuOtvor = QMenu(self.menu_file)
        self.menuOtvor.setObjectName(u"menuOtvor")
        self.menu_settings = QMenu(self.menubar)
        self.menu_settings.setObjectName(u"menu_settings")
        self.menuRe_im_zobrazenia = QMenu(self.menu_settings)
        self.menuRe_im_zobrazenia.setObjectName(u"menuRe_im_zobrazenia")
        self.menu_about = QMenu(self.menubar)
        self.menu_about.setObjectName(u"menu_about")
        self.menuN_stroje = QMenu(self.menubar)
        self.menuN_stroje.setObjectName(u"menuN_stroje")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.measurment_controls_toolbar = QToolBar(MainWindow)
        self.measurment_controls_toolbar.setObjectName(u"measurment_controls_toolbar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.measurment_controls_toolbar.sizePolicy().hasHeightForWidth())
        self.measurment_controls_toolbar.setSizePolicy(sizePolicy5)
        font4 = QFont()
        font4.setFamilies([u"Nirmala UI Semilight"])
        font4.setPointSize(11)
        self.measurment_controls_toolbar.setFont(font4)
        self.measurment_controls_toolbar.setLayoutDirection(Qt.RightToLeft)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.measurment_controls_toolbar)
        self.devices_controls_dock_widget = QDockWidget(MainWindow)
        self.devices_controls_dock_widget.setObjectName(u"devices_controls_dock_widget")
        sizePolicy4.setHeightForWidth(self.devices_controls_dock_widget.sizePolicy().hasHeightForWidth())
        self.devices_controls_dock_widget.setSizePolicy(sizePolicy4)
        self.devices_controls_dock_widget.setFont(font)
        self.devices_controls_dock_widget.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.devices_controls_dock_widget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.verticalLayout_5 = QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.devices_controls_devices_selection_label = QLabel(self.dockWidgetContents_3)
        self.devices_controls_devices_selection_label.setObjectName(u"devices_controls_devices_selection_label")
        font5 = QFont()
        font5.setFamilies([u"Nirmala UI Semilight"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.devices_controls_devices_selection_label.setFont(font5)

        self.verticalLayout_5.addWidget(self.devices_controls_devices_selection_label)

        self.devices_controls_devices_selection_widget = QWidget(self.dockWidgetContents_3)
        self.devices_controls_devices_selection_widget.setObjectName(u"devices_controls_devices_selection_widget")
        self.devices_controls_devices_selection_widget.setFont(font2)
        self.formLayout_4 = QFormLayout(self.devices_controls_devices_selection_widget)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.devices_controls_devices_selection_volt_label = QLabel(self.devices_controls_devices_selection_widget)
        self.devices_controls_devices_selection_volt_label.setObjectName(
            u"devices_controls_devices_selection_volt_label")
        self.devices_controls_devices_selection_volt_label.setFont(font)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.devices_controls_devices_selection_volt_label)
        self.devices_controls_devices_selection_volt_cbox = QComboBox(self.devices_controls_devices_selection_widget)
        self.devices_controls_devices_selection_volt_cbox.setObjectName(u"devices_controls_devices_selection_volt_cbox")
        self.devices_controls_devices_selection_volt_cbox.setFont(font2)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.devices_controls_devices_selection_volt_cbox)

        self.devices_controls_devices_selection_disperse_label = QLabel(self.devices_controls_devices_selection_widget)
        self.devices_controls_devices_selection_disperse_label.setObjectName(
            u"devices_controls_devices_selection_disperse_label")
        self.devices_controls_devices_selection_disperse_label.setFont(font)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.devices_controls_devices_selection_disperse_label)

        self.devices_controls_devices_selection_disperse_cbox = QComboBox(
            self.devices_controls_devices_selection_widget)
        self.devices_controls_devices_selection_disperse_cbox.setObjectName(
            u"devices_controls_devices_selection_disperse_cbox")
        self.devices_controls_devices_selection_disperse_cbox.setFont(font2)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.devices_controls_devices_selection_disperse_cbox)

        self.verticalLayout_5.addWidget(self.devices_controls_devices_selection_widget)

        self.line_2 = QFrame(self.dockWidgetContents_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFont(font2)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)

        self.label_2 = QLabel(self.dockWidgetContents_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font5)

        self.verticalLayout_5.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.radioButton = QRadioButton(self.dockWidgetContents_3)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font)

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.dockWidgetContents_3)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font)

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_11)

        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.line = QFrame(self.dockWidgetContents_3)
        self.line.setObjectName(u"line")
        self.line.setFont(font2)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.devices_controls_engine_positioning_label = QLabel(self.dockWidgetContents_3)
        self.devices_controls_engine_positioning_label.setObjectName(u"devices_controls_engine_positioning_label")
        self.devices_controls_engine_positioning_label.setFont(font5)

        self.verticalLayout_5.addWidget(self.devices_controls_engine_positioning_label)

        self.devices_controls_engine_positioning_widget = QWidget(self.dockWidgetContents_3)
        self.devices_controls_engine_positioning_widget.setObjectName(u"devices_controls_engine_positioning_widget")
        self.devices_controls_engine_positioning_widget.setFont(font2)
        self.verticalLayout_6 = QVBoxLayout(self.devices_controls_engine_positioning_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.devices_controls_devices_engine_controls_widget = QWidget(self.devices_controls_engine_positioning_widget)
        self.devices_controls_devices_engine_controls_widget.setObjectName(
            u"devices_controls_devices_engine_controls_widget")
        self.devices_controls_devices_engine_controls_widget.setFont(font2)
        self.horizontalLayout_6 = QHBoxLayout(self.devices_controls_devices_engine_controls_widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.devices_controls_engine_positioning_left_btn = QPushButton(
            self.devices_controls_devices_engine_controls_widget)
        self.devices_controls_engine_positioning_left_btn.setObjectName(u"devices_controls_engine_positioning_left_btn")
        self.devices_controls_engine_positioning_left_btn.setFont(font2)
        icon2 = QIcon()


        self.devices_controls_engine_positioning_left_btn.setIcon(icon2)

        self.horizontalLayout_6.addWidget(self.devices_controls_engine_positioning_left_btn)

        self.devices_controls_engine_positioning_step_sbox = QSpinBox(
            self.devices_controls_devices_engine_controls_widget)
        self.devices_controls_engine_positioning_step_sbox.setObjectName(
            u"devices_controls_engine_positioning_step_sbox")
        self.devices_controls_engine_positioning_step_sbox.setFont(font2)
        self.devices_controls_engine_positioning_step_sbox.setSingleStep(1)
        self.devices_controls_engine_positioning_step_sbox.setRange(0, 6000)

        self.horizontalLayout_6.addWidget(self.devices_controls_engine_positioning_step_sbox)

        self.devices_controls_engine_positioning_right_btn = QPushButton(
            self.devices_controls_devices_engine_controls_widget)
        self.devices_controls_engine_positioning_right_btn.setObjectName(
            u"devices_controls_engine_positioning_right_btn")
        self.devices_controls_engine_positioning_right_btn.setFont(font2)
        icon3 = QIcon()


        self.devices_controls_engine_positioning_right_btn.setIcon(icon3)

        self.horizontalLayout_6.addWidget(self.devices_controls_engine_positioning_right_btn)

        self.verticalLayout_6.addWidget(self.devices_controls_devices_engine_controls_widget)

        self.devices_controls_devices_goto_widget = QWidget(self.devices_controls_engine_positioning_widget)
        self.devices_controls_devices_goto_widget.setObjectName(u"devices_controls_devices_goto_widget")
        self.devices_controls_devices_goto_widget.setFont(font2)
        self.gridLayout_2 = QGridLayout(self.devices_controls_devices_goto_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, -1, 0, -1)
        self.devices_controls_goto_label = QLabel(self.devices_controls_devices_goto_widget)
        self.devices_controls_goto_label.setObjectName(u"devices_controls_goto_label")
        self.devices_controls_goto_label.setFont(font)

        self.gridLayout_2.addWidget(self.devices_controls_goto_label, 1, 0, 1, 1)

        self.devices_controls_goto_btn = QPushButton(self.devices_controls_devices_goto_widget)
        self.devices_controls_goto_btn.setObjectName(u"devices_controls_goto_btn")
        self.devices_controls_goto_btn.setFont(font)

        self.gridLayout_2.addWidget(self.devices_controls_goto_btn, 1, 2, 1, 1)

        self.devices_controls_goto_sbox = QDoubleSpinBox(self.devices_controls_devices_goto_widget)
        self.devices_controls_goto_sbox.setObjectName(u"devices_controls_goto_sbox")
        self.devices_controls_goto_sbox.setFont(font2)
        self.devices_controls_goto_sbox.setRange(0,20000)

        self.goto_confirmation_dialog = QMessageBox()
        self.goto_confirmation_dialog.setIcon(QMessageBox.Question)
        self.goto_confirmation_dialog.setWindowTitle("Určite?")
        self.goto_confirmation_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        self.gridLayout_2.addWidget(self.devices_controls_goto_sbox, 1, 1, 1, 1)

        self.verticalLayout_6.addWidget(self.devices_controls_devices_goto_widget)

        self.verticalLayout_5.addWidget(self.devices_controls_engine_positioning_widget)

        self.line_3 = QFrame(self.dockWidgetContents_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFont(font2)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_3)

        self.devices_controls_engine_settings_label = QLabel(self.dockWidgetContents_3)
        self.devices_controls_engine_settings_label.setObjectName(u"devices_controls_engine_settings_label")
        self.devices_controls_engine_settings_label.setFont(font5)

        self.verticalLayout_5.addWidget(self.devices_controls_engine_settings_label)

        self.devices_controls_engine_settings_widget = QWidget(self.dockWidgetContents_3)
        self.devices_controls_engine_settings_widget.setObjectName(u"devices_controls_engine_settings_widget")
        self.devices_controls_engine_settings_widget.setFont(font2)
        self.gridLayout_3 = QGridLayout(self.devices_controls_engine_settings_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.devices_controls_engine_settings_widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.motor_init_pos_sbox = QDoubleSpinBox(self.devices_controls_engine_settings_widget)
        self.motor_init_pos_sbox.setObjectName(u"motor_init_pos_sbox")
        self.motor_init_pos_sbox.setFont(font2)
        self.motor_init_pos_sbox.setRange(0, 30)
        self.motor_init_pos_sbox.setSuffix(" °")

        self.gridLayout_3.addWidget(self.motor_init_pos_sbox, 0, 1, 1, 1)

        self.devices_controls_calibration_btn = QPushButton(self.devices_controls_engine_settings_widget)
        self.devices_controls_calibration_btn.setObjectName(u"devices_controls_calibration_btn")
        self.devices_controls_calibration_btn.setFont(font)

        self.gridLayout_3.addWidget(self.devices_controls_calibration_btn, 0, 2, 1, 1)

        self.verticalLayout_5.addWidget(self.devices_controls_engine_settings_widget)

        self.line_4 = QFrame(self.dockWidgetContents_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFont(font2)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_4)

        self.devices_controls_current_wavelength_widget = QLabel("Posledné namerané hodnoty: ")
        self.devices_controls_current_wavelength_widget.setObjectName(u"devices_controls_current_wavelength_widget")
        self.devices_controls_current_wavelength_widget.setFont(font2)
        self.horizontalLayout_7 = QHBoxLayout(self.devices_controls_current_wavelength_widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.devices_controls_angle_label = QLabel(self.devices_controls_current_wavelength_widget)
        self.devices_controls_angle_label.setObjectName(u"devices_controls_angle_label")
        self.devices_controls_angle_label.setFont(font5)

        self.horizontalLayout_7.addWidget(self.devices_controls_angle_label)

        self.lcdNumber = QLCDNumber(self.devices_controls_current_wavelength_widget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setFont(font2)
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setProperty("value", 0.000000000000000)

        self.horizontalLayout_7.addWidget(self.lcdNumber)

        self.verticalLayout_5.addWidget(self.devices_controls_current_wavelength_widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.devices_controls_dock_widget.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.devices_controls_dock_widget)
        self.log_dock_widget = QDockWidget(MainWindow)
        self.log_dock_widget.setObjectName(u"log_dock_widget")
        self.log_dock_widget.setFont(font)
        self.log_dock_widget.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.dockWidgetContents_5 = QWidget()
        self.dockWidgetContents_5.setObjectName(u"dockWidgetContents_5")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.log_scroll_area = QScrollArea(self.dockWidgetContents_5)
        self.log_scroll_area.setObjectName(u"log_scroll_area")
        self.log_scroll_area.setMinimumSize(QSize(1304, 0))
        self.log_scroll_area.setFont(font2)
        self.log_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1322, 210))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.log_list_view = QListWidget(self.scrollAreaWidgetContents)
        self.log_list_view.setObjectName(u"log_list_view")
        self.log_list_view.setFont(font)

        self.verticalLayout_4.addWidget(self.log_list_view)

        self.log_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.log_scroll_area)

        self.log_dock_widget.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.log_dock_widget)
        self.comparative_file_dock_widget = QDockWidget(MainWindow)
        self.comparative_file_dock_widget.setObjectName(u"comparative_file_dock_widget")
        self.comparative_file_dock_widget.setFont(font)
        self.comparative_file_dock_widget.setFeatures(QDockWidget.DockWidgetFloatable | QDockWidget.DockWidgetMovable)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.comparative_file_toolbox = QToolBox(self.dockWidgetContents)
        self.comparative_file_toolbox.setObjectName(u"comparative_file_toolbox")
        self.comparative_file_toolbox.setMinimumSize(QSize(304, 0))
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        self.comparative_file_toolbox.setFont(font6)
        self.comparative_file_filemanager_page = QWidget()
        self.comparative_file_filemanager_page.setObjectName(u"comparative_file_filemanager_page")
        self.comparative_file_filemanager_page.setGeometry(QRect(0, 0, 304, 531))
        self.verticalLayout_7 = QVBoxLayout(self.comparative_file_filemanager_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.comparative_file_dir_tree_view = QTreeView(self.comparative_file_filemanager_page)
        self.comparative_file_dir_tree_view.setObjectName(u"comparative_file_dir_tree_view")
        self.verticalLayout_7.addWidget(self.comparative_file_dir_tree_view)
        self.change_comparative_dir_btn = QPushButton(self.comparative_file_filemanager_page)
        self.change_comparative_dir_btn.setObjectName(u"change_comparative_dir_btn")
        font7 = QFont()
        font7.setPointSize(8)
        self.change_comparative_dir_btn.setFont(font7)
        self.verticalLayout_7.addWidget(self.change_comparative_dir_btn)
        self.comparative_file_toolbox.addItem(self.comparative_file_filemanager_page,
                                              u"V\u00fdber porovn\u00e1vacieho merania")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 304, 531))
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.textBrowser = QLabel(self.page_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setFont(font2)
        self.textBrowser.setStyleSheet("border: 1px solid black;")

        self.verticalLayout_9.addWidget(self.textBrowser)

        self.comparative_file_unload_btn = QPushButton(self.page_2)
        self.comparative_file_unload_btn.setObjectName(u"comparative_file_unload_btn")
        font8 = QFont()
        font8.setFamilies([u"Nirmala UI Semilight"])
        font8.setPointSize(8)
        font8.setBold(True)
        self.comparative_file_unload_btn.setFont(font8)

        self.verticalLayout_9.addWidget(self.comparative_file_unload_btn)

        self.comparative_file_toolbox.addItem(self.page_2, u"Porovn\u00e1van\u00e9 meranie")

        self.verticalLayout_2.addWidget(self.comparative_file_toolbox)

        self.comparative_file_dir_view_widget = QWidget(self.dockWidgetContents)
        self.comparative_file_dir_view_widget.setObjectName(u"comparative_file_dir_view_widget")
        self.comparative_file_dir_view_widget.setFont(font2)
        self.verticalLayout = QVBoxLayout(self.comparative_file_dir_view_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)

        self.verticalLayout_2.addWidget(self.comparative_file_dir_view_widget)

        self.comparative_file_dock_widget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.comparative_file_dock_widget)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menuN_stroje.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())
        self.menu_file.addAction(self.menuOtvor.menuAction())
        self.menu_file.addAction(self.action_save_as)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menuOtvor.addAction(self.actionPorovnanie)
        self.menu_settings.addAction(self.menuRe_im_zobrazenia.menuAction())
        self.menuRe_im_zobrazenia.addAction(self.actionDenn)
        self.menuRe_im_zobrazenia.addAction(self.actionNo_n)
        self.menu_about.addAction(self.actionDokument_cia)
        self.menu_about.addSeparator()
        self.menu_about.addAction(self.actionO_programe)
        self.menuN_stroje.addAction(self.actionKalibr_cia)
        self.menuN_stroje.addAction(self.action_choose_comport)
        self.measurment_controls_toolbar.addAction(self.action_stop)
        self.measurment_controls_toolbar.addAction(self.action_play)

        self.retranslateUi(MainWindow)

        self.measurement_config_menu_tabs.setCurrentIndex(0)
        self.comparative_file_toolbox.setCurrentIndex(0)

        self.devices_controls_devices_selection_volt_cbox.clear()
        self.devices_controls_devices_selection_volt_cbox.addItems(
            VOLTMETERS
        )

        self.devices_controls_devices_selection_disperse_cbox.clear()
        self.devices_controls_devices_selection_disperse_cbox.addItems(
            DISPERSE_ELEMENTS
        )

        self.measurement_config_menu_halogen_cbox.clear()
        self.measurement_config_menu_halogen_cbox.addItems(
            LIGHTS
        )

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        '''
        translates displayed text to slovak
        @param MainWindow: mainWindow of the application
        @return:
        '''
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ARTKEPS", None))
        self.action_play.setText(QCoreApplication.translate("MainWindow", u"play", None))
        self.action_stop.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.action_new.setText(QCoreApplication.translate("MainWindow", u"Nov\u00fd", None))
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017ei\u0165", None))
        self.action_save_as.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017ei\u0165 ako", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Ukon\u010di\u0165", None))
        self.actionKalibr_cia.setText(QCoreApplication.translate("MainWindow", u"Kalibr\u00e1cia", None))
        self.action_choose_comport.setText(QCoreApplication.translate("MainWindow", u"Vyber comporty", None))
        self.actionDokument_cia.setText(QCoreApplication.translate("MainWindow", u"Dokument\u00e1cia", None))
        self.actionO_programe.setText(QCoreApplication.translate("MainWindow", u"O programe", None))
        self.actionDenn.setText(QCoreApplication.translate("MainWindow", u"Denn\u00fd", None))
        self.actionNo_n.setText(QCoreApplication.translate("MainWindow", u"No\u010dn\u00fd", None))
        self.actionPorovnanie.setText(QCoreApplication.translate("MainWindow", u"Porovnávacie meranie", None))
        self.measurement_config_menu_sample_label.setText(
            QCoreApplication.translate("MainWindow", u"N\u00e1zov vzorky", None))
        self.measurement_config_menu_width_label_4.setText(QCoreApplication.translate("MainWindow", u"Teplota", None))
        self.measurement_config_menu_width_label.setText(QCoreApplication.translate("MainWindow", u"Hr\u00fabka vrstvy", None))
        self.measurement_config_menu_width_label_2.setText(
            QCoreApplication.translate("MainWindow", u"Pozn\u00e1mka k technol\u00f3gii", None))
        self.measurement_config_menu_width_label_3.setText(
            QCoreApplication.translate("MainWindow", u"Popis vzorky", None))
        self.measurement_config_menu_tabs.setTabText(self.measurement_config_menu_tabs.indexOf(self.sample_tab),
                                                     QCoreApplication.translate("MainWindow", u"Vzorka", None))
        self.measurement_config_menu_filename_label.setText(
            QCoreApplication.translate("MainWindow", u"N\u00e1zov s\u00faboru", None))
        self.measurement_config_menu_start_label.setText(
            QCoreApplication.translate("MainWindow", u"Za\u010diatok", None))
        self.measurement_config_menu_end_label.setText(QCoreApplication.translate("MainWindow", u"Koniec", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Po\u010det integr\u00e1cii", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Korekcia", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Krok motora", None))
        self.measurement_config_menu_tabs.setTabText(
            self.measurement_config_menu_tabs.indexOf(self.measurement_config_tab),
            QCoreApplication.translate("MainWindow", u"Meranie", None))
        self.measurement_config_menu_ref_label.setText(QCoreApplication.translate("MainWindow", u"Ref", None))
        self.measurement_config_menu_min_sensitivity_label.setText(QCoreApplication.translate("MainWindow", u"Min. auto senzitivita", None))
        self.measurement_config_menu_span_label.setText(QCoreApplication.translate("MainWindow", u"Rozsah", None))
        self.measurement_config_menu_span_auto_check.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.measurement_config_menu_time_const_label.setText(
            QCoreApplication.translate("MainWindow", u"\u010casov\u00e1 kon\u0161tanta- pre", None))

        self.measurement_config_menu_time_const_label_post.setText(
            QCoreApplication.translate("MainWindow", u"\u010casov\u00e1 kon\u0161tanta- post", None))

        self.measurement_config_menu_angle_label.setText(
            QCoreApplication.translate("MainWindow", u"F\u00e1zov\u00fd posun", None))
        self.measurement_config_menu_tabs.setTabText(self.measurement_config_menu_tabs.indexOf(self.voltmeter_tab),
                                                     QCoreApplication.translate("MainWindow", u"Milivoltmeter", None))
        self.measurement_config_menu_halogen_label.setText(QCoreApplication.translate("MainWindow", u"Typ", None))
        self.measurement_config_menu_laser_label.setText(
            QCoreApplication.translate("MainWindow", u"Pozn\u00e1mka", None))
        self.measurement_config_menu_tabs.setTabText(self.measurement_config_menu_tabs.indexOf(self.light_source_tab),
                                                     QCoreApplication.translate("MainWindow", u"Zdroj svetla", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Detektor", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Detaily", None))
        self.measurement_config_menu_tabs.setTabText(self.measurement_config_menu_tabs.indexOf(self.detector_tab),
                                                     QCoreApplication.translate("MainWindow", u"Detektor", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Vstupn\u00e1 \u0161trbina", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Šírka", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Výška", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"V\u00fdstupn\u00e1 \u0161trbina", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Šírka", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Optick\u00fd filter", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"názov", None))

        self.measurement_config_menu_tabs.setTabText(self.measurement_config_menu_tabs.indexOf(self.monochromator_tab),
                                                     QCoreApplication.translate("MainWindow", u"Monochrom\u00e1tor",
                                                                                None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"S\u00fabor", None))
        self.menuOtvor.setTitle(QCoreApplication.translate("MainWindow", u"Otvori\u0165", None))
        self.menu_settings.setTitle(QCoreApplication.translate("MainWindow", u"Nastavenia", None))
        self.menuRe_im_zobrazenia.setTitle(QCoreApplication.translate("MainWindow", u"Re\u017eim zobrazenia", None))
        self.menu_about.setTitle(QCoreApplication.translate("MainWindow", u"Pomoc", None))
        self.menuN_stroje.setTitle(QCoreApplication.translate("MainWindow", u"N\u00e1stroje", None))
        self.measurment_controls_toolbar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.devices_controls_devices_selection_label.setText(
            QCoreApplication.translate("MainWindow", u"Zariadenia", None))
        self.devices_controls_devices_selection_volt_label.setText(
            QCoreApplication.translate("MainWindow", u"Milivoltmeter", None))
        self.devices_controls_devices_selection_disperse_label.setText(
            QCoreApplication.translate("MainWindow", u"Disperzn\u00fd prvok", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Jednotky", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Uhol", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Angstrom", None))
        self.devices_controls_engine_positioning_label.setText(
            QCoreApplication.translate("MainWindow", u"Polohovanie motora", None))
        self.devices_controls_engine_positioning_left_btn.setText("")
        self.devices_controls_engine_positioning_right_btn.setText("")
        self.devices_controls_goto_label.setText(QCoreApplication.translate("MainWindow", u"Cho\u010f na", None))
        self.devices_controls_goto_btn.setText(QCoreApplication.translate("MainWindow", u"Cho\u010f", None))
        self.devices_controls_engine_settings_label.setText(
            QCoreApplication.translate("MainWindow", u"Inicializovanie polohy motora", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Uhol", None))
        self.devices_controls_calibration_btn.setText(QCoreApplication.translate("MainWindow", u"Inicializuj", None))
        self.devices_controls_angle_label.setText(
            QCoreApplication.translate("MainWindow", u"Vlnov\u00e1 d\u013a\u017eka", None))
        self.change_comparative_dir_btn.setText(
            QCoreApplication.translate("MainWindow", u"Zmeni\u0165 adres\u00e1r", None))
        self.comparative_file_toolbox.setItemText(
            self.comparative_file_toolbox.indexOf(self.comparative_file_filemanager_page),
            QCoreApplication.translate("MainWindow", u"V\u00fdber porovn\u00e1vacieho merania", None))
        self.comparative_file_unload_btn.setText(QCoreApplication.translate("MainWindow", u"Zru\u0161", None))
        self.comparative_file_toolbox.setItemText(self.comparative_file_toolbox.indexOf(self.page_2),
                                                  QCoreApplication.translate("MainWindow",
                                                                             u"Porovn\u00e1van\u00e9 meranie", None))
    # retranslateUi
