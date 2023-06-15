import Handlers
import telebot


class WeatherHandler(Handlers):
    @staticmethod
    async def Handler(self, bot: telebot, message, next_handler: Handlers):
        await bot.reply_to(message, f"{message.from_user.first_name} {message.from_user.last_name} ")