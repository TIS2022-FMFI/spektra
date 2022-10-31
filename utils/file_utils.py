import os
from datetime import datetime, timedelta


def remove_files_older_than(path, days):
    if (not os.path.exists(path)) or (not os.path.isdir(path)):
        raise ValueError(f'Path {path} does not exist or is not a directory')
    now = datetime.now()
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path) and os.stat(file_path).st_mtime < (now - timedelta(days=days)).timestamp():
            os.remove(file_path)


def generate_log_file_name():
    return f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'
