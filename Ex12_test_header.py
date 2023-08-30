import requests
#'x-secret-homework-header': 'Some secret value'

class TestHeader:
    def test_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        header_name = response.headers.get('x-secret-homework-header')

        assert header_name == "Some secret value", "Не получены необходимые header"






