import requests

class TestFirstAPI:
    def test_hello_call(self):
        url = "http://playground.learnqa.ru/api/hello"
        name = 'Julia'
        data = {'name': name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, f"wrong response code"

        response.dict =  response.json()
        assert "answer" in response.dict, "There is no field 'answer' in the response"

        expected_response_text = f"Hello, {name}"
        actual_response_text = response.dict["answer"]
        assert actual_response_text == expected_response_text, "Actual text in the response is not correct"