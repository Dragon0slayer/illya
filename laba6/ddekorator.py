import time
from functools import wraps

def throttle(seconds: float):
    def decorator(func):
        last_called = [0]

        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            if current_time - last_called[0] >= seconds:
                last_called[0] = current_time
                return func(*args, **kwargs)
            else:
                print(f" Функцію '{func.__name__}' можна викликати лише раз на {seconds} секунд!")
        return wrapper
    return decorator
