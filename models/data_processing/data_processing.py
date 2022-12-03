
#zistit co presne sa vykresluje v grafe - ci na y je intenzita
# a na x je len cas

class DataProcessing:

    def __init__(self):
        self.fileName = ""
        self.beginingOfData = "ALFA[A°]\tVLNOVÁ DĹŽKA[A]\nINTENZITA[mV]°"

    def createNewFile(self, settings):
        if not settings.checkLegend():
            return False

        if not self.writeLegend(settings):
            return False

        settings.storeLastLegend()

        return True

    #NEDOKONCENE
    def addMeasurement(self, intensity):
        if self.fileName == "":
            return False
        with open(self.fileName, 'a') as currentFile:
            #blablabla
            pass
        return True

    def writeLegend(self, settings):
        if self.fileName == "":
            return False

        with open(self.fileName, 'w', encoding="utf-8") as currentFile:
            currentFile.write(str(settings) + "\n\n")
            currentFile.write(self.beginingOfData)
        return True

    def setFileName(self, name):
        self.fileName += name + ".txt"

    def setFilePath(self, path):
        if path[-1:] != "\\":
            path += "\\"
        self.fileName = path + self.fileName

    def loadMeasurements(self, fileName):
        #upravit co sa vracia
        measurements = []
        with open(fileName, 'r') as f:
            line = f.readline()
            while line != self.beginingOfData:
                line = f.readline()
            measurementLine = f.readline()
            while measurementLine != '':
                alfa, waveLength, intensity = measurementLine.split("\t")
                measurements.append([alfa, waveLength, intensity])
                measurementLine = f.readline()






####    TESTY
'''
    dp = DataProcessing()
    dp.setFileName("C:\\Users\\lucin\\OneDrive\\Desktop\\spektra\\spektra\\mojPokusOHlavicku.txt")
    dp.setNameSample("utorkajsia vzorka")
    dp.setNoteToTechnology("blabla")
    dp.setThickness("11.3")
    dp.setReference("ref")
    dp.setTemperature("15.4")
    dp.setNameDispersingElement("M465645")
    dp.setInputCreviceWidth("3,4")
    dp.setInputCreviceHeight("2,4")
    dp.setOutputCreviceWidth("5,3")
    dp.setOutputCreviceHeight("3,4")
    dp.setOpticalFilter("filter")
    dp.setTypeDetector("Si-fotodioda")
    dp.setAdditionalInfoDetector("nazov")
    dp.setTypeOfLight("Laser")
    dp.setNameOfLight("nadupany")
    dp.setStartAngstrom("340")
    dp.setEndAngstrom("200")
    dp.setStepOfMotor("1.3")
    dp.setNumberOfMitigations("1")
    dp.setCorrection("2")
    dp.setLockIn("Lockin nano voltmeter type 232")
    dp.setLockInReference("1.4")
    dp.setLockInFilter("signal filters")
    dp.setPhaseShift("1")
    dp.setTimeConstant("1")
    dp.createNewFile()
    '''
