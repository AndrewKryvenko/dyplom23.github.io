from aiogram.types import WebAppInfo
from aiogram import types

web_app = WebAppInfo(url='https://andrewkryvenko.github.io/dyplom23.github.io/')

keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text='Site', web_app=web_app)]
    ],
    resize_keyboard=True
)