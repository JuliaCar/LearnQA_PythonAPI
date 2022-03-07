import json.decoder
from datetime import datetime
from requests import Response


class BaseCase:
    @staticmethod
    def get_cookie(response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Can't find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    @staticmethod
    def get_header(response: Response, headers_name):
        assert headers_name in response.headers, f"Can't find header with the name {headers_name} in the last response"
        return response.headers[headers_name]

    @staticmethod
    def get_json_value(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not JSON format. Response test is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

        return response_as_dict[name]

    @staticmethod
    def prepare_registration_data(email=None):
        if email is None:
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            base_part = "learnqa"
            domain = "example.com"
            email = f"{base_part}{random_part}@{domain}"
        return {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

