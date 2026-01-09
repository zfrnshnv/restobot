from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_button():
    menu = KeyboardButton(text='🍽 Restoran menyusi')
    connect = KeyboardButton(text="📞 Biz bilan bog'lanish")
    lang = KeyboardButton(text="Tilni o'zgartirish")
    reply = ReplyKeyboardBuilder()
    reply.add(menu, connect, lang)
    reply.adjust(1)
    return reply.as_markup(resize_keyboard=True)