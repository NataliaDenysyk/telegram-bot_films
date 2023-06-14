import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from settings import TgSettings
from tg_API import common, selection_movie


async def main():
    """
    Запускает бота
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    dp = Dispatcher(storage=MemoryStorage())

    Token = TgSettings()
    token_bot = Token.token
    bot = Bot(token=token_bot)

    dp.include_router(common.router)
    dp.include_router(selection_movie.router)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


with open('readme.md', 'w', encoding='utf-8') as file:
    result = '\ndef main' + main.__doc__
    file.write(result)


if __name__ == '__main__':
    asyncio.run(main())























# import os
# from settings import TgSettings
#
# import asyncio
# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters.command import Command
# from aiogram.filters import Text



# from dotenv import load_dotenv
# import os
# import asyncio
# from aiogram import Bot, Dispatcher
#
#
# load_dotenv()
#
#
# async def main():
#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
#     )
#     Token = TgSettings()
#     token_bot = Token.token
#
#     logging.basicConfig(level=logging.INFO)
#     bot = Bot(token=token_bot)
#
#     dp = Dispatcher()
#
#     # Запускаем бота и пропускаем все накопленные входящие
#     # Да, этот метод можно вызвать даже если у вас поллинг
#     await bot.delete_webhook(drop_pending_updates=True)
#     await dp.start_polling(bot)
#
#
# import asyncio
# import logging
#
# from aiogram import Bot, Dispatcher
# from aiogram.fsm.storage.memory import MemoryStorage
#
# # файл config_reader.py можно взять из репозитория
# # пример — в первой главе
# from config_reader import config
# from handlers import common, ordering_food
#
#
# async def main():
#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
#     )
#
#     # Если не указать storage, то по умолчанию всё равно будет MemoryStorage
#     # Но явное лучше неявного =]
#     dp = Dispatcher(storage=MemoryStorage())
#     bot = Bot(config.bot_token.get_secret_value())
#
#     dp.include_router(common.router)
#     dp.include_router(ordering_food.router)
#     # сюда импортируйте ваш собственный роутер для напитков
#
#     await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
#
#
# if __name__ == '__main__':
#     asyncio.run(main())
#
#




#         def get_selections_of_movie
#             return _selections_of_films()
#
#
#
# import telebot
# from telebot import types
# from telebot import apihelper
# from dotenv import load_dotenv
# import os
#
#
# from site_API.core import site_api, url, headers, params
# from site_API.utils.message_handler import MessageMovie
#
# load_dotenv()
#
# bot = telebot.TeleBot('5991665549:AAGqlvskIRbMvAQ2KPM-axNgswCd96YPRlg')
#
# @bot.message_handler(commands=['start', 'hellow-world', 'Привет'])
# def send_welcome(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     items_1 = types.KeyboardButton('genre')
#     items_2 = types.KeyboardButton('year')
#     items_3 = types.KeyboardButton('random')
#     items_4 = types.KeyboardButton('history')
#     markup.add(items_1, items_2, items_3, items_4)
#
#     bot.reply_to(message, 'Привет, я бот, который поможет тебе выбрать интересный фильм.Выбери одну из команд.', reply_markup=markup)
#
#
#
# @bot.message_handler(func=lambda message: True)
# def menu(message):
#     if message.text == 'genre':
#         markup = types.InlineKeyboardMarkup(row_width=4)
#         items_1 = types.InlineKeyboardButton('Action', callback_data='Action')
#         items_2 = types.InlineKeyboardButton('Comedy', callback_data='Comedy')
#         items_3 = types.InlineKeyboardButton('Documentary', callback_data='Documentary')
#         items_4 = types.InlineKeyboardButton('Family', callback_data='Family')
#         items_5 = types.InlineKeyboardButton('Horror', callback_data='Horror')
#         items_6 = types.InlineKeyboardButton('Thriller',callback_data='Thriller')
#         items_7 = types.InlineKeyboardButton('Animation', callback_data='Animation')
#         items_8 = types.InlineKeyboardButton('Crime', callback_data='Crime')
#         items_9 = types.InlineKeyboardButton('Fantasy', callback_data='Fantasy')
#         items_10 = types.InlineKeyboardButton('Adventure', callback_data='Adventure')
#         items_11 = types.InlineKeyboardButton('Sport', callback_data='Sport')
#         items_12 = types.InlineKeyboardButton('Mystery', callback_data='Mystery')
#         items_13 = types.InlineKeyboardButton('History', callback_data='History')
#         items_14 = types.InlineKeyboardButton('Animation', callback_data='Animation')
#         items_15 = types.InlineKeyboardButton('War', callback_data='War')
#         items_16 = types.InlineKeyboardButton('Western', callback_data='Western')
#         markup.add(items_1, items_2, items_3, items_4, items_5, items_6,
#                    items_7, items_8, items_9, items_10, items_11, items_12,
#                    items_13, items_14, items_15, items_16)
#
#         bot.send_message(message.chat.id, 'Выбери жанр', reply_markup=markup)
#
#     elif message.text == 'year':
#         year_hendler = bot.send_message(message.chat.id, 'Выбери с какого года по какой искать(например, 1970-2020)')
#     # elif message.text == 'random':
#     #     result = SearchRecordMovies()
#     #     res = result[:10]
#     #             bot.send_message(message.chat.id, element.message)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def genre(call):
#     try:
#         if call.message == 'Action':
#             db_write = crud.create()
#             db_read = crud.retrieve()
#
#             movie_list = site_api.get_params()
#
#             response = movie_list('GET', url, headers, params, genre='Action',
#                                   start_year=1998, end_year=2020)
#
#             response = response.json()
#
#             list_movie = MessageMovie.my_message(response)
#
#             data = [{'id_user': call.from_user.id, genre: 'Action', 'message': list_movie}]
#
#             db_write(db, History, data)
#
#             bot.send_message(call.message.chat.id, *list_movie)
#             bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Приятного просмотра')
#
#         if call.message == 'comedy':
#             db_write = crud.create()
#             db_read = crud.retrieve()
#
#             movie_list = site_api.get_params()
#
#             response = movie_list('GET', url, headers, params, genre='comedy',
#                                   start_year=1998, end_year=2020)
#
#             response = response.json()
#
#             list_movie = MessageMovie.my_message(response)
#
#             data = [{'id': call.from_user.id, 'genre': 'comedy', 'message': list_movie}]
#
#             db_write(db, History, data)
#
#             bot.send_message(call.message.chat.id, *list_movie)
#             bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Приятного просмотра')
#     except Exception as e:
#         print(e)
#
#
# @bot.message_handler(commands=['help'])
# def help(message):
#     bot.send_message(message.chat.id, 'genre - выбор фильма по жанру;\n'
#                                       'year - выбор фильма по году;\n'
#                                       'random - случайная подборка фильмов;\n'
#                                       'history - история поиска')
#
#
#
#
#
#
#
# bot.polling(none_stop=True)
