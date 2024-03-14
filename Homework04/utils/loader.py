import os
from time import time

import requests


class URLImageLoader:

    @staticmethod
    def get_image_from_url(url: str, path_to_save: str = './data/images') -> None:
        start_time = time()

        # Подготовка имени файла и пути. -----------------------------------------------------------------
        # Откинем url запрос после '?', если таковой имеется в адресе (см. 1 пример в 'data/images.lst')
        url_without_request = url[:url.find('?')] if url.count('?') else url
        # Найдем правую '/' и откинем всё, что слева
        file_name_with_extension = url_without_request[url.rfind('/') + 1:]
        # Разделим наименование файла на имя и расширение
        root, ext = os.path.splitext(file_name_with_extension)
        # Проверим, что у файла есть расширение, если нет назначим расширение по умолчанию -> '.jpg'
        ext = ext if ext else '.jpg'
        # Проверим, существует ли переданная директория, если нет, создадим её
        os.makedirs(os.path.abspath(path_to_save), exist_ok=True)
        # Сформируем полный путь до файла
        file_path = os.path.join(os.path.abspath(path_to_save), f'{root}{ext}')

        # Запись файла
        with open(file_path, 'wb') as f:
            data = requests.get(url).content
            f.write(data)

        print(f'{file_path} загружен за {time() - start_time:.2f} сек')

    @staticmethod
    async def async_get_image_from_url(url: str, path_to_save: str = '../data/images') -> None:
        start_time = time()
        url_without_request = url[:url.find('?')] if url.count('?') else url
        file_name_with_extension = url_without_request[url.rfind('/') + 1:]
        root, ext = os.path.splitext(file_name_with_extension)
        ext = ext if ext else '.jpg'
        os.makedirs(os.path.abspath(path_to_save), exist_ok=True)
        file_path = os.path.join(os.path.abspath(path_to_save), f'{root}{ext}')

        with open(file_path, 'wb') as f:
            data = requests.get(url).content
            f.write(data)

        print(f'{file_path} загружен за {time() - start_time:.2f} сек')
