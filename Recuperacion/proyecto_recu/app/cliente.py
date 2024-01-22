from flask import *
from flask_jwt_extended import jwt_required
import functions

clienteBP = Blueprint('cliente', __name__)

@clienteBP.get('/<int:id>/total')
def getCliente(id):
    
    pedidos = functions.leeFichero("proyecto_recu/ficheros/pedidos.json")
    cantidad = 0
    #Si el pedido es igual al id del cliente, se suma
    for pedido in pedidos:
        if(pedido['id_cliente'] == id):
            cantidad += pedido['total_pedido']
    return jsonify({'cantidad': cantidad })

@clienteBP.get('/<int:id>/pedidos/<int:idPedido>')
def getPedido(id, idPedido):
    
    pedidos = functions.leeFichero("proyecto_recu/ficheros/pedidos.json")
    #Si el id del cliente coincide y el del pedido tambien, lo devuelve
    for pedido in pedidos:
        if(pedido['id_cliente'] == id):
            if(pedido['id_pedido'] == idPedido):
                return pedido, 200
            
    return jsonify({'no se ha encontrado el pedido'}), 404

@clienteBP.put('/<int:id>')
@jwt_required()
def putCliente(id):

    if request.is_json:
        clientes = functions.leeFichero('proyecto_recu/ficheros/clientes.json')
        newCliente = request.get_json()
        newCliente['id_cliente'] = id

        #Si el id del cliente coincide, se modifica
        for cliente in clientes:
            if cliente['id_cliente'] == id:
                for element in cliente:
                    cliente[element] = newCliente[element]
                    functions.escribeFichero("proyecto_recu/ficheros/clientes.json", clientes)
                    return jsonify(cliente), 200
        #En caso que el id no coincida se crea el cliente
        else:
            newCliente['id_cliente'] = id
            clientes.append(newCliente)
            functions.escribeFichero('proyecto_recu/ficheros/clientes.json', clientes)
            return jsonify(newCliente), 201
    return jsonify({'Tiene que ser JSON'}), 401

@clienteBP.delete('/<int:id>')
@jwt_required()
def deleteCliente(id):
    
    clientes = functions.leeFichero('proyecto_recu/ficheros/clientes.json')

    #Si algun id cliente coincide con el introducido, se elimina
    for cliente in clientes:
        if(cliente['id_cliente'] == id):
            clientes.remove(cliente)
            functions.escribeFichero('proyecto_recu/ficheros/clientes.json', clientes)
            return {}, 200
    return 'No se ha encontrado el id del cliente', 404