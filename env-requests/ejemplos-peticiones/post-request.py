import requests
api_url = "http://localhost:5050/countries"

# Creamos diccionario con los datos del nuevo todo
todo = {"area":10000, "capital":"Madrid", "name": "España"}
response = requests.post(api_url, json=todo)

# Imprimimos el JSON de la respuesta
print(response.json())

# Imprimimos el estado de la respuesta para ver cómo ha ido
print("Código de estado:", response.status_code)
