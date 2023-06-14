from data_base.common.models import db, History
from data_base.core import crud

from site_API.core import site_api, url, headers, params
from site_API.utils.message_handler import MessageMovie

from dotenv import load_dotenv


load_dotenv()# проверить надо ли его подключать повторною он уже подключен в main


class Movie():
    """
    Устанавливает соединение с АPI сайта, запрашивает информацию
    и получает список фильмов
    """
    def __init__(self, user_id, genre, start_year, end_year):
        self.user_id = user_id
        self.genre = genre
        self.start_year = start_year
        self.end_year = end_year

    def selections_of_films(self):
        db_write = crud.create()

        movie_list = site_api.get_params()

        response = movie_list('GET', url,  headers, params, self.genre,
                              self.start_year, self.end_year)
        response = response.json()

        list_movie = MessageMovie.my_message(response)

        data = [{'id_user': self.user_id, 'genre': self.genre, 'message': list_movie}]
        db_write(db, History, data)

        return list_movie

with open('readme.md', 'w', encoding='utf-8') as file:
    result = '\nclass Movie' + Movie.__doc__
    file.write(result)


if __name__ == "__main__":

    Movie()