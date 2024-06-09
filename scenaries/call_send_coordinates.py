import requests
import json

url = "http://localhost:8000/devices/send_coordinates"
data = {
  "collar_id": 13256,
  "latitude": 52.29778,
  "longitude": 104.29639,
  "timestamp": "2024-06-09 23:25:23"
}

response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
print(response.status_code, response.json())
