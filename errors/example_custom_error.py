from errors.error import Error
from errors.constants import EXAMPLE_CUSTOM_ERROR_CODE, ERROR_MESSAGES


class ExampleCustomError(Error):
    error_code = EXAMPLE_CUSTOM_ERROR_CODE

    def __init__(self, message=None):
        # Call the base class constructor
        if message is None:
            message = ERROR_MESSAGES[ExampleCustomError.error_code]
        super().__init__(message, ExampleCustomError.error_code)
