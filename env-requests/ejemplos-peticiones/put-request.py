import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"

# Petción GET
response = requests.get(api_url)
print(response.json())

# Construimos el diccionario con los datos a modificar
todo = {'userId':1, 'title': 'Wash car', 'completed': True}

# Realizamos petición PUT
response = requests.put(api_url, json=todo)
print(response.json())
print(response.status_code)