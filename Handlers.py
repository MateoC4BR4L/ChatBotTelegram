from abc import ABC, abstractmethod
from APIS import WeatherAPI, Lat_LonAPI


class Handlers(ABC):
    @staticmethod
    @abstractmethod
    def handler(message):
        pass


class WeatherHandler(Handlers):
    Keywords = ["/clima", "clima"]

    @staticmethod
    def handler(message):
        if message in WeatherHandler.Keywords:

            return
        else:
            return "nao nao amigao"
