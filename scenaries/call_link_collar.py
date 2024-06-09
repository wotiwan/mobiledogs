import requests
import json

url = "http://localhost:8000/link_collar"
data = {
  "reg_number": {
    "reg_number": 13256
  },
  "uid": {
    "id": 1
  }
}

response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
print(response.status_code, response.json())
