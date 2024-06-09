import requests
import json

url = "http://localhost:8000/devices/add_collar"
data = {
    "reg_number": "41452",
    "nickname": "Stredlka"
}

response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
print(response.status_code, response.json())
