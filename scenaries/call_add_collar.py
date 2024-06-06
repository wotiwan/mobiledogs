import requests
import json

url = "http://localhost:8000/add_collar"
data = {
    "reg_number": "58239",
    "nickname": "Strelka"
}

response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
print(response.status_code, response.json())
