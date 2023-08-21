import requests

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("1. Get запрос без параметра:", response.text, f". Код ответа:{response.status_code}")
print("")

response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
request_response = response.text
if not request_response:
    request_response = "метод возвращает пустой ответ"
else:
    request_response = response.text
print("2. Запрос не из списка:", f"{request_response}. Код ответа:{response.status_code}")
print("")

payload = {'method':"GET"}
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
print("3. Запрос с правильным значением method (GET-запрос с параметром GET):", response.text, f". Код ответа:{response.status_code}")
print("")

print("4. Проверка всех возможных сочетаний реальных типов запроса и значений параметра method с помощью цикла:")
for method in 'POST', 'GET', 'PUT', 'DELETE':
    payload = {'method':f"{method}"}
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
    print(f"Параметр {method} для GET запроса:",response.text, f". Код ответа:{response.status_code}")
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f"Параметр {method} для POST запроса:",response.text, f". Код ответа:{response.status_code}")
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f"Параметр {method} для PUT запроса:", response.text, f". Код ответа:{response.status_code}")
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f"Параметр {method} для DELETE запроса:", response.text, f". Код ответа:{response.status_code}")