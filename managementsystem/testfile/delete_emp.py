import requests
import json

api = 'http://127.0.0.1:8000/api/employee/'
Menu_id = 1

url = f'{api}{Menu_id}'
response = requests.delete(url)
