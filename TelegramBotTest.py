import telebot
from Handlers import *

# Obtengo el token del BOT contenido en el archivo (por seguridad)

with open("Token.txt", "r") as token:
    token = token.read()
# Creación del bot
bot = telebot.TeleBot(token)


# Comienzo del programa
# Manejar los mensajes iniciales
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 """\
    Hola ¿Cómo estás?
    ¡Soy un bot dispuesto a ayudarte en lo que me sea posible!
    Te explico mis funcionalidades:
    1- Puedo indicarte el clima de una ciudad en específico.
    2- Puedo decirte la cantidad de nuestras interacciones.\
    """)


# Manejar todos los otros tipos de mensajes
@bot.message_handler(func=lambda message: True)
def handlers(message):
    bot.reply_to(message, WeatherHandler.handler(message))


bot.infinity_polling()
