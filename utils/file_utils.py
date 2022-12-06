import inspect
import os
from datetime import datetime, timedelta


def get_current_line():
    return inspect.currentframe().f_back.f_lineno

def get_current_filename():
    return os.path.basename(__file__)


def get_current_dir():
    return os.path.dirname(__file__)


def remove_files_older_than(path, file_extension, days):
    if (not os.path.exists(path)) or (not os.path.isdir(path)):
        raise ValueError(f'Path {path} does not exist or is not a directory')
    now = datetime.now()
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path) and os.stat(file_path).st_mtime < (now - timedelta(days=days)).timestamp():
            if file.endswith(file_extension):
                os.remove(file_path)


def generate_log_file_name():
    return f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'
