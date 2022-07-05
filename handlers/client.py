from aiogram import types, Dispatcher
from create_bot import dp, bot
from buttons.client_btn import btn_client


async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Приятного аппетита", reply_markup=btn_client)
        await message.delete()
    except:
        await message.reply("Общение с ботом через личные сообщения, напишите ему: \nhttps://t_me/Pizza_HotBot")


async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Вс-Чт с 9:00 до 20:00\nПт-Сб с 10:00 до 23:00")


async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, "ул. Пушкинская, 12")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=["start", "help"])
    dp.register_message_handler(pizza_open_command, commands=["Режим_работы"])
    dp.register_message_handler(pizza_place_command, commands=["Расположение"])
