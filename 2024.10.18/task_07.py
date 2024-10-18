# Написать запрос к сайту date.nager.at и получить все доступные страны.
# Вывести их на экран

import requests

url = 'https://date.nager.at/api/v3/AvailableCountries'
payload = {'countryCode': '', 'name': ''}
res = requests.get(url, params=payload)
country = res.json()
print(country)
