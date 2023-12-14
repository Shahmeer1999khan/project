import requests

api = 'http://127.0.0.1:8000/api/employee/2'

resp = requests.get(api, headers={'Content-Type': 'application/json'})
if resp.status_code == 200:
    data = resp.json()
    print(data)
else:
    print(f"Request failed with status code: {resp.status_code}")
