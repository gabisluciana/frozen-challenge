import requests


class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    UNITS = "metric"
    HOT_MIN_TEMP = 28

    @classmethod
    def is_hot_in_pehuajo(cls):
        params = {"lat": cls.LAT, "lon": cls.LON, "appid": cls.API_KEY, "units": cls.UNITS}
        try:
            response = requests.get(cls.BASE_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                temp = data["main"]["temp"]

                return temp > cls.HOT_MIN_TEMP

            return False

        except:
            return False
