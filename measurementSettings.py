import json
from datetime import datetime
from datetime import date
import os


class settings:
    mandatory = ["nameSample", "noteToTech", "thickness", "reference", "temperature", "nameOfDispersingElement",
                 "typeOfDispersingElement", "inputCreviceWidth", "inputCreviceHeight", "outputCreviceWidth",
                 "outputCreviceHeight", "opticalFilter", "typeOfDetector", "additionalInfoDetector",
                 "typeOfLight", "nameOfLight", "stepOfMotor", "numberOfMitigations", "correction",
                 "lockIn", "lockInReference", "lockInFilter", "phaseShift", "timeConstante",
                  "typeSensitivity"]
    alternatives = [("startAngle", "endAngle"),
                    ("startAngstrom", "endAngstrom")]

    def __init__(self):
        self.legend = dict()
        self.setSetting("typeOfDispersingElement", "mriežka")
        self.setSetting("typeSensitivity", "AUTO")

        script_dir = os.path.dirname(__file__)
        rel_path = "lastSettings.txt"
        self.jsonName = os.path.join(script_dir, rel_path)



    def setSetting(self, key, param):
        all = self.mandatory + [key for alter in self.alternatives
                                for key in alter]
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
        if "startAngle" in self.legend.keys():
            type = "°"
            start = self.legend["startAngle"]
            stop = self.legend["endAngle"]
        else:
            type = "A°"
            start = self.legend["startAngstrom"]
            stop = self.legend["endAngstrom"]

        today = date.today()
        now = datetime.now()
        dateCurrent = today.strftime('%d-%m-%Y')
        timeCurrent = now.strftime("%H:%M:%S")

        return "VZORKA:\n" + \
            "názov vzorky: " + self.legend["nameSample"] + "\n" + \
            "poznámka k technológií: " +  self.legend["noteToTech"] + "\n" + \
            "hrúbka: " + self.legend["thickness"] + "\n" + \
            "referencie: " + self.legend["reference"] + "\n" +  \
            "teplota: " + self.legend["temperature"] + "\n" + \
            "DISPERZNÝ ELEMENT:\n" + \
            self.legend["typeOfDispersingElement"] + " " +  \
                     self.legend["nameOfDispersingElement"] + "\n" +   \
            "MONOCHROMÁTOR:\n" + \
            "vstupná štrbina (hrúbka, výška): " + \
                self.legend["inputCreviceWidth"] + " " + \
                self.legend["inputCreviceHeight"] + "\n" + \
            "výstupná štrbina (hrúbka, výška): " +    \
                self.legend["outputCreviceWidth"] + " " + \
                self.legend["outputCreviceHeight"] + "\n" +  \
            "optický filter: " + self.legend["opticalFilter"] + "\n" + \
            "DETEKTOR:\n" + \
            self.legend["typeOfDetector"] + " " +   \
                self.legend["additionalInfoDetector"] + "\n" + \
            "BÚDIACE SVETLO:\n" +   \
            self.legend["typeOfLight"] + " " + \
                self.legend["nameOfLight"] + "\n" + \
            "MERANIE:\n" + \
            dateCurrent + ", " + timeCurrent + "\n" + \
            self.legend["nameSample"] + "\n" + \
            "počiatočná vlnová dĺžka ["  \
                + type + "]: " + start + "\n" + \
            "koncová vlnová dĺžka [" \
                + type + "]: " + stop + "\n" + \
            "krok motora [v impulzoch]: " + \
                self.legend["stepOfMotor"] + "\n" + \
            "počet mitigácií: " + \
                self.legend["numberOfMitigations"] + "\n" + \
            "korekcia [A°]: " + \
                self.legend["correction"] + "\n" + \
            "MILIVOLTMENTER:\n" + \
            self.legend["lockIn"] + "\n" + \
            "citlivosť: " + self.legend["typeSensitivity"] + "\n" + \
            "referencia [Hz]: " + self.legend["lockInReference"] + "\n" + \
            "filters: " + self.legend["lockInFilter"] + "\n" + \
            "fázový posun: " + self.legend["phaseShift"] + "\n" + \
            "časová konštanta: " + self.legend["timeConstante"]


    def loadLastLegend(self):
        with open(self.jsonName, 'r') as f:
            self.legend = json.load(f)
            if "nameSample" in self.legend.keys():
                del self.legend["nameSample"]   #vymazeme pre vacsiu intuitivnost
            return True
        return False


    def storeLastLegend(self):
        with open(self.jsonName, 'w') as f:
            json.dump(self.legend, f, indent=2)
            return True
        return False



