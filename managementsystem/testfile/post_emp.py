import requests
import json

api = 'http://127.0.0.1:8000/api/employee/'

data = {
    
    "first_name": "Shahmeer",
    "last_name": "Ahmed",
    "position": "Manager",
    "email": "shahmeer000@gmail.com",
    "phone_number": "++9212345678",
    "hire_date": "2022-05-01",
    "user": 6,
    "department": 1
}

response = requests.post(api, data=json.dumps(data), headers=({'Content-Type': 'application/json'}))
if response.status_code == 200:
    print("Employee instance created successfully.")
else:
    print(f"Failed to create Employee instance. Status code: {response.status_code}")
    print(response.content)