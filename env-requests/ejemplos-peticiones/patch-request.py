import requests

api_url = "https://jsonplaceholder.typicode.com/todos/2"
todo = {'title': 'Mow lawn'}
response = requests.patch(api_url, json=todo)

print(response.json())
print(response.status_code)
