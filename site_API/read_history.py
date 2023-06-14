from data_base.common.models import db, History
from data_base.core import crud


def get_history_movie(user_id: int) -> list[list]:
    """
        Создает список последних трех ответов бота пользователю из базы данных
        :param user_id: ID пользователя
        :return: список списков фильмов
        """
    list_history = []
    db_read = crud.retrieve()
    retrieved = db_read(db, History, History.id_user,
                        History.genre, History.message)
    for element in retrieved:
        if element.id_user == user_id:
            list_history.append(element.message)
    end = len(list_history)

    return list_history[end-3:end]


with open('readme.md', 'w', encoding='utf-8') as file:
    result = '\ndef get_history_movie' + get_history_movie.__doc__
    file.write(result)


if __name__ == "__main__":
    get_history_movie()
