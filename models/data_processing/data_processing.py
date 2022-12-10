
from PySide6.QtCore import Signal, QObject

from measurementSettings import measurementSettings
import os


#zistit co presne sa vykresluje v grafe - ci na y je intenzita
# a na x je len cas

#skontrolovat ci je dobre ten graf
#spytat sa ze ako zistim presne z teh tabulkz mriezky spravne udaje
#od martina zistit ake udaje mam posielat loggerovi  ---- a
#ako osetrit chyby - vyhadzovat errory?? poslat spravu loggeru??
#napriklad ako v loadMeasurement
##ci maju ist vsetky subory merania do saved_measurements
##ze ako sa da spravit to aby sa tie naloadovane
#data v hlavicke dali do formularu

#spravit error vlastny - message - v measurementcontroler sa to bude logovat
#navrh dokoncit


class DataProcessing(QObject):
    setSettings_ = Signal(measurementSettings)

    def __init__(self):
        super(DataProcessing, self).__init__()
        self.fileName = ""
        self.path = self.getDefaultPath()
        self.beginingOfData = '{: <20s}\t{: <20s}\t{}\n'.format("ALFA[A°]", "VLNOVÁ DĹŽKA[A]", "INTENZITA[mV]")
            #"ALFA[A°]\t\t\tVLNOVÁ DĹŽKA[A]\t\t\tINTENZITA[mV]\n"
        self.settings = None
        self.setSettings_.connect(lambda settings: self.setSettings(settings))

    def getDefaultPath(self):
        path = os.path.dirname(os.path.abspath(__file__))
        dirs = path.split("\\")
        rootName = "spektra"
        targetDir = "\\saved_measurements\\"
        indexRoot = len(dirs) - dirs[::-1].index(rootName) - 1
        return "\\".join(dirs[:indexRoot + 1]) + targetDir

    def setSettings(self, settings):
        self.settings = settings

    def createNewFile(self):
        if not self.settings.checkLegend():
            return False

        if not self.writeLegend():
            return False

        self.settings.storeLastLegend()
        return True


    def addMeasurement(self, angle, waveLength, intensity):
        if self.fileName == "":
            return False
        with open(self.path + self.fileName, 'a', encoding="utf-8") as currentFile:
            line = '\n{: <20s}\t{: <20s}\t{}'.format(str(angle), str(waveLength), str(intensity))
            currentFile.write(line)
        return True

    def writeLegend(self):
        if self.fileName == "":
            return False

        with open(self.path + self.fileName, 'w', encoding="utf-8") as currentFile:
            currentFile.write(str(self.settings) + "\n\n")
            currentFile.write(self.beginingOfData)
        return True

    def setFileName(self, name):
        self.fileName = name + ".txt"

    def setFilePath(self, path):
        if path[-1:] != "\\":
            path += "\\"
        self.path = path

    def loadMeasurements(self, fileName):

        measurements = []
        with open(fileName, 'r', encoding="utf-8") as f:
            line = f.readline()
            while line != '' and line != self.beginingOfData:
                line = f.readline()

            if line == '':
                return measurements

            measurementLine = f.readline()
            while measurementLine == "\n":
                measurementLine = f.readline()

            while measurementLine != '':
                # treba osetrit to ak subor nie je v danom formate
                try:
                    alfa, waveLength, intensity = measurementLine.split("\t")
                    waveLength = waveLength.replace(" ", "")
                    intensity = intensity.replace(" ", "")
                    measurements.append([float(waveLength),
                                         float(intensity)])
                except:
                    return []
                measurementLine = f.readline()

        return measurements

