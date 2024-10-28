# Выведите все праздники для России на 2024 год

import requests

url = 'https://date.nager.at/api/v3/PublicHolidays/2024/RU'

res = requests.get(url)

data = res.json()

print("праздники для России на 2024 год:")
for i in enumerate(data):
    print(f"Праздник {i}")
