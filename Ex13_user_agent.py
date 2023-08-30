import pytest
import requests

class TestUserAgent:
    user_agent = "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
    user_agent1 = "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"
    user_agent2 = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    user_agent3 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"
    user_agent4 = "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"

    result = {"platform": "Mobile","browser": "No","device": "Android"}
    result1 = {"platform": "Mobile","browser": "Chrome","device": "iOS"}
    result2 = {"platform": "Googlebot","browser": "Unknown","device": "Unknown"}
    result3 = {"platform": "Web","browser": "Chrome","device": "No"}
    result4 = {"platform": "Mobile","browser": "No","device": "iPhone"}

    params = [
        (user_agent, result, "User Agent 1"),
        (user_agent1, result1, "User Agent 2"),
        (user_agent2, result2, "User Agent 3"),
        (user_agent3, result3, "User Agent 4"),
        (user_agent4, result4, "User Agent 5")
    ]



    @pytest.mark.parametrize('user_agent_in', params)
    def test_user_agent_check(self, user_agent_in):
        user_agent_value = user_agent_in[0]
        expected_result = user_agent_in[1]
        number_of_user_agent = user_agent_in[2]

        payload = {'User-Agent':f"{user_agent_value}"}
        response = requests.get(
                "https://playground.learnqa.ru/ajax/api/user_agent_check",
                headers=payload
            )
        platform = response.json()["platform"]
        browser = response.json()["browser"]
        device = response.json()["device"]

        assert platform == expected_result['platform'], f"{number_of_user_agent} - not correct. Response parameter 'platform' are NOT correct: {platform}. Expected: {expected_result['platform']}"
        assert browser == expected_result['browser'], f"{number_of_user_agent} - not correct. Response parameter 'browser' are NOT correct: {browser}. Expected: {expected_result['browser']}"
        assert device == expected_result['device'], f"{number_of_user_agent} - not correct. Response parameter 'device' are NOT correct: {device}. Expected: {expected_result['device']}"



