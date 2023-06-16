import telebot
from Handlers import *

# Obtengo el token del BOT contenido en el archivo (por seguridad)
with open("Token.txt", "r") as token:
    token = token.read()
# Creación del bot
bot = telebot.TeleBot(token)
print(WeatherHandler.get_weather)
# En caso de que el bot esté esperando una ciudad como mensaje
if WeatherHandler.get_weather:
    @bot.message_handler(content_types=["text"])
    def handler(message):
        print("eeeeeeeeeeeeee")
        bot.reply_to(message, WeatherHandler.get_weather_handler(message.text))


# Comienzo del programa
# Manejar los mensajes iniciales
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    # Sumamos una interaccion mas al contador
    CounterHandler.counter += 1
    bot.reply_to(message,
                 """\
    Hola ¿Cómo estás?
    ¡Soy un bot dispuesto a ayudarte en lo que me sea posible!
    Te explico mis funcionalidades:
    1- Si deseas puedo indicarte el clima de una ciudad en específico, para ello ingresa el comando <b> /clima </b>.
    2- También puedo decirte la cantidad de nuestras interacciones, , para ello ingresa el comando <b> /contador </b>.\
    """, parse_mode="html")


# Manejar el comando "clima"
@bot.message_handler(commands=["clima"])
def handlers(message):
    bot.reply_to(message, WeatherHandler.handler())


# Manejar el comando "contador"
@bot.message_handler(commands=["contador"])
def handlers(message):
    bot.reply_to(message, CounterHandler.handler())


if __name__ == '__main__':
    # Se configura los comandos del bot
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Instrucciones generales del programa"),
        telebot.types.BotCommand("/help", "Instrucciones generales del programa"),
        telebot.types.BotCommand("/clima", "Obtener el clima de una ciudad"),
        telebot.types.BotCommand("/contador", "Obtener el número de interacciones con el bot")
    ])
    print("Iniciando bot...")
    bot.infinity_polling()
    print("Bot finalizado")
