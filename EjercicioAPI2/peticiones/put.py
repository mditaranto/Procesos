import requests

api_url = "http://127.0.0.1:5050/asignatura"

token = ''
cabecera = {'Authorization': f'Bearer {token}'}
dicc = {"IdProfesor": 3, "NumHoras": 6, "Titulo": "Lengua"}
response = requests.post(api_url, headers=cabecera, json= dicc)


print(response.json())
print(response.status_code)