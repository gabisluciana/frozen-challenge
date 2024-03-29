import pandas as pd

_PRODUCT_DF = pd.DataFrame(
    {"product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"], "quantity": [3, 10, 0, 5]}
)


def is_product_available(product_name, quantity):
    product = _PRODUCT_DF.loc[(_PRODUCT_DF["product_name"] == product_name) & (_PRODUCT_DF["quantity"] >= quantity)]

    if not product.empty:
        return True
    else:
        return False
