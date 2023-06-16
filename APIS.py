# Liberías para procesar los datos obtenidos de la API
# Al igual que para procesar el formato JSON
from urllib.request import urlopen
import json


# Clase para obtener latitud y longitud
class Lat_LonAPI:
    # Obtengo el token de la API contenido en el archivo (por seguridad)
    with open("WeatherToken.txt", "r") as token:
        token = token.read()

    # Obtener latitud de la ciudad
    @staticmethod
    def get_lat(city):
        # Url de la API con su respectivo token
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={Lat_LonAPI.token}"
        # Obtenemos la información en formato de String
        response = urlopen(url)
        # Transformamos los datos a JSON
        data = json.loads(response.read())
        # Obtenemos la latitud
        lat = data[0]["lat"]

        return lat

    # Obtener longitud de la ciudad
    @staticmethod
    def get_lon(city):
        # Url de la API con su respectivo token
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={Lat_LonAPI.token}"
        # Obtenemos la información en formato de String
        response = urlopen(url)
        # Transformamos los datos a JSON
        data = json.loads(response.read())
        # Obtenemos la longitud
        lon = data[0]["lon"]

        return lon


# Clase para obtener el clima
class WeatherAPI:
    @staticmethod
    def get_weather(city):
        # Url de la API con su respectivo token, latitud y longitud
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={Lat_LonAPI.get_lat(city)}&lon={Lat_LonAPI.get_lon(city)}&appid={Lat_LonAPI.token}&lang=es"
        # Transformamos los datos a JSON
        response = urlopen(url)
        # Obtenemos los datos de clima de la ciudad
        data = json.loads(response.read())
        # Obtenemos la descripción del clima de dicha ciudad
        description = data["weather"][0]["description"]

        return description


print(WeatherAPI.get_weather("Tokyo"))
