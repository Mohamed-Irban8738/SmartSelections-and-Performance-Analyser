from functools import wraps
from utils.exceptions import BackOperation
from utils.ui import UI
def back_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BackOperation:
            UI.info("Returning to previous menu...")
            return
    return wrapper