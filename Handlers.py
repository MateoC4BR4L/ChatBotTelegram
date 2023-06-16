from abc import ABC, abstractmethod

from APIS import WeatherAPI, Lat_LonAPI


# Clase abstracta Handler
class Handlers(ABC):
    @staticmethod
    @abstractmethod
    def handler():
        pass


# Clase que maneja el comando "clima"
class WeatherHandler(Handlers):
    # Variable para comprobar que se ingrese la ciudad luego de ingresar el comando clima
    get_weather = False
    @staticmethod
    def handler():
        # Sumamos una interaccion mas al contador
        CounterHandler.counter += 1
        # Habilitamos el ingreso de una ciudad
        WeatherHandler.get_weather = True

        return "¡Perfecto! Ahora ingresa el nombre de la ciudad para ver su clima."

    @staticmethod
    def get_weather_handler(city):
        # Try-Except para manejar el error de una posible ciudad mal ingresada
        try:
            # Se obtiene el clima de la ciudad
            weather = WeatherAPI.get_weather(city)
            # Al completarse la solicitud de el clima de la ciudad, la variable vuelve a su valor inicial
            WeatherHandler.get_weather = False
            # Se suma una interacción más al contador
            CounterHandler.counter += 1

            return weather
        except Exception as e:
            # Caso de que salte un error por un ingreso incorrecto de la ciudad
            print(f"Se produjo un error: {str(e)}")

            return str(e)


# Clase con el contador de interacciones
class CounterHandler(Handlers):
    counter = 0

    @staticmethod
    def handler():
        # Sumamos una interaccion mas al contador
        CounterHandler.counter += 1
        return str(CounterHandler.counter)
