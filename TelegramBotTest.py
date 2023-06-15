from telebot.async_telebot import AsyncTeleBot

api_token = "6149921628:AAFoeMV8BXJ_H6LzIgjujF_rIKIg60Dt1_s"
bot = AsyncTeleBot(api_token)


@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    await bot.reply_to(message, """\
        Hola ¿Cómo estás?
        ¡Soy un bot dispuesto a ayudarte en lo que me sea posible!
        Te explico mis funcionalidades:
        1- Puedo indicarte el clima de una ciudad en específico.
        2- Puedo decirte la cantidad de nuestras interacciones.\
        """)


@bot.message_handler(func=lambda message: True)
async def handle_message(message):
    await bot.reply_to(message, f"{message.from_user.first_name} {message.from_user.last_name} ")
