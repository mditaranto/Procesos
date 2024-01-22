import secrets
import string

from flask import Flask
from flask_jwt_extended import JWTManager
from cliente import clienteBP
from pedidos import pedidosBP
from users import usersBP

alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(8))

matiServer = Flask(__name__)

matiServer.register_blueprint(clienteBP, url_prefix='/clientes')
matiServer.register_blueprint(pedidosBP, url_prefix='/pedidos')
matiServer.register_blueprint(usersBP, url_prefix='/users')


matiServer.config['SECRET_KEY'] = password
jwt = JWTManager(matiServer)

if (__name__ == '__main__'):
    matiServer.run(host="0.0.0.0", port='9999', debug=True)
