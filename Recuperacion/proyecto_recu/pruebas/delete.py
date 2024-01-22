import requests

user = {
    "username":"manu",
    "password":"cosano"
}

urlUser = 'http://127.0.0.1:9999/users'
urlCliente = 'http://127.0.0.1:9999/clientes/4' #Funcional
urlCliente2 = 'http://127.0.0.1:9999/clientes/76' #Cliente no existe

resposeToken = requests.get(url=urlUser, json=user).json()
token = resposeToken.get('token')

headers = {"Authorization": f'Bearer {token}'}

respose = requests.delete(url=urlCliente, headers=headers)
if (respose.status_code == 200):
    print("El cliente se elimino correctamente")
elif (respose.status_code == 404):
    print("Cliente no encontrado")
else:
    print("Hubo un error")
