import pytest
import requests

class TestPhraseTerminal:

    # def test_phrase_input(self):
    #     answer = input("Please, enter word or phrase shorter than 15 symbols: ")
    #     assert len(answer) <= 15, f"You phrase is more than 15 symbols "


    def test_print_cookie(self):
        response1 = requests.get("https://playground.learnqa.ru/api/homework_cookie")

        # option #1 - checking value only
        actual_cookies = dict(response1.cookies)
        expected_cookies = "hw_value"
        assert expected_cookies in actual_cookies.values(), \
            f"The value of the actual cookie {actual_cookies} doesn't match the expected value {actual_cookies.values()}"

        # option #2  checking key and value
        actual_cookies = dict(response1.cookies)
        expected_cookies = {'HomeWork': 'hw_value'}
        assert expected_cookies == actual_cookies, \
            f"The value of the actual cookie {actual_cookies} doesn't match the expected value {expected_cookies}."