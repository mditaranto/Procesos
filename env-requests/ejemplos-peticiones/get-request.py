import requests, json
api_url = "https://jsonplaceholder.typicode.com/photos/2"
response = requests.get(api_url)
print(response.status_code)
res = response.json()

for key in res:
    print(key, "->", res[key])
