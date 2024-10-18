# Импорт модуля requests для выполнения HTTP-запросов
import requests

# сайт для получения цитат
url = 'http://api.forismatic.com/api/1.0/'

# создание словаря с параметрами запроса( метод для получения цитаты, формат ответа, язык запроса)
payload = {'method': 'getQuote', 'format': 'json', 'lang': 'ru'}

# выполнение запроса с параметром payload
res = requests.get(url, params=payload)


# парсинг JSON-отчета
data = res.json()

# вывод на экран
print(data)
