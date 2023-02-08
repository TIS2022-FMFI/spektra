import qtawesome as qta

from view.constants import NIGHT_MODE


class Icons:
    start_measurement = qta.icon('fa5s.play', color='green')
    start_measurement_disabled = qta.icon('fa5s.play', color='grey')
    start_measurement_night = qta.icon('fa5s.play', color='yellow')
    stop_measurement = qta.icon('fa5s.stop', color='red')
    stop_measurement_disabled = qta.icon('fa5s.stop', color='grey')
    stop_measurement_night = stop_measurement
    save_measurement = qta.icon('fa5s.save', color='blue')
    save_measurement_disabled = qta.icon('fa5s.save', color='grey')
    save_measurement_night = qta.icon('fa5s.save', color='yellow')
    left_arrow = qta.icon('fa5s.arrow-left', color='blue')
    left_arrow_disabled = qta.icon('fa5s.arrow-left', color='grey')
    left_arrow_night = qta.icon('fa5s.arrow-left')
    right_arrow = qta.icon('fa5s.arrow-right', color='blue')
    right_arrow_disabled = qta.icon('fa5s.arrow-right', color='grey')
    right_arrow_night = qta.icon('fa5s.arrow-right')
    ui_night = qta.icon('fa5s.sun', color='yellow')
    ui = qta.icon('fa5s.moon', color='blue')
    ui_disabled = qta.icon('fa5s.moon', color='grey')
    save = qta.icon('fa5s.save', color='green')
    save_disabled = qta.icon('fa5s.save', color='grey')
    save_night = qta.icon('fa5s.save', color='yellow')
    open = qta.icon('fa5s.folder-open', color='green')
    open_disabled = qta.icon('fa5s.folder-open', color='grey')
    open_night = qta.icon('fa5s.folder-open', color='yellow')
    settings = qta.icon('fa5s.cog', color='green')
    settings_disabled = qta.icon('fa5s.cog', color='grey')
    settings_night = qta.icon('fa5s.cog', color='yellow')
    exit = qta.icon('fa5s.times', color='red')
    exit_disabled = qta.icon('fa5s.times', color='grey')
    exit_night = qta.icon('fa5s.times', color='yellow')
    about = qta.icon('fa5s.info-circle', color='green')
    about_disabled = qta.icon('fa5s.info-circle', color='grey')
    about_night = qta.icon('fa5s.info-circle', color='yellow')
    help = qta.icon('fa5s.question-circle', color='green')
    help_disabled = qta.icon('fa5s.question-circle', color='grey')
    help_night = qta.icon('fa5s.question-circle', color='yellow')
    voltmeter_disconnected = qta.icon('fa5s.bolt', color='grey')
    voltmeter_connected = qta.icon('fa5s.bolt', color='yellow')

    def get(self, icon_name, mode, enabled=True):
        """
            Returns the icon for the given mode and in a given state.
            @param icon_name: The name of the icon to return.
            @param mode: The mode of the application.
            @param enabled: The state of the icon.
        """

        if not enabled:
            return getattr(self, f'{icon_name}_disabled')
        if mode == NIGHT_MODE:
            return getattr(self, f'{icon_name}_night')
        return getattr(self, icon_name)
