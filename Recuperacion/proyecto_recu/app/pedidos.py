from flask import *
from flask_jwt_extended import jwt_required
import functions

pedidosBP = Blueprint('pedidos', __name__)

def find_next_id():
    pedidos = functions.leeFichero('proyecto_recu/ficheros/pedidos.json')
    return max(pedido['id_pedido'] for pedido in pedidos) + 1

@pedidosBP.post('/')
@jwt_required()
def postPedido():
    if request.is_json:
        pedidos = functions.leeFichero('proyecto_recu/ficheros/pedidos.json')
        clientes = functions.leeFichero('proyecto_recu/ficheros/clientes.json')

        newPedido = request.get_json()
        idCliente = newPedido['id_cliente']

        #Si el cliente existe, se crea el pedido con un nuevo id
        for cliente in clientes:
            if(cliente['id_cliente'] == idCliente):
                newPedido['id_pedido'] = find_next_id()
                pedidos.append(newPedido)
                functions.escribeFichero('proyecto_recu/ficheros/pedidos.json', pedidos)
                return newPedido, 201
        
        return 'Id cliente no encontrado', 404
    else:
        return 'No es un json', 415

    