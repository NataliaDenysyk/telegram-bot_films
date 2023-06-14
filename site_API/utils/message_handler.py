import random
from typing import Dict


class MessageMovie:
    """
    Создает список фильмов из полученного файла
    """
    def my_message(files: Dict) -> list:
        list_file = []
        for i_key, i_value in enumerate(files):
            if i_value == 'results':
                for num in range(len(files[i_value])):
                    if files[i_value][num]['title'] \
                            and not files[i_value][num]['title'].startswith('Banned'):
                        list_file.append(files[i_value][num]['title'])

        random.shuffle(list_file)
        if len(list_file) > 10:
            return random.sample(list_file, 10)
        else:
            return list_file


with open('readme.md', 'w', encoding='utf-8') as file:
    result = '\nclass MessageMovie' + MessageMovie.__doc__
    file.write(result)

if __name__ == '__main__':
    MessageMovie()