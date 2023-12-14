import requests
import json

api = 'http://127.0.0.1:8000/api/employee/'
menu_id = 4
data = {
    "first_name":"Ahmed",
    "last_name":"Khan",
    "department": 1,
    "position": "Senior",
    "email" :'Asad741@gmail.com',
    "phone_number":"51472515",
    "hire_date":"2022-05-01",
}
url = f"{api}{menu_id}/"

response = requests.put(url, data=json.dumps(data), headers=({'Content-Type': 'application/json'}))
if response.status_code == 200:
    print("Employee instance created successfully.")
else:
    print(f"Failed to create Employee instance. Status code: {response.status_code}")
    print(response.content)
