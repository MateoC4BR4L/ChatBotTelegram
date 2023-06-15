import Handlers
from telebot.async_telebot import AsyncTeleBot


class WeatherHandler(Handlers):
    async def Handler(self, bot: AsyncTeleBot, message, next_handler: Handlers):
        await bot.reply_to(message, f"{message.from_user.first_name} {message.from_user.last_name} ")