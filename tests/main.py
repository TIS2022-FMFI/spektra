from unittest import main

from tests.logger.log_tests import LogTests
from tests.logger.log_level_tests import LogLevelTests
from tests.logger.logger_tests import LoggerTests
from tests.logger.log_buffer_tests import LogBufferTests

if __name__ == '__main__':
    main(verbosity=2, exit=False)
