import requests
import json

# Вызов API и сохранение ответа
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Анализ структур данных
response_dist = r.json()
readable_file = 'plotting/api/data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dist, f, indent=4)