from .constants import *
from .mediator import SR510, Metex
import json


class Lockin:
    def __init__(self, name=None, port=None):
        """
        @param name: nazov lockinu, musi byt definovany v lockins_data.json
        @param port: port na ktorom je kabel z lockinu pripojeny
        """
        self.name = name

        self.gain_values = []
        self.pre_time_const = []
        self.post_time_const = []
        self.mediator_name = None

        self.cur_gain_index = None
        self.should_auto_switch_gain = True
        self.mediator = None
        self.connected = False

        if name is not None:
            self.load_lockin_information()
        if port is not None:
            self.connect(port)

    def load_lockin_information(self):
        """
        Nacita informacie o lockine z json suboru
        @param nazov lockinu:
        @return:
        """
        with open('models/lockin/lockins_data.json') as file:
                lockin_data = json.load(file)[self.name]

        self.gain_values = lockin_data[GAIN]
        self.pre_time_const = lockin_data[PRE_TIME_CONST]
        self.post_time_const = lockin_data[POST_TIME_CONST]
        self.mediator_name = lockin_data['mediator_name']

    def connect(self, port):
        """
        Pripoji sa sposob komunikacie s lockinom
        @param port: port na ktorom je kabel z lockinu pripojeny
        """
        if self.mediator_name == 'SR510':
            self.mediator = SR510(port)
        elif self.mediator_name == 'Metex':
            self.mediator = Metex(port)
        else:
            raise NotImplementedError

        self.connected = True

    def disconnect(self):
        """
        Odpoji lockin
        @return:
        """
        if self.mediator is not None:
            self.mediator.disconnect()
        self.mediator = None
        self.connected = False

    def current_gain_value(self):
        """
        Vrati hodnotu momentalne nastavenej senzitivty na zaklade lokalne ulozenej premennej self.cur_gain_index.
        Cize ak by pouzivatel manualne menil senzitivu na lockine sa nebude vraciat spravna hodnota.
        @return: float
        """
        return self.gain_values[self.cur_gain_index]

    def read_setting(self, setting):
        """
        Precita nastavenie napr. a spracuje ak je to potrebne.
        @param setting: jedno z nastaveni definovane v constants
        @return: hodnota, ktoru sme vyziadali
        """
        value = self.mediator.read_setting(setting)
        if setting == GAIN:
            return self.gain_values[value]
        elif setting == PRE_TIME_CONST:
            return self.pre_time_const[value]
        elif setting == POST_TIME_CONST:
            return self.post_time_const[value]
        return value

    def read_value(self):
        """
        Precita namerane napatie na lockine
        @return: momentalne napatie
        """
        return self.mediator.read_value()

    def lower_gain(self):
        """
        Znizi senzitivitu a zaznamena to v lokalne ulozenej premennej self.cur_gain_index zmenu
        @return:
        """
        self.cur_gain_index += 1
        if self.should_auto_switch_gain and self.mediator.is_setting_gain_possible():
            self.mediator.lower_gain()

    def higher_gain(self):
        """
        Zvysi senzitivitu a zaznamena to v lokalne ulozenej premennej self.cur_gain_index zmenu
        @return:
        """
        if self.cur_gain_index >= 12:
            self.cur_gain_index -= 1
            if self.should_auto_switch_gain and self.mediator.is_setting_gain_possible():
                self.mediator.higher_gain()

    def prepare(self):
        """
        priprava lockinu na zacatie merania.
        Lokalne ulozi senzitivtu, ktoru lokalne menime aby nebolo nutne zakazdym cakat na citanie z lockinu
        @return:
        """
        self.mediator.read_value()
        self.cur_gain_index = self.mediator.read_setting(GAIN)

    def can_auto_switch(self):
        """
        Zisti ci je mozne automaticky menit senzitivitu
        @return: bool
        """
        return self.mediator.is_setting_gain_possible()
