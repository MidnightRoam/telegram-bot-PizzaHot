from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton("/Режим_работы")
b2 = KeyboardButton("/Расположение")
b3 = KeyboardButton("/Меню")
# b4 = KeyboardButton("Поделиться номером", request_contact=True)
# b5 = KeyboardButton("Отправить свое местоположение", request_location=True)


btn_client = ReplyKeyboardMarkup(resize_keyboard=True)

btn_client.add(b1).add(b2).insert(b3)#.row(b4, b5)
