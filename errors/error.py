class Error(Exception):
    """Base class for other custom exceptions / errors."""
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code

    def __str__(self):
        return f"{self.error_code}: {self.message}"

    def __repr__(self):
        return f"{self.error_code}: {self.message}"

    def __eq__(self, other):
        return self.error_code == other.error_code

    def __ne__(self, other):
        return self.error_code != other.error_code

