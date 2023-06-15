import random
from typing import Dict


class MessageMovie:
    """
    Создает список фильмов и постеров к ним из полученного файла
    """
    def my_message(files: Dict) -> list:
        list_file = []
        image_file = []
        for i_key, i_value in enumerate(files):
            if i_value == 'results':
                for num in range(len(files[i_value])):
                    if files[i_value][num]['title'] \
                            and not files[i_value][num]['title'].startswith('Banned'):
                        image_file.append(files[i_value][num]['imageurl'])
                        list_file.append(files[i_value][num]['title'])

        file_zip = list(zip(list_file, image_file))

        random.shuffle(file_zip)
        if len(file_zip) > 10:
            return random.sample(file_zip, 10)
        else:
            return file_zip


with open('readme.md', 'w', encoding='utf-8') as file:
    result = '\nclass MessageMovie' + MessageMovie.__doc__
    file.write(result)

if __name__ == '__main__':
    MessageMovie()