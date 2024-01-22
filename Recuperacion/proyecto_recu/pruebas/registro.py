import requests

url = "http://127.0.0.1:9999/users"

user = {
    "username": "manu",
    "password": "cosano"
}

response = requests.post(url=url, json=user)

if (response.status_code == 201):
    print("Usuario registrado correctamente")
else:
    print("Se ha producido un error")
    print(response.text)
