import json
from datetime import datetime
from datetime import date
import os
from errors.data_processing_error import DataProcessingError


class measurementSettings:
    mandatory = ["nameSample", "noteToTech", "thickness", "measurementOfSample", "temperature",
                 "typeOfDispersingElement", "nameOfDispersingElement",
                  "inputCreviceBegin", "inputCreviceEnd", "outputCreviceBegin",
                 "outputCreviceEnd", "opticalFilter", "typeOfDetector", "additionalInfoDetector",
                 "typeOfLight", "nameOfLight",
                 "stepOfMotor", "numberOfIntegrations", "correction",
                 "lockIn", "typeSensitivity", "lockInReference",
                 "range", "phaseShift", "timeConstante",
                  ]
    nonMandatory = ["date", "time"]
    KEY_BEFORE_ALTERNATIVES = "nameOfLight"
    ANGLE_INDEX = 0
    ANGSTROM_INDEX = 1
    SYMBOLS = ["°", "A°"]
    alternatives = [("startAngle", "endAngle"),
                    ("startAngstrom", "endAngstrom")]


    def __init__(self):
        self.legend = dict()
        self.setSetting("typeOfDispersingElement", "mriežka")
        self.setSetting("typeSensitivity", "AUTO")

        script_dir = os.path.dirname(__file__)
        rel_path = "models/data_processing/lastSettings.txt"
        self.jsonName = os.path.join(script_dir, rel_path)



    def setSetting(self, key, param):
        all = self.mandatory + [key for alter in self.alternatives
                                for key in alter] + self.nonMandatory
        if key in all:
            self.legend[key] = str(param)
            return True
        return False


    def checkLegend(self):
        for legendType in self.mandatory:
            if legendType not in self.legend.keys():
                return False
        for alt in self.alternatives:
            if all(map(lambda key : key in self.legend.keys(), alt)):
                return True
        return False


    def __str__(self):
        alternativeIndex = self.ANGSTROM_INDEX
        if "startAngle" in self.legend.keys():
            alternativeIndex = self.ANGLE_INDEX

        dateCurrent = self.setCurrentDate()
        timeCurrent = self.setCurrentTime()

        return "VZORKA:\n" + \
            "názov vzorky: " + self.legend["nameSample"] + "\n" + \
            "poznámka k technológií: " +  self.legend["noteToTech"] + "\n" + \
            "hrúbka: " + self.legend["thickness"] + "\n" + \
            "meranie vzorky: " + self.legend["measurementOfSample"] + "\n" +  \
            "teplota: " + self.legend["temperature"] + "\n" + \
            "DISPERZNÝ ELEMENT:\n" + \
            self.legend["typeOfDispersingElement"] + ", " +  \
                     self.legend["nameOfDispersingElement"] + "\n" +   \
            "MONOCHROMÁTOR:\n" + \
            "vstupná štrbina (začiatok, koniec): " + \
                self.legend["inputCreviceBegin"] + ", " + \
                self.legend["inputCreviceEnd"] + "\n" + \
            "výstupná štrbina (začiatok, koniec): " +    \
                self.legend["outputCreviceBegin"] + ", " + \
                self.legend["outputCreviceEnd"] + "\n" +  \
            "optický filter: " + self.legend["opticalFilter"] + "\n" + \
            "DETEKTOR:\n" + \
            "PMT: " + self.legend["typeOfDetector"] + ", " +   \
                self.legend["additionalInfoDetector"] + "\n" + \
            "BÚDIACE SVETLO:\n" +   \
            self.legend["typeOfLight"] + ", " + \
                self.legend["nameOfLight"] + "\n" + \
            "MERANIE:\n" + \
            dateCurrent + ", " + timeCurrent + "\n" + \
            "počiatočná ["  \
                + self.SYMBOLS[alternativeIndex] + "]: " + \
                self.legend[self.alternatives[alternativeIndex][0]] + "\n" + \
            "koncová [" \
                + self.SYMBOLS[alternativeIndex] + "]: " \
               + self.legend[self.alternatives[alternativeIndex][1]] + "\n" + \
            "krok motora [v impulzoch]: " + \
                self.legend["stepOfMotor"] + "\n" + \
            "počet integrácií: " + \
                self.legend["numberOfIntegrations"] + "\n" + \
            "korekcia [A°]: " + \
                self.legend["correction"] + "\n" + \
            "MILIVOLTMENTER:\n" + \
            self.legend["lockIn"] + "\n" + \
            "citlivosť: " + self.legend["typeSensitivity"] + "\n" + \
            "referencia [Hz]: " + self.legend["lockInReference"] + "\n" + \
            "range: " + self.legend["range"] + "\n" + \
            "fázový posun: " + self.legend["phaseShift"] + "\n" + \
            "časová konštanta: " + self.legend["timeConstante"]

    def setCurrentTime(self):
        today = date.today()
        timeCurrent = today.strftime("%H:%M:%S")
        if "time" in self.legend.keys():
            timeCurrent = self.legend["time"]
        return timeCurrent

    def setCurrentDate(self):
        now = datetime.now()
        dateCurrent = now.strftime('%d-%m-%Y')
        if "date" in self.legend.keys():
            dateCurrent = self.legend["date"]
        return dateCurrent

    def loadStringLegend(self, strLegend):
        strLegend = strLegend.replace(":\n", ": \n")
        linesOfLegend = strLegend.split("\n")

        alternative, settingField = self.settingFieldsFromLines(linesOfLegend)
        oldSettings = self.settingFieldsToMeasurSetting(alternative, settingField)

        if not oldSettings.checkLegend():
            raise DataProcessingError("Legenda v načítanom súbore je v nespravnom formáte.")
        return oldSettings

    def settingFieldsFromLines(self, linesOfLegend):
        alternative = self.ANGLE_INDEX
        settingField = []
        for i in range(len(linesOfLegend)):
            line = linesOfLegend[i]
            if "počiatočná" in line and "A°" in line:
                alternative = self.ANGSTROM_INDEX
            if ": " in line:
                line = line.strip()
                line = line[line.index(":") + 2:]
            if len(line) > 0:
                settingField.extend(line.split(", "))
        return alternative, settingField

    def settingFieldsToMeasurSetting(self, alternative, settingField):
        oldSettings = measurementSettings()
        iMandatory = 0
        iSettings = 0
        while iSettings < len(settingField):
            key = self.mandatory[iMandatory]
            value = settingField[iSettings]
            oldSettings.setSetting(key, value)
            iSettings += 1
            iMandatory += 1
            if key == self.KEY_BEFORE_ALTERNATIVES:
                value = settingField[iSettings]
                oldSettings.setSetting("date", value)
                iSettings += 1
                value = settingField[iSettings]
                oldSettings.setSetting("time", value)
                iSettings += 1
                key = self.alternatives[alternative][0]
                value = settingField[iSettings]
                oldSettings.setSetting(key, value)
                iSettings += 1
                key = self.alternatives[alternative][1]
                value = settingField[iSettings]
                oldSettings.setSetting(key, value)
                iSettings += 1
        return oldSettings

    def loadLastJsonLegend(self):
        with open(self.jsonName, 'r') as f:
            self.legend = json.load(f)
            if "nameSample" in self.legend.keys():
                del self.legend["nameSample"]

    def storeLastJsonLegend(self):
        with open(self.jsonName, 'w') as f:
            json.dump(self.legend, f, indent=2)



