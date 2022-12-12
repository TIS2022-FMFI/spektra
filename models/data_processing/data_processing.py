
from PySide6.QtCore import Signal, QObject

from measurementSettings import measurementSettings
from errors.data_processing_error import DataProcessingError
import os

#v navrhu zmenit strukturu suboru

class DataProcessing(QObject):
    setSettings_ = Signal(measurementSettings)

    def __init__(self):
        super(DataProcessing, self).__init__()
        self.fileName = ""
        self.path = self.getDefaultPath()
        self.beginingOfData = '{: <20s}\t{: <20s}\t{}\n'.format("ALFA[A°]", "VLNOVÁ DĹŽKA[A]", "INTENZITA[mV]")
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
            raise DataProcessingError("Legenda nie je kompletne vyplnená. Nie je možne vytvoriť nový súbor pre meranie.")

        self.writeLegend()
        self.settings.storeLastJsonLegend()

    def addMeasurement(self, angle, waveLength, intensity):
        if self.fileName == "":
            DataProcessingError("Nie je vyplnené meno súboru. Nie je možné pridať najnovšie meranie do súboru.")
        with open(self.path + self.fileName, 'a', encoding="utf-8") as currentFile:
            line = '\n{: <20s}\t{: <20s}\t{}'.format(str(angle), str(waveLength), str(intensity))
            currentFile.write(line)

    def writeLegend(self):
        if self.fileName == "":
            raise DataProcessingError("Nie je vyplnené meno súboru. Nie je možné vytvoriť nový súbor pre meranie.")

        with open(self.path + self.fileName, 'w', encoding="utf-8") as currentFile:
            currentFile.write(str(self.settings) + "\n\n")
            currentFile.write(self.beginingOfData)

    def setFileName(self, name):
        self.fileName = name + ".txt"

    def setFilePath(self, path):
        if path[-1:] != "\\":
            path += "\\"
        self.path = path

    def loadMeasurements(self, fileName):
        with open(fileName, 'r', encoding="utf-8") as f:
            stringLegend = self.readLegendFromFile(f)
            loadedSettings = self.settings.loadStringLegend(stringLegend)
            measurements = self.readMeasurementsFromFile(f)

        if measurements == []:
            raise DataProcessingError("Načítaný súbor nie je v správnom formáte. Neobsahuje nameraná údaje.")

        return loadedSettings, measurements

    def readMeasurementsFromFile(self, f):
        measurementLine = f.readline()
        while measurementLine == "\n":
            measurementLine = f.readline()

        measurements = []

        while measurementLine != '':
            try:
                alfa, waveLength, intensity = measurementLine.split("\t")
                waveLength = waveLength.replace(" ", "")
                intensity = intensity.replace(" ", "")
                measurements.append([float(waveLength),
                                     float(intensity)])
                measurementLine = f.readline()
            except:
                raise DataProcessingError("Načítaný súbor nie je v správnom formáte. Namerané údaje sú v zlom formáte.")


        return measurements

    def readLegendFromFile(self, f):
        line = f.readline()
        stringLegend = ""
        while line != '' and line != self.beginingOfData:
            stringLegend += line + "\n"
            line = f.readline()

        if line == '':
            raise DataProcessingError("Načítaný súbor nie je v správnom formáte. Neobsahuje nameraná údaje.")

        return stringLegend

