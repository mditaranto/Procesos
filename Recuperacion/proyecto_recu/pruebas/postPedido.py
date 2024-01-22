import requests

urlPedidos = 'http://127.0.0.1:9999/pedidos'
urlUser = 'http://127.0.0.1:9999/users'

json = {
      "fecha_pedido": "2024-01-14",
      "total_pedido": 200.75,
      "estado_pedido": "En proceso",
      "id_cliente": 2
    }

user = {
    "username":"manu",
    "password":"cosano"
}

resposeToken = requests.get(url=urlUser, json=user).json()
token = resposeToken.get('token')

headers = {"Authorization" : f'Bearer {token}'}

respose = requests.post(url=urlPedidos, json=json, headers=headers)
if (respose.status_code == 201):
    print ('Se ha creado el pedido')
elif (respose.status_code == 404):
    print ('Cliente no encontrado')
else:
    print ('tiene que ser JSON')