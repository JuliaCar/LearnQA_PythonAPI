import pytest
import requests
import json
from json.decoder import JSONDecodeError

class TestPhraseTerminal:

    # def test_phrase_input(self):
    #     """
    #     Пользователь вводит фразу меньше 15 символов
    #     Проверяем кол-во симовлов в фразе
    #     """
    #     answer = input("Please, enter word or phrase shorter than 15 symbols: ")
    #     assert len(answer) <= 15, f"You phrase is more than 15 symbols "
    #
    #
    # def test_print_cookie(self):
    #     """
    #     Запрос на метод "https://playground.learnqa.ru/api/homework_cookie"
    #     Сравниваем полученное значение cookie с ожидаемым
    #     """
    #     response1 = requests.get("https://playground.learnqa.ru/api/homework_cookie")
    #
    #     # option #1 - checking value only
    #     actual_cookies = dict(response1.cookies)
    #     expected_cookies = "hw_value"
    #     assert expected_cookies in actual_cookies.values(), \
    #         f"The value of the actual cookie {actual_cookies} doesn't match the expected value {actual_cookies.values()}"
    #
    #     # option #2  checking key and value
    #     actual_cookies = dict(response1.cookies)
    #     expected_cookies = {'HomeWork': 'hw_value'}
    #     assert actual_cookies == expected_cookies, \
    #         f"The value of the actual cookie {actual_cookies} doesn't match the expected value {expected_cookies}."
    #
    # def test_header_method(self):
    #     """
    #     Запрос на метод https://playground.learnqa.ru/api/homework_header
    #     Сравниваем полученное значение header с ожидаемым
    #     """
    #     response = requests.get("https://playground.learnqa.ru/api/homework_header")
    #     parsed_response_text = response.json()
    #     expected_header = {'success': '!'}
    #     assert parsed_response_text == expected_header, \
    #         f"The value of the actual header {parsed_response_text} doesn't match the expected value {expected_header}"

    # Uses-Agent = [
    #     ("platform"),
    #     ("browser = [
    #     ("Chrome"),
    #     ("Firefox"),
    #     ("Unknown")
    # ]


    # @pytest.mark.parametrize('condition', exclude_params)
    def test_user_agent(self):
        url = "https://gist.github.com/KotovVitaliy/138894aa5b6fa442163561b5db6e2e26"
        data = 'User Agent'

        response = requests.get(url, params=data)
        print(response.headers)
