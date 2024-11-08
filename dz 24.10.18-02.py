# Выведите три ближайших праздника и через сколько дней они будут.

import requests

url = 'https://date.nager.at/api/v3/NextPublicHolidays/RU'

res = requests.get(url)

data = res.json()

print("три ближайших праздника:")
for i in enumerate(data[:3]):
    print(f"Праздник {i}")
