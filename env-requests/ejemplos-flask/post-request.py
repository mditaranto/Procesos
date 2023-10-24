import requests
api_url = "http://localhost:5050/countries"

# Creamos diccionario con los datos del nuevo todo
todo = {"area":3000, "capital":"Madrid", "name": "España"}
response = requests.post(api_url, json=todo)


print(response.status_code)
print(response.json())