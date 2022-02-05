import requests
from json.decoder import JSONDecodeError
from time import sleep

# задание 5
json_text = requests.get("https://gist.github.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37")
print(json_text.text)

try:
    parsed_json_text = json_text.json()
    print(parsed_json_text)
except JSONDecodeError:
    print("Response is not JSON format")


# задание 6
response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
print(len(response.history))   #3
first_response = response.history[0]
second_response = response.history[1]
third_response = response.history[2]


print(first_response.url)  #https://playground.learnqa.ru/api/long_redirect
print(second_response.url) #https://playground.learnqa.ru/
print(third_response.url)  #https://learnqa.ru/


# задание 7
# задание 7.1
response = requests.get("", params="get")
print(response)
# requests.exceptions.MissingSchema: Invalid URL '': No schema supplied. Perhaps you meant http://?

# задание 7.2
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data="HEAD")
print(response)
#<Response [400]>

# задание 7.3
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data="PUT")
print(response)
# <Response [200]>

# задание 7.4
#  Не смогла пройтись двойным loop, почемуто не работает :(
# method_lst = ["get"] #, "post", "put", "delete"]
# parameters_lst = [{"method": "GET"}, {"method": "POST"}, {"method": "PUT"}, {"method": "DELETE"}]
#
# for i in method_lst:
#     for parameter in parameters_lst:
#         response = requests.i("https://playground.learnqa.ru/ajax/api/compare_query_type", params=parameter)


parameters_list = [{"method":"GET"}, {"method":"POST"}, {"method":"PUT"}, {"method":"DELETE"}]

for param in parameters_list:
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"Method GET with parameter params={param} has following response {response} with status code {response.status_code}")
        response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"Method POST with parameter data={param} has following response {response} with status code {response.status_code}")
        response  = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"Method PUT with parameter data={param} has following response {response} with status code {response .status_code}")
        response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"Method DELETE with parameter data={param} has following response {response} with status code {response .status_code}")

#response
# Method GET with parameter {'method': 'GET'} has following response <Response [200]> with status code 200          # Correct
# Method POST with parameter data={'method': 'GET'} has following response <Response [200]> with status code 200    # Wrong
# Method PUT with parameter data={'method': 'GET'} has following response <Response [200]> with status code 200     # Wrong
# Method DELETE with parameter data={'method': 'GET'} has following response <Response [200]> with status code 200  # Wrong
# Method GET with parameter {'method': 'POST'} has following response <Response [200]> with status code 200         # Wrong
# Method POST with parameter data={'method': 'POST'} has following response <Response [200]> with status code 200   # Correct
# Method PUT with parameter data={'method': 'POST'} has following response <Response [200]> with status code 200          # Wrong
# Method DELETE with parameter data={'method': 'POST'} has following response <Response [200]> with status code 200       # Wrong
# Method GET with parameter {'method': 'PUT'} has following response <Response [200]> with status code 200                # Wrong
# Method POST with parameter data={'method': 'PUT'} has following response <Response [200]> with status code 200          # Wrong
# Method PUT with parameter data={'method': 'PUT'} has following response <Response [200]> with status code 200           # Wrong
# Method DELETE with parameter data={'method': 'PUT'} has following response <Response [200]> with status code 200        # Correct
# Method GET with parameter {'method': 'DELETE'} has following response <Response [200]> with status code 200             # Wrong
# Method POST with parameter data={'method': 'DELETE'} has following response <Response [200]> with status code 200      # Wrong
# Method PUT with parameter data={'method': 'DELETE'} has following response <Response [200]> with status code 200      # Wrong
# Method DELETE with parameter data={'method': 'DELETE'} has following response <Response [200]> with status code 200   # Correct

# задание 8
#1) создавал задачу
task = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
parsed_task = task.json()
print(parsed_task)
token = parsed_task["token"]
seconds = parsed_task["seconds"]
payload = {"token": token}

# 2)cделал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
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
    print("You test is very flaky")
