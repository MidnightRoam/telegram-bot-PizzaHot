from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token="5533324983:AAEGSH02jnbpdlLQiVtHMG5ihqnYVKmebG8")
dp = Dispatcher(bot, storage=storage)

