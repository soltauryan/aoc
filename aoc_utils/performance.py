import time
from functools import wraps

def time_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        try:
            return func(*args, **kwargs)
        finally:
            duration = time.perf_counter() - start

            print(
                f"{func.__name__} "
                f"completed in {duration:.6f} seconds"
            )

    return wrapper