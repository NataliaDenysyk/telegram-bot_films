from random import choice
import re

from aiogram import Router, F
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from site_API.read_history import get_history_movie
from site_API.movie import Movie
from tg_API.utils.creating_row import make_row_keyboard


router = Router()

choice_search_method = ['genre', 'year', 'random', 'history']
choice_genre = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime',
                'Documentary', 'Drama', 'Family', 'Fantasy',
                'History', 'Horror', 'Mystery', 'Sci-Fi', 'Sport', 'Thriller',
                'War', 'Western']


class OrderChoiceMovie(StatesGroup):
    ''''
    Класс, наследующийся от класса StatesGroup, для описания состояний пользователя
    '''
    choosing_search_method = State()
    choosing_genre = State()
    choosing_year = State()
    choosing_random = State()
    choosing_history = State()


@router.message(Command('hellow_world'))
async def cmd_button(message: Message, state: FSMContext):
    await message.answer(
        text="Выбери по какому признаку будем искать фильм",
        reply_markup=make_row_keyboard(choice_search_method)
    )
    await state.set_state(OrderChoiceMovie.choosing_search_method)


@router.message(Text('Привет'))
async def cmd_button(message: Message, state: FSMContext):
    await message.answer(
        text="Выбери по какому признаку будем искать фильм",
        reply_markup=make_row_keyboard(choice_search_method)
    )
    await state.set_state(OrderChoiceMovie.choosing_search_method)


@router.message(Text("genre"))
async def cmd_genre(message: Message, state: FSMContext):
    await message.answer(
        text="Отлично, теперь выбери жанр",
        reply_markup=make_row_keyboard(choice_genre)
    )
    await state.set_state(OrderChoiceMovie.choosing_genre)


@router.message(OrderChoiceMovie.choosing_genre, F.text.in_(choice_genre))
async def method_chosen_genre(message: Message, state: FSMContext):
    await state.update_data(chosen_movie=message.text.lower())
    user_data = await state.get_data()
    userid = message.from_user.id
    usergenre = user_data['chosen_movie']
    response = Movie(user_id=userid, genre=usergenre, start_year=2005, end_year=2020)
    result = response.selections_of_films()
    await message.answer('\n'.join(result))
    await message.answer('Приятного просмотра!')
    await message.answer(
        text="Выбери по какому признаку будем искать фильм",
        reply_markup=make_row_keyboard(choice_search_method)
    )
    await state.set_state(OrderChoiceMovie.choosing_search_method)


@router.message(OrderChoiceMovie.choosing_genre)
async def genre_incorrectly(message: Message):
    await message.answer(
        text="Я не знаю такого жанра.\n\n"
             "Пожалуйста, выбери один из вариантов из списка ниже:",
        reply_markup=make_row_keyboard(choice_genre)
    )


@router.message(Text("year"))
async def cmd_year(message: Message, state: FSMContext):
    await message.answer(
        text="Отлично, теперь напиши с какого по какой год будем искать\n\nНапример: 1970/2020"
    )
    await state.set_state(OrderChoiceMovie.choosing_year)


@router.message(OrderChoiceMovie.choosing_year)
async def method_chosen_year(message: Message, state: FSMContext):
    if re.fullmatch(r'\d{4}\D\d{4}', message.text):
        await state.update_data(chosen_year=message.text.lower().split('/'))
        user_data = await state.get_data()
        userid = message.from_user.id
        userstart_year = user_data['chosen_year'][0]
        userend_year = user_data['chosen_year'][1]
        usergenre = choice(choice_genre)
        response = Movie(user_id=userid, genre=usergenre, start_year=userstart_year, end_year=userend_year)
        result = response.selections_of_films()
        await message.answer('\n'.join(result))
        await message.answer(text='Приятного просмотра!')
        await message.answer(
            text="Выбери по какому признаку будем искать фильм",
            reply_markup=make_row_keyboard(choice_search_method)
        )
        await state.set_state(OrderChoiceMovie.choosing_search_method)
    else:
        await message.answer(
            text="Некорректно введен год поиска.\n\n"
                 "Пожалуйста, введите год как \n1970/2020\nи в этом диапазоне"
        )
        await state.set_state(OrderChoiceMovie.choosing_year)


@router.message(Text("random"))
async def cmd_random(message: Message, state: FSMContext):
    userid = message.from_user.id
    usergenre = choice(choice_genre)
    response = Movie(user_id=userid, genre=usergenre, start_year=1970, end_year=2020)
    result = response.selections_of_films()
    await message.answer('\n'.join(result))
    await message.answer(text='Приятного просмотра!')
    await message.answer(
        text="Выбери по какому признаку будем искать фильм",
        reply_markup=make_row_keyboard(choice_search_method)
    )
    await state.set_state(OrderChoiceMovie.choosing_search_method)


@router.message(Text("history"))
async def cmd_history(message: Message, state: FSMContext):
    userid = message.from_user.id
    # usergenre = choice(choice_genre)
    response = get_history_movie(user_id=userid)
    await message.answer(text='Ваша история поиска')
    await message.answer('\n\n'.join(response))
    await message.answer(
        text="Выбери по какому признаку будем искать фильм",
        reply_markup=make_row_keyboard(choice_search_method)
    )
    await state.set_state(OrderChoiceMovie.choosing_search_method)


@router.message(OrderChoiceMovie.choosing_search_method)
async def method_chosen_incorrectly(message: Message):
    await message.answer(
        text="У меня нет такого способа .\n\n"
             "Пожалуйста, выбери одно из названий из списка ниже:",
        reply_markup=make_row_keyboard(choice_search_method)
    )