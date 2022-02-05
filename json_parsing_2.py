from json.decoder import JSONDecodeError
import requests

# response = requests.get("https://playground.learnqa.ru/api/hello", params={"name":"User"})
# parsed_response_text = response.json()
# print(parsed_response_text["answer"])
#
# response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)
#
# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except JSONDecodeError:
#     print("Response is not JSON format")

# response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1":"value1"})
# print(response.text)
#
# response = requests.put("https://playground.learnqa.ru/api/check_type", data={"param1":"value1"})
# print(response.text)

# response = requests.post("https://playground.learnqa.ru/api/check_type")
# print(response.status_code)

# response = requests.post("https://playground.learnqa.ru/api/somthing")
# print(response.status_code)
# print(response.text)

# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)  #False -> 301, True -> 200
# print(response.status_code)

# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# first_response = response.history[0]
# second_response = response
# print(first_response.url)  #https://playground.learnqa.ru/api/get_301
# print(second_response.url)  #https://www.learnqa.ru/

# headers = {"some_header":"123"}
# response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers = headers)
# print(response.text) #заголовки запроса
# print(response.headers)  #заголовки ответа

#cookies получение
# payload = {"login":"secret_login", "password":"secret_pass"}
# response = requests.post("https://playground.learnqa.ru/api/get_cookie", data=payload)
# print(response.text) #no text
# print(response.status_code)
# print(dict(response.cookies))
# print(response.headers)

# получение и передача cookies
# payload = {"login": "secret_login", "password": "secret_pass"}
# response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
# cookie_value = response1.cookies.get('auth_cookies')
# cookies = {}
# if cookie_value is not None:
#     cookies.update({'auth_cookie': cookie_value})
#
# response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
#
# print(response2.text)