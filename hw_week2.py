import requests
from json.decoder import JSONDecodeError
from time import sleep

# # задание 5
json_text = requests.get("https://gist.github.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37")
print(json_text.text)

try:
    parsed_json_text = json_text.json()
    print(parsed_json_text)
except JSONDecodeError:
    print("Response is not JSON format")


# задание 6
# С помощью конструкции response.history необходимо узнать,
# сколько редиректов происходит от изначальной точки назначения до итоговой. И какой URL итоговый.
# вариант №1
response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
print(len(response.history))
print(response.history[len(response.history)-1].url)
# вариант №2
response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
print(len(response.history))
for i in range(0, len(response.history)):
    print(response.history[i].url)


# # задание 7
# # задание 7.1
# response = requests.get("", params="get")
# print(response.text)
# # requests.exceptions.MissingSchema: Invalid URL '': No schema supplied. Perhaps you meant http://?

# # задание 7.2
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data="HEAD")
print(response.text)

#
# # # задание 7.3
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data="PUT")
print(response.text)

# # задание 7.4 вариант №1
METHODS = [{"method": "GET"}, {"method": "POST"}, {"method": "PUT"}, {"method": "DELETE"}]
METHODS_FUNC = [requests.get, requests.post, requests.put, requests.delete]

for meth in METHODS_FUNC:
    if meth.__name__ == "get":
        for param in METHODS:
            response = meth("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
            print(f"{meth.__name__}, method: {param['method']}: {response.text}")
    else:
        for param in METHODS:
            response = meth("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
            print(f"{meth.__name__}, method: {param['method']}: {response.text}")

# вариант №2
parameters_list = [{"method":"GET"}, {"method":"POST"}, {"method":"PUT"}, {"method":"DELETE"}]
for param in parameters_list:
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"Method GET with parameter params={param} has following response {response.text} with status code {response.status_code}")
        response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"Method POST with parameter data={param} has following response {response.text} with status code {response.status_code}")
        response  = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"Method PUT with parameter data={param} has following response {response.text} with status code {response .status_code}")
        response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"Method DELETE with parameter data={param} has following response {response.text} with status code {response .status_code}")


# # задание 8
# #1) создавал задачу
task = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
parsed_task = task.json()
print(parsed_task)
token = parsed_task["token"]
seconds = parsed_task["seconds"]
payload = {"token": token}

# # 2)cделал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
response_before = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
parsed_response_before = response_before.json()
response_status_before = parsed_response_before["status"]
print(response_status_before)
assert response_status_before == "Job is NOT ready", f"Expected status 'Job is NOT ready', but got {response_status_before}"

# 3)ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
sleep(seconds)

#4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result

response_after = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
parsed_response_after = response_after.json()
response_status_after = parsed_response_after["status"]
response_result_after = parsed_response_after["result"]
assert response_status_after == "Job is ready", f"Expected status 'Job is ready', but got {response_status_after}"
if int(response_result_after) > 0:
    print(f"{response_status_after} with result {response_result_after}")
else:
    print("Your test is very flaky")
