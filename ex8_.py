import json
import requests

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
obj = json.loads(response.text)
time_to_sleep = obj['seconds']
token = obj['token']

payload = {'token':f"{token}"}
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
obj = json.loads(response.text)

if 'error' in response.json():
    error = obj['error']
    print(error)
else:
    if 'status' in response.json():
        status = obj['status']
        if status == "Job is NOT ready":
            print(f"Работа не готова, необходимо подождать {time_to_sleep} секунд")
            import time
            time.sleep(time_to_sleep)
            response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
            obj = json.loads(response.text)
            print(f"{obj['status']}. Результат: {obj['result']}")
        else:
            response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
            obj = json.loads(response.text)
            print(f"{obj['status']}. Результат: {obj['result']}")
    else:
        print("Пустой ответ на запрос")



