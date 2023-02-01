import pyqtgraph as pg
from PySide6.QtCore import QFileInfo
from pyqtgraph.Qt import QtCore

from errors.data_processing_error import DataProcessingError
from models.data_processing.dataProcessing import DataProcessing
from models.logger.constants import *
class CustomAxis(pg.AxisItem):

    # src: https://stackoverflow.com/questions/56890481/how-to-set-pyqtgraph-axis-label-offset
    @property
    def nudge(self):
        if not hasattr(self, "_nudge"):
            self._nudge = 5
        return self._nudge

    @nudge.setter
    def nudge(self, nudge):
        self._nudge = nudge
        s = self.size()
        # call resizeEvent indirectly
        self.resize(s + QtCore.QSizeF(1, 1))
        self.resize(s)

    def resizeEvent(self, ev=None):
        # s = self.size()

        ## Set the position of the label
        nudge = 5
        if self.label is None:  # self.label is set to None on close, but resize events can still occur.
            self.picture = None
            return

        br = self.label.boundingRect()
        p = QtCore.QPointF(0, 0)
        if self.orientation == 'left':
            p.setY(int(self.size().height() / 2 + br.width() / 2))
            p.setX(-nudge)
        elif self.orientation == 'right':
            p.setY(int(self.size().height() / 2 + br.width() / 2))
            p.setX(int(self.size().width() - br.height() + nudge))
        elif self.orientation == 'top':
            p.setY(-nudge)
            p.setX(int(self.size().width() / 2. - br.width() / 2.))
        elif self.orientation == 'bottom':
            p.setX(int(self.size().width() / 2. - br.width() / 2.))
            p.setY(int(self.size().height() - br.height() + nudge))
        self.label.setPos(p)
        self.picture = None


class Graph(pg.PlotWidget):
    def __init__(self, parent):
        '''
        sets up empty graph with correct style and labels
        @param parent: parent widget of graph widget
        '''
        super(Graph, self).__init__(parent)
        self.view = None
        self.currentX = []
        self.currentY = []
        self.oldX = []
        self.oldY = []
        self.setBackground('w')
        self.styles = {'color': 'r', 'font-size': '20px'}
        self.setLabel('left', 'Intenzita [mV]', **self.styles)
        self.setLabel('bottom', 'Vlnová dĺžka [A°]', **self.styles)
        self.addLegend()
        self.showGrid(x=True, y=True)
        self.plotGraph()

    def add_views(self, views):
        '''
        adds reference to all widgets in gui of application
        @param views: reference to all widgets in gui
        '''
        self.view = views

    def add_logger(self, logger):
        '''
        stores reference to logger
        @param logger: reference to logger
        @return:
        '''
        self.logger = logger

    def initialize(self):
        self.currentX = []
        self.currentY = []

    def addMeasurement(self, measurements, current):
        '''
        adds new data from current ongoing measurement or adds all measured data
        from a past measurement for comparision
        @param measurements: two-dimensional list, which contains coordinates of new points in graph
        @param current: boolean variable which switches between adding old and current measurement data
        @return:
        '''
        if current:
            self.add_current_measurements(measurements)
        else:
            self.add_old_measurements(measurements)

    def add_old_measurements(self, measurements):
        '''
        adds all measured data from a past measurement for comparision
        @param measurements: two-dimensional list, which contains coordinates of new points in graph
        @return:
        '''
        self.oldX = []
        self.oldY = []
        for measurement in measurements:
            self.oldX.append(measurement[0])
            self.oldY.append(measurement[1])

    def add_current_measurements(self, measurements):
        '''
        adds new data from current ongoing measurement
        @param measurements: two-dimensional list, which contains coordinates of new points in graph
        @return:
        '''
        for measurement in measurements:
            self.currentX.append(measurement[0])
            self.currentY.append(measurement[1])

    def plotGraph(self):
        '''
        plots graph with current data displayed in blue and optionally with
        old data in red
        @return:
        '''
        self.clear()
        self.plot(self.currentX, self.currentY, name="Momentálne meranie",
                              pen='b', symbol='o', symbolSize=8,
                              symbolBrush=('b'))

        if len(self.currentX) != 0 and len(self.currentY) != 0 and self.view is not None:
            self.view.widgets.devices_controls_current_wavelength_widget.setText(
                "Posledné namerané hodnoty: x=" + str(self.currentX[-1]) + ", y="
                + str(self.currentY[-1])
            )


        if len(self.oldX) != 0 and len(self.oldY) != 0:
            self.plot(self.oldX, self.oldY, name="Staršie meranie",
                              pen='r', symbol='o', symbolSize=5,
                              symbolBrush=('r'))
        return

    def dragEnterEvent(self, event):
        '''
        processes drag enter event over graph widget
        @param event: drag enter event
        @return:
        '''
        def is_utf8_encoded(mime_data):
            '''
            finds out if the item dragged over graph has the right format
            @param mime_data: item that is dragged over graph
            @return: boolean value representing if the format is right
            '''
            if mime_data.hasUrls():
                file_url = mime_data.urls()[0]
                file_path = QFileInfo(file_url.toLocalFile()).absoluteFilePath()
                with open(file_path, "r", encoding="utf-8") as file:
                    try:
                        file.read()
                        return True
                    except UnicodeDecodeError:
                        return False
            return False

        mime_data = event.mimeData()
        if is_utf8_encoded(mime_data):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        '''
        processes drop event. If file is dropped then displays data and legend from this file
        in the graph and in the label element
        @param event: drop event
        @return:
        '''
        mime_data = event.mimeData()
        file_url = mime_data.urls()[0]
        file_path = QFileInfo(file_url.toLocalFile()).absoluteFilePath()

        try:
            loaded_settings, measurements = DataProcessing(self.view).load_old_file(file_path)
        except DataProcessingError as e:
            self.logger.log(WARNING, e.message, True)
            event.accept()
            return

        self.addMeasurement(measurements, False)
        self.plotGraph()
        self.view.widgets.textBrowser.setText(str(loaded_settings))
        event.accept()

    def dragLeaveEvent(self, event):
        '''
        processes drag leave event
        @param event: drag leave event
        @return:
        '''
        event.accept()

    def dragMoveEvent(self, event):
        '''
        processes drag move event
        @param event: drag move event
        @return:
        '''
        event.accept()






