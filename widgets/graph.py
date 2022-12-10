import pyqtgraph as pg
from pyqtgraph.Qt import QtCore


class Graph(pg.PlotWidget):
    def __init__(self, parent):
        super(Graph, self).__init__(parent)
        self.currentX = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.currentY = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        self.oldX = []
        self.oldY = []

        self.setBackground('w')
        self.styles = {'color': 'r', 'font-size': '20px'}
        self.setLabel('left', 'Intenzita [mV]', **self.styles)
        self.setLabel('bottom', 'Vlnová dĺžka [A°]', **self.styles)

        self.addLegend()

        self.showGrid(x=True, y=True)

        self.plotGraph()


    def addMeasurement(self, measurements, current):
        if current:
            for measurement in measurements:
                self.currentX.append(measurement[0])
                self.currentY.append(measurement[1])
        else:
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


    '''
    
    ###TESTOVANIE

    currentX = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    currentY = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
    old = [[1, 50], [2, 35] , [3, 44],
            [4, 22], [5, 38], [6, 32], [7, 27],
            [8, 38], [9, 32], [10, 44]]
    g = Graph(window.graphWidget)
    g.plot()
    
    for i in range(10):
        g.plot()
        g.addMeasurement([[currentX[i], currentY[i]]], True)

    g.addMeasurement(old, False)
    g.plot()

    '''




