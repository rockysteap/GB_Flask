# Сравнение разных подходов на примере парсинга сайтов.
#
# Перед нами задача по скачиванию информации с главных страниц пяти сайтов.
# Рассмотрим решение задачи с использованием
# синхронного, многопоточного, многопроцессорного и асинхронного подходов.
#
#
# Пример 1.
# Обычная синхронная загрузка
#
# В данном примере мы используем библиотеку requests для получения html-страницы каждого сайта из списка urls.
# Затем мы записываем полученный текст в файл с именем, соответствующим названию сайта.
"""
import requests
import time

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]
start_time = time.time()
for url in urls:
    response = requests.get(url)
    filename = 'sync_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")
"""
#
#
# Пример 2.
# Здесь мы создаем функцию download, которая загружает html-страницу и сохраняет ее в файл.
# Затем мы создаем по одному потоку для каждого сайта из списка urls,
# передавая функцию download в качестве целевой функции для каждого потока.
# Мы запускаем каждый поток и добавляем его в список threads.
# В конце мы ждем завершения всех потоков с помощью метода join.
"""
import requests
import threading
import time
urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]
def download(url):
    response = requests.get(url)
    filename = 'threading_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")
threads = []
start_time = time.time()
for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
"""
#
#
# Пример 3.
# Здесь мы используем модуль multiprocessing для создания процессов вместо потоков.
# Остальной код аналогичен предыдущему примеру.
"""
import requests
from multiprocessing import Process
import time

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]


def download(url):
    response = requests.get(url)
    filename = 'multiprocessing_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


processes = []
start_time = time.time()

if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
"""
#
#
# Пример 4.
# Здесь мы используем модуль asyncio для асинхронной загрузки страниц.
# Мы создаем функцию download, которая использует aiohttp для получения html-страницы
# и сохранения ее в файл. Затем мы создаем асинхронную функцию main,
# которая запускает функцию download для каждого сайта из списка urls и ожидает
# их завершения с помощью метода gather.
# Мы запускаем функцию main с помощью цикла событий asyncio.
"""
"""
import asyncio
import aiohttp
import time

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = 'asyncio_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            with open(filename, "w", encoding='utf-8') as f:
                f.write(text)
            print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
