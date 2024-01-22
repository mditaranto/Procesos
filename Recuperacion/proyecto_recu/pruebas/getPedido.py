import requests

url='http://127.0.0.1:9999/clientes/2/pedidos/102'

respose = requests.get(url)

if (respose.status_code == 200):
    print (respose.json())
else:
    print ('Ha ocurrido un error')