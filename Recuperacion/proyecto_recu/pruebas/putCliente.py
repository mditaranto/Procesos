import requests

data = {
      "nombre_cliente": "Maria rufo",
      "direccion_envio": "Calle Principal 123, Ciudad J",
      "correo_electronico": "pablo@example.com",
      "numero_telefono": "123-456-9999"
    }

user = {
    "username":"manu",
    "password":"cosano"
}

urlUser = 'http://127.0.0.1:9999/users'
urlCliente = 'http://127.0.0.1:9999/clientes/7'

resposeToken = requests.get(url=urlUser, json=user).json()
token = resposeToken.get('token')

headers = {"Authorization": f'Bearer {token}'}

respose = requests.put(url=urlCliente, json=data, headers=headers)
if (respose.status_code == 201):
    print ('Se ha creado el cliente')
elif (respose.status_code == 200):
    print ('Se ha modificado el cliente')
else:
    print ('tiene que ser JSON')


