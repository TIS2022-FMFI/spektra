from datetime import datetime
from datetime import date

#spytat sa ako je to s nazvom suboru- ci cela cesta
#alebo budeme mat nejaky priecinok kde sa budu ukladat

class DataProcessing:

    def __init__(self):
        self._legend = dict()
        self._legend["typeOfDispersingElement"] = "mriežka"
        self._legend["typeSensitivity"] = "AUTO"
        self.currentFileName = ""
        self.oldFileName = ""

    def createNewFile(self):
        today = date.today()
        self._legend["date"] = today.strftime('%d-%m-%Y')
        now = datetime.now()
        self._legend["time"] = now.strftime("%H:%M:%S")
        if not self.checkLegend():
            return False

        self.writeLegend()

        self.storeLastLegend()

        return True

    def addMeasurement(self, intensity):
        if self.currentFileName == "":
            return False
        currentFile = open(self.currentFileName, 'a')
        #blablavla
        currentFile.close()
        return True

    def checkLegend(self):
        mandatory = ["nameSample", "noteToTech", "thickness", "reference", "temperature", "nameOfDispersingElement",
                    "typeOfDispersingElement", "inputCreviceWidth", "inputCreviceHeight", "outputCreviceWidth",
                     "outputCreviceHeight", "opticalFilter", "typeOfDetector", "additionalInfoDetector",
                    "typeOfLight", "nameOfLight",  "stepOfMotor", "numberOfMitigations", "correction",
                     "lockIn", "lockInReference", "lockInFilter", "phaseShift", "timeConstante"]
        alternatives = [("startAngle", "startAngstrom"),
                        ("endAngle", "endAngstrom")]

        for legendType in mandatory:
            if legendType not in self._legend.keys():
                return False
        for alternative in alternatives:
            oneAltIsPresent = False
            for oneAlt in alternative:
                if oneAlt in self._legend.keys():
                    oneAltIsPresent = True
            if not oneAltIsPresent:
                return False

        return True

    def writeLegend(self):
        if self.currentFileName == "":
            return False

        with open(self.currentFileName, 'w',  encoding="utf-8") as currentFile:
            currentFile.write("VZORKA:\n")
            currentFile.write("názov vzorky: " +
                              self._legend["nameSample"] + "\n")
            currentFile.write("poznámka k technológií: " +
                              self._legend["noteToTech"] + "\n")
            currentFile.write("hrúbka: " +
                              self._legend["thickness"] + "\n")
            currentFile.write("referencie: " +
                              self._legend["reference"] + "\n")
            currentFile.write("teplota: " +
                              self._legend["temperature"] + "\n")

            currentFile.write("DISPERZNÝ ELEMENT:\n")
            currentFile.write(self._legend["typeOfDispersingElement"] +
                                " " +
                              self._legend["nameOfDispersingElement"] + "\n")

            currentFile.write("MONOCHROMÁTOR:\n")
            currentFile.write("vstupná štrbina (hrúbka, výška): " +
                              self._legend["inputCreviceWidth"] + " " +
                            self._legend["inputCreviceHeight"] + "\n")
            currentFile.write("výstupná štrbina (hrúbka, výška): " +
                              self._legend["outputCreviceWidth"] + " " +
                            self._legend["outputCreviceHeight"] + "\n")
            currentFile.write("optický filter: " +
                              self._legend["opticalFilter"] + "\n")

            #toto treba este specifikovat
            currentFile.write("DETEKTOR:\n")
            currentFile.write(self._legend["typeOfDetector"] + " " +
                              self._legend["additionalInfoDetector"] + "\n")

            currentFile.write("BÚDIACE SVETLO:\n")
            currentFile.write(self._legend["typeOfLight"] + " " +
                              self._legend["nameOfLight"] + "\n")

            currentFile.write("MERANIE:\n")
            currentFile.write(self._legend["nameSample"] + "\n")
            if "startAngle" in self._legend.keys():
                type = "°"
                start = self._legend["startAngle"]
                stop = self._legend["endAngle"]
            else:
                type = "A°"
                start = self._legend["startAngstrom"]
                stop = self._legend["endAngstrom"]
            currentFile.write("počiatočná vlnová dĺžka ["
                                + type + "]: " + start  + "\n")
            currentFile.write("koncová vlnová dĺžka ["
                                + type + "]: " + stop + "\n")
            currentFile.write("krok motora [v impulzoch]: " +
                              self._legend["stepOfMotor"] + "\n")
            currentFile.write("počet mitigácií: " +
                              self._legend["numberOfMitigations"] + "\n")
            currentFile.write("korekcia [A°]: " +
                              self._legend["correction"] + " \n")

            currentFile.write("MILIVOLTMENTER:\n")
            currentFile.write(self._legend["lockIn"] + "\n")
            currentFile.write("citlivosť: " +
                    self._legend["typeSensitivity"] + "\n")
            currentFile.write("referencia [Hz]: " +
                        self._legend["lockInReference"] + " \n")
            currentFile.write("filters: " +
                        self._legend["lockInFilter"] + "\n")
            currentFile.write("fázový posun: " +
                        self._legend["phaseShift"] + "\n")
            currentFile.write("časová konštanta: " +
                              self._legend["timeConstante"]
                              + "\n")

        return True

    def loadLastLegend(self):
        pass

    def storeLastLegend(self):
        pass

    def setFileName(self, name):
        self.currentFileName = name

    def setOldFileName(self, name):
        self.oldFileName = name

    def setNameSample(self, name):
        self._legend["nameSample"] = name

    def setNoteToTechnology(self, note):
        self._legend["noteToTech"] = note

    def setThickness(self, thickness):
        self._legend["thickness"] = thickness

    def setReference(self, ref):
        self._legend["reference"] = ref

    def setTemperature(self, temperature):
        self._legend["temperature"] = temperature

    def setNameDispersingElement(self, disperElem):
        self._legend["nameOfDispersingElement"] = disperElem

    def setTypeDispersingElement(self, disperElem):
        self._legend["typeOfDispersingElement"] = disperElem

    # crevice = strbina
    def setInputCreviceWidth(self, width):
        self._legend["inputCreviceWidth"] = width

    def setInputCreviceHeight(self, height):
        self._legend["inputCreviceHeight"] = height

    def setOutputCreviceWidth(self, width):
        self._legend["outputCreviceWidth"] = width

    def setOutputCreviceHeight(self, height):
        self._legend["outputCreviceHeight"] = height

    def setOpticalFilter(self, filter):
        self._legend["opticalFilter"] = filter

    #spytat sa gregusa na blizsie info k detektoru
    def setTypeDetector(self, detector):
        self._legend["typeOfDetector"] = detector

    def setAdditionalInfoDetector(self, info):
        self._legend["additionalInfoDetector"] = info

    def setTypeOfLight(self, type):
        self._legend["typeOfLight"] = type

    def setNameOfLight(self, name):
        self._legend["nameOfLight"] = name

    # alternativy podla toho ci sa zvoli uhol alebo angstrom
    def setStartAngle(self, angle):
        self._legend["startAngle"] = angle

    def setStartAngstrom(self, angstrom):
        self._legend["startAngstrom"] = angstrom

    def setEndAngle(self, angle):
        self._legend["endAngle"] = angle

    def setEndAngstrom(self, angstrom):
        self._legend["endAngstrom"] = angstrom

    def setStepOfMotor(self, step):
        self._legend["stepOfMotor"] = step

    def setNumberOfMitigations(self, number):
        self._legend["numberOfMitigations"] = number

    def setCorrection(self, correction):
        self._legend["correction"] = correction

    def setLockIn(self, type):
        self._legend["lockIn"] = type
    def setLockInReference(self, reference):
        self._legend["lockInReference"] = reference

    def setLockInFilter(self, filter):
        self._legend["lockInFilter"] = filter

    def setPhaseShift(self, shift):
        self._legend["phaseShift"] = shift

    def setTimeConstant(self, constante):
        self._legend["timeConstante"] = constante




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
