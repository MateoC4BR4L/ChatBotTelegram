import telebot
from Handlers import *

# Obtengo el token del BOT contenido en el archivo (por seguridad)
with open("Token.txt", "r") as token:
    token = token.read()
# Creación del bot
bot = telebot.TeleBot(token)


# Comienzo del programa
# Manejar los mensajes iniciales
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    # Si el programa no espera una ciudad para obtener el clima
    if not WeatherHandler.get_weather:
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
    else:
        # Se suma una interacción más al contador
        CounterHandler.counter += 1
        # En caso de que espere una ciudad para obtener el clima
        bot.send_message(message.chat.id, "¡Este comando no se acepta como ciudad!")


# Manejar el comando "clima"
@bot.message_handler(commands=["clima"])
def handlers(message):
    # Si el programa no espera una ciudad para obtener el clima
    if not WeatherHandler.get_weather:
        bot.reply_to(message, WeatherHandler.handler())
    else:
        # Se suma una interacción más al contador
        CounterHandler.counter += 1
        # En caso de que espere una ciudad para obtener el clima
        bot.send_message(message.chat.id, "¡Este comando no se acepta como ciudad!")


# Manejar el comando "contador"
@bot.message_handler(commands=["contador"])
def handlers(message):
    # Si el programa no espera una ciudad para obtener el clima
    if not WeatherHandler.get_weather:
        bot.reply_to(message, CounterHandler.handler())
    else:
        # Se suma una interacción más al contador
        CounterHandler.counter += 1
        # En caso de que espere una ciudad para obtener el clima
        bot.send_message(message.chat.id, "¡Este comando no se acepta como ciudad!")


# Manejar en caso de que no se ingrese un comando y si una ciudad
@bot.message_handler(content_types=["text"])
def handlers(message):
    bot.send_message(message.chat.id, WeatherHandler.get_weather_handler(message.text))


def Main():
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


if __name__ == '__main__':
    Main()
