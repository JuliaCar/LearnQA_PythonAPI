import pytest
import string
import random
import requests
import allure

from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

@allure.epic("Registration cases")
class TestUserRegister(BaseCase):
    broken_email = {
        "@example.com",
        "vinkotovexample.com",
        "vinkotov@com",
        "vinkotov@example"
    }
    @allure.description("Create user successfully")
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("Create user with existing email")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected response content {response.content}."

    @allure.description("Create user without @")
    def test_create_user_without_at(self):
        """
        Create new user with incorrect email format without @ symbol
        """
        email = 'vinkotovexample.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format",\
            f"Invalid email format in the {email}"

    @allure.description("User not able to register with an email that does not have one of the necessary components")
    @pytest.mark.parametrize('email', broken_email)
    def test_without_one_parametr(self, email):
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format",\
            f"Invalid email format in the {email}"

    @allure.description("Create user without short name - 1 symbol")
    def test_create_user_short_name(self):
        """
        Create user with length of the name - 1 symbol
        """
        random_letter = ''.join(random.choices(string.ascii_lowercase + string.digits, k=1))
        email = f"{random_letter}@j@example.com"
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("Create user without long name - more that 250 symbols")
    def test_create_user_long_name(self):
        """
        Create user with length of the name - more than 250 symbols
        """
        random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=255))
        email = f"{random_name}@j@example.com"
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'email' field is too long",\
            f"The value of 'email' field is too long in the {email}."

    # user_agent_params = [
    #     "no_device",
    #     "no_browser",
    #     "no_platform"
    # ]
    #
    # @pytest.mark.parametrize('condition', user_agent_params)
    # def test_user_agent(self, condition):
    #     device = {
    #         "iOS",
    #         "Android"
    #     }
    #     response = requests.get("/user_agent_check/", headers={"User-Agent": device})
    #     print(response.text, response)
