import datetime
from config.logger import write_log

def log_action(func):
    # simple logger decorator
    def wrapper(*args, **kwargs):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        write_log(f"[LOG {time}] - Running: {func.__name__}")
        result = func(*args, **kwargs)
        write_log(f"[LOG {time}] - Finished: {func.__name__}")
        return result
    return wrapper
