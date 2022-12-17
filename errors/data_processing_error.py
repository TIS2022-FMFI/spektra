from errors.error import Error
from errors.constants import DATA_PROCESSING_ERROR_CODE, ERROR_MESSAGES


class data_processing_error(Error):
    error_code = DATA_PROCESSING_ERROR_CODE

    def __init__(self, message=None):
        self.message = message
        if self.message is None:
            self.message = ERROR_MESSAGES[data_processing_error.error_code]
        super().__init__(self.message, data_processing_error.error_code)