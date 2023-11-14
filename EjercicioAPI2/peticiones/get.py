import requests

api_url = "http://127.0.0.1:5050/users"

dicc = {"username":"Manu", "password":"cosano"}

response = requests.get(api_url, json= dicc)
print(response.json())
print(response.status_code)