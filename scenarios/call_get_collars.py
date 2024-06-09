import requests
import json

url = "http://localhost:8000/devices/get_collars"

response = requests.get(url, headers={"Content-Type": "application/json"})
print(response.status_code, response.json())
