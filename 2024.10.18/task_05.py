# Напишите программу, которая при запуске спрашивает
# "На каком языке вы хотите цитату?" и даёт выбор: 0 - Русский | 1 - Английский
# И в зависимости от выбора присылает цитату на выбранном языке.

import requests


def get_lang():
    lang = {0: 'ru', 1: 'en'}
    choice = int(input("На каком языке вы хотите цитату?\n0 - Русский | 1 - Английский: "))
    return lang.get(choice)


if __name__ == '__main__':
    url = 'http://api.forismatic.com/api/1.0/'

    payload = {'method': 'getQuote', 'format': 'json', 'lang': get_lang()}

    res = requests.get(url, params=payload)
    data = res.json()

    print(data)
