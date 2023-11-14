import requests

url=""

token = 'token_creado'
cabecera = {'Authorization': f'Bearer {token}'}
response = requests.get(url, headers=cabecera)

print("Codigo de estado: ", response.status_code)
#print(response.json())
if(response.status_code == 200):
    lista = response.json()
    for element in lista:
        for clave in element:
            print(clave, ": ", element[clave])
        print()
else:
    print("la peticion no ha terminado correctamente: ", response.status_code)