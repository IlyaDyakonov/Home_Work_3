import requests
import json
import datetime

# устанавливаем параметры запроса к API Stack Overflow
params = {
    "fromdate": int(datetime.datetime.timestamp(datetime.datetime.now() - datetime.timedelta(days=2))),  # за последние два дня
    "order": "desc",
    "sort": "activity",
    "tagged": "python",
    "site": "stackoverflow"
}

# делаем запрос к API
response = requests.get("https://api.stackexchange.com/2.3/questions", params=params)

# обрабатываем ответ
if response.status_code == 200:
    data = json.loads(response.text)
    for item in data["items"]:
        print(item["title"])  # выводим заголовок вопроса
else:
    print("Ошибка при запросе к API: ", response.status_code)