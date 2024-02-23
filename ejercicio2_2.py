import time
import functools
import pandas as pd

_PRODUCT_DF = pd.DataFrame(
    {"product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"], "quantity": [3, 10, 0, 5]}
)


class RetryLimitReachedError(BaseException):
    def __init__(self, message="Límite de consultas alcanzado."):
        self.message = message

    def __str__(self):
        return repr(self.message)


def max_retries(max_attempts):
    def decorator(func):
        attempts = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal attempts
            if attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except:
                    time.sleep(1)
                finally:
                    attempts += 1
            else:
                raise RetryLimitReachedError()

        return wrapper

    return decorator


@max_retries(3)
def is_product_available_advanced(product_name, quantity):
    product = _PRODUCT_DF.loc[(_PRODUCT_DF["product_name"] == product_name) & (_PRODUCT_DF["quantity"] >= quantity)]

    if not product.empty:
        return True
    else:
        return False
