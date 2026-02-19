from functools import wraps
from common.schedule.scanner.task_scanner import TaskScanner

def task(func:callable):
    full_path = f"{func.__module__}.{func.__qualname__}"
    TaskScanner.register(func.__name__, full_path)
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper._is_task = True
    wrapper._task_path = full_path
    return wrapper