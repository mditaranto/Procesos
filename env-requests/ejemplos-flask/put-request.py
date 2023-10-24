import requests
api_url = "http://localhost:5050/countries/4"

# Creamos diccionario con los datos del nuevo todo
todo = {"area":4000, "capital":"Londres", "name": "Inglaterra"}
response = requests.put(api_url, json=todo)


print(response.status_code)
print(response.json())