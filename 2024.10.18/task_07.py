# Написать запрос к сайту date.nager.at и получить все доступные страны.
# Вывести их на экран

import requests




if __name__ == '__main__':
    url = 'https://date.nager.at/api/v3/AvailableCountries'

    res = requests.get(url).json()

    for country in res:
        if country['name'] == 'Russia':
            print(f"Страна Россия, код {country['countryCode']} ")
