from flask import Flask
from .asignatura.routes import asigBP
from .profesor.routes import profBP

app = Flask(__name__)

# Registramos los blueprints: primero se indica el nombre
# del Blueprint, en url_prefix indicamos el prefijo de la URL
app.register_blueprint(asigBP, url_prefix='/countries')
app.register_blueprint(profBP, url_prefix='/cities')

