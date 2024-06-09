import requests
import json

url = "http://localhost:8000/get_track"
data = {
  "collar_id": 13256,
  "start_time": "2023-01-01",
  "end_time": "2025-01-01"
}

response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))
print(response.status_code, response.json())
