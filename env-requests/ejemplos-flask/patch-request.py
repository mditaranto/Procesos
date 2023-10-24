import requests
api_url = "http://localhost:5050/countries/2"

# Creamos diccionario con los datos del nuevo todo
todo = {"area":5000}
response = requests.patch(api_url, json=todo)


print(response.status_code)
print(response.json())