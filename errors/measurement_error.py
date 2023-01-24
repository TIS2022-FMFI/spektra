from errors.error import Error
from errors.constants import MEASUREMENT_ERROR_CODE, ERROR_MESSAGES


class MeasurementError(Error):
    error_code = MEASUREMENT_ERROR_CODE

    def __init__(self, message=None):
        self.message = message
        if self.message is None:
            self.message = ERROR_MESSAGES[MeasurementError.error_code]
        super().__init__(self.message, MeasurementError.error_code)
