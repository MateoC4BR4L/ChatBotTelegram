from abc import ABC, abstractmethod
from telebot.async_telebot import AsyncTeleBot


class Handlers(ABC):
    @staticmethod
    async def Handler(self, bot: AsyncTeleBot, message, next_handler: ABC):
        pass
