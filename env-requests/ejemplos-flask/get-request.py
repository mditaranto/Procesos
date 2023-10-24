import requests
api_url = "http://localhost:5050/countries/4"
response = requests.get(api_url)
print(response.status_code)
print(response.json())