import requests
import json

url = "http://localhost:8000/create_user"
data = {
    "nickname": "wotiwan",
    "email": "iwanpomogaev@yandex.ru",
    "password": "12345"
}

response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
print(response.status_code, response.json())
