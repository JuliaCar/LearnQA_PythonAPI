import allure

from lib.base_case import BaseCase
from lib.my_requests import MyRequests
from lib.assertions import Assertions


class TestUserDelete(BaseCase):
    @allure.description("Create new user for testing DELETE")
    def setup(self):
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post(f"/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        self.email = register_data['email']
        self.password = register_data['password']
        self.user_id = self.get_json_value(response1, "id")

    @allure.description("Delete auth user with ID 2")
    def test_delete_user_id2(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response, "user_id")

        response1 = MyRequests.delete(f"/user/{user_id_from_auth_method}",
                                      headers = {"x-csrf-token": token},
                                      cookies = {"auth_sid": auth_sid}
                                      )
        Assertions.assert_code_status(response1, 400)

    @allure.description("Delete just created auth user")
    def test_create_auth_delete_new_user(self):
        with allure.step(f"Login with new user"):
            login_data = {
                'email': self.email,
                'password': self.password
            }
            response2 = MyRequests.post(f"/user/login", data=login_data)
            Assertions.assert_code_status(response2, 200)

            auth_sid = self.get_cookie(response2, "auth_sid")
            token = self.get_header(response2, "x-csrf-token")

        with allure.step(f"Delete just created user"):
            response3 = MyRequests.delete(f"/user/{self.user_id}",
                                          headers = {"x-csrf-token": token},
                                          cookies = {"auth_sid": auth_sid}
                                          )
            Assertions.assert_code_status(response3, 200)

    @allure.description("Delete user with other auth user")
    def test_create_delete_new_user_auth_other_user(self):
        with allure.step(f"Login with existing user"):
            data = {
                'email': 'vinkotov@example.com',
                'password': '1234'
            }
            response1 = MyRequests.post("/user/login", data=data)

            auth_sid = self.get_cookie(response1, "auth_sid")
            token = self.get_header(response1, "x-csrf-token")

        with allure.step(f"Delete just created user with data existing user"):
            response2 = MyRequests.delete(f"/user/{self.user_id}",
                                          headers = {"x-csrf-token": token},
                                          cookies = {"auth_sid": auth_sid}
                                          )
            Assertions.assert_code_status(response2, 400)
