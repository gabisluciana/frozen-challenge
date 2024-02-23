from ejercicio1 import GeoAPI
from ejercicio2_1 import is_product_available
from ejercicio2_2 import is_product_available_advanced, RetryLimitReachedError

def main():
    print("#"*5, "Ejercicio 1", "#"*5)
    is_hot = GeoAPI.is_hot_in_pehuajo()
    print(f"Hoy {"si" if is_hot else "no"} esta caluroso en Pehuajo" )

    products = ["Granizado", "Limon", "Menta", "Chocolate", "Dulce de Leche", "Vainilla"]
    quantities = [2, 5, 1, 5, 2, 1]

    print()
    print("#"*5, "Ejercicio 2.1", "#"*5)
    for product, quantity in zip(products,quantities):
        is_available = is_product_available(product, quantity)
        print(f"{"Hay" if is_available else "No hay"}", product, "en cantidad", quantity)

    print()
    print("#"*5, "Ejercicio 2.2", "#"*5)
    for product, quantity in zip(products,quantities):
        try:
            is_available = is_product_available_advanced(product, quantity)
            print(f"{"Hay" if is_available else "No hay"}", product, "en cantidad", quantity)
        except RetryLimitReachedError as e:
            print(f"ERROR: {e}")
            break
    


if __name__ == "__main__":
    main()
