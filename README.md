# ChatBotTelegram

<h3>- Introducción: </h3>

- Este es un chatbot de Telegram creado en Python, utilizando la librería pyTelegramBotAPI.

<h3>- Funcionalidades: </h3>

- Este chatbot es capaz de indicarte el clima de la ciudad que desees.

- También puede contarte el número de interacciones que has tenido con este mismo.

<h3>- Clases utilizadas: </h3>

- APIS: Este archivo .py contiene las dos API utilizadas para obtener el clima de una ciudad:

    - Lat_LonAPI
    - WeatherAPI

- Handlers.py: Este archivo contiene 3 clases encargadas de las respuestas al chatbot.

    - Handlers
    - WeatherHandler
    - CounterHandler

- TelegramBotTest: Este archivo contiene la creación y ejecución del bot, junto a la clase main.

    - Main

<h3>- Comandos: </h3>

- /start: Muestra una introducción del bot.
- /help: Muestra una introducción del bot.
- /clima: Si desea ver el clima de una ciudad (posterior de haber ingreasdo el comando se deberá ingresar una ciudad).
- /contador: Mostrar la cantidad de interacciones entre el usuario y el bot.