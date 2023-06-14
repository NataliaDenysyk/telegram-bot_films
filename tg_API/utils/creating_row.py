from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import types

def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    """
    Создаёт реплай-клавиатуру с кнопками по 4 в ряд
    :param items: список текстов для кнопок
    :return: объект реплай-клавиатуры
    """
    builder = ReplyKeyboardBuilder()
    for item in items:
        builder.add(types.KeyboardButton(text=str(item)))
    builder.adjust(4)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


with open('readme.md', 'w', encoding='utf-8') as file:
    result = '\ndef make_row_keyboard' + make_row_keyboard.__doc__
    file.write(result)


if __name__ == "__main__":
    make_row_keyboard()