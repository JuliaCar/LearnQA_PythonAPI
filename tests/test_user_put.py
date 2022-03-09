import allure

from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


@allure.epic("Negative tests for put")
class TestUserPut(BaseCase):
    @allure.description("Login with valid credentials and get user info")
    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = MyRequests.post("/user/login", data=data)
        self.auth_sid = self.get_cookie(response, "auth_sid")
        self.token = self.get_header(response, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response, "user_id")

    @allure.description("Change user data without authorization")
    def test_change_user_data_without_auth(self):
        new_lastname = "Clone"
        response = MyRequests.put(f"/user/10",
                                  data={'firstName': new_lastname}
                                  )
        Assertions.assert_code_status(response, 400)

    @allure.description("Change user data with authorization with other user")
    def test_change_user_data_with_auth_other_user(self):
        new_lastname = "Cardenas"
        response1 = MyRequests.put(f"/user/6",
                                   headers={"x-csrf-token": self.token},
                                   cookies={"auth_sid": self.auth_sid},
                                   data={'lastName': new_lastname}
                                   )
        Assertions.assert_code_status(response1, 400)

    @allure.description("Change authorized user's email to new email without @")
    def test_change_auth_eser_wrong_email(self):
        new_email = 'vinkotovexample.com'
        response1 = MyRequests.put(f"/user/{self.user_id_from_auth_method}",
                                   headers={"x-csrf-token": self.token},
                                   cookies={"auth_sid": self.auth_sid},
                                   data={'email': new_email})
        Assertions.assert_code_status(response1, 400)

    @allure.description("Change authorized user's firstName to new 1 symbol firstName")
    def test_change_auth_users_name_to_new_1symbol(self):
        new_firstname = "S"
        response1 = MyRequests.put(f"/user/{self.user_id_from_auth_method}",
                                   headers={"x-csrf-token": self.token},
                                   cookies={"auth_sid": self.auth_sid},
                                   data={'email': new_firstname})
        Assertions.assert_code_status(response1, 400)
