# frozen-challenge

## Ejercicio 1
Se implementó un método de clase para la clase GeoAPI. Este método usa la API de OpenWeatherMap para obtener la temperatura acutal en Pehuajó en grados Celsius (`UNITS = "metric"`) y compararlo contra una variable (`HOT_MIN_TEMP`) que permite definir la temperatura mínima para considerar que hace calor. Devuelve `True` en caso que la temperatura actual sea superior al umbral establecido, `False` en cualquier otro caso, incluyendo errores.


## Ejercicio 2.1
En esta función se utilizó el método `loc` del DataFrame para encontar la fila que tenga el mismo `product_name` y la cantidad `quantity` sea igual o mayor a la solicitada por parámetro. Si la fila devuelta no está vacía se devuelve `True`. En caso contrario se retorna `False`


## Ejercicio 2.2
Se decidió utilizar un decorador para la función. Con este decorador se puede indicar la cantidad de veces que se puede invocar la función. Si se consulta más veces, se lanza un error de tipo `RetryLimitReachedError`
