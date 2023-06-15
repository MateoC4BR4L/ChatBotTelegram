import telebot

with open("Token/Token.txt", "r") as token:
    token = token.read()

bot = telebot.TeleBot(token)


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


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, f"{message.from_user.first_name}  {message.from_user.id}")


bot.infinity_polling()
