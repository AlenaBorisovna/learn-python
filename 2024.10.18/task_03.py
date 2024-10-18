import requests

url = 'http://api.forismatic.com/api/1.0/'
payload = {'method': 'getQuote', 'format': 'json', 'lang': 'en'}
res = requests.get(url, params=payload)

data = res.json()
data1 = res.text

print(data, data1)