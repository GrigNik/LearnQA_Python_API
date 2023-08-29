import requests



class TestCookie:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie_name = response.cookies.get('HomeWork')

        assert cookie_name == "hw_value", "Не получены необходимые cookie"



