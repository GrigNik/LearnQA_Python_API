import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
number_of_redirects = len(response.history)
print("Number of redirects: ", number_of_redirects)
print("Final URL:", response.url)