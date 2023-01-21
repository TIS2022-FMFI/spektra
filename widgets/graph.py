import pyqtgraph as pg
from PySide6.QtCore import QFileInfo
from pyqtgraph.Qt import QtCore
from models.data_processing.dataProcessing import DataProcessing
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
        super(Graph, self).__init__(parent)
        self.currentX = []
        self.currentY = []
        self.oldX = []
        self.oldY = []
        self.setBackground('w')
        self.styles = {'color': 'r', 'font-size': '20px'}
        self.setLabel('left', 'Intenzita [mV]', **self.styles)
        self.setLabel('bottom', 'Vlnová dĺžka [A°]', **self.styles)
        #self.getPlotItem().setAxisItems({"bottom": CustomAxis(orientation="bottom", text="Vlnová dĺžka [A°]")})
        self.addLegend()
        self.showGrid(x=True, y=True)
        self.plotGraph()

    def add_views(self, views):
        self.view = views

    def addMeasurement(self, measurements, current):
        if current:
            for measurement in measurements:
                self.currentX.append(measurement[0])
                self.currentY.append(measurement[1])
        else:
            self.oldX = []
            self.oldY = []
            for measurement in measurements:
                self.oldX.append(measurement[0])
                self.oldY.append(measurement[1])

    def plotGraph(self):
        self.clear()
        self.plot(self.currentX, self.currentY, name="Momentálne meranie",
                              pen='b', symbol='o', symbolSize=15,
                              symbolBrush=('b'))

        if len(self.currentX) != 0 and len(self.currentY) != 0:
            self.setLabel('top',
                    str([self.currentX[-1], self.currentY[-1]]), **self.styles)


        if len(self.oldX) != 0 and len(self.oldY) != 0:
            self.plot(self.oldX, self.oldY, name="Staršie meranie",
                              pen='r', symbol='o', symbolSize=15,
                              symbolBrush=('r'))

    def dragEnterEvent(self, event):
        def is_utf8_encoded(mime_data):
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
        mime_data = event.mimeData()
        file_url = mime_data.urls()[0]
        file_path = QFileInfo(file_url.toLocalFile()).absoluteFilePath()
        loaded_settings, measurements = DataProcessing().load_old_file(file_path)
        self.addMeasurement(measurements, False)
        self.plotGraph()
        self.view.widgets.textBrowser.setText(str(loaded_settings))
        event.accept()

    def dragLeaveEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        event.accept()






