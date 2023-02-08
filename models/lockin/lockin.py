from .constants import *
from .mediator import SR510, Metex
import json


class Lockin:
    def __init__(self, name=None, port=None):
        """
        initialization of Lockin model
        @param name: name of lockin (defined in lockins_data.json)
        @param port: port, where is lockin connected
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
        Load lockin info from JSON file
        """
        with open('models/lockin/lockins_data.json') as file:
            lockin_data = json.load(file)[self.name]

        self.gain_values = lockin_data[GAIN]
        self.pre_time_const = lockin_data[PRE_TIME_CONST]
        self.post_time_const = lockin_data[POST_TIME_CONST]
        self.mediator_name = lockin_data['mediator_name']

    def connect(self, port):
        """
        Connect to Lockin at concrete port
        @param port: port where is lockin connected
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
        Disconnect lockin
        """
        if self.mediator is not None:
            self.mediator.disconnect()
        self.mediator = None
        self.connected = False

    def current_gain_value(self):
        """
        Return value of sensitivity based on locally saved variable in self.cur_gain_index.
        If user change value directly at lockin device, won't get correct value
        @return: float
        """
        return self.gain_values[self.cur_gain_index]

    def read_setting(self, setting):
        """
        Read settings (and processes it, if needed)
        @param setting: setting defined in constants
        @return: required value
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
        Read measured value from lockin
        @return: current measured value
        """
        return self.mediator.read_value()

    def lower_gain(self):
        """
        Lower sensitivity (change in local variable self.cur_gain_index)
        """
        self.cur_gain_index += 1
        if self.should_auto_switch_gain and self.mediator.is_setting_gain_possible():
            return self.mediator.set_gain(self.cur_gain_index)
        return False

    def higher_gain(self):
        """
        Increase sensitivity (change in local variable self.cur_gain_index)
        """
        if self.cur_gain_index > self.mediator.lowest_auto_settable_gain:
            self.cur_gain_index -= 1
            if self.should_auto_switch_gain and self.mediator.is_setting_gain_possible():
                return self.mediator.set_gain(self.cur_gain_index)
        return False

    def prepare(self):
        """
        Prepare locking for measurement start
        Save sensitivity locally, sensitivity is then changed locally, due to delay reasons
        """
        self.mediator.read_value()
        self.cur_gain_index = self.mediator.read_setting(GAIN)

    def can_auto_switch(self):
        """
        Check, if sensitivity can be changed automatically
        @return: if yes return True else False
        """
        return self.mediator.is_setting_gain_possible()

    def set_min_auto_sensitivity(self, value):
        self.mediator.lowest_auto_settable_gain = value
