from flask import * 
from flask_jwt_extended import JWTManager
from .asignatura.routes import asigBP
from .profesor.routes import profBP
from .users.routes import usersBP
from .funciones.funciones import randomPass

app = Flask(__name__)
app.config['SECRET_KEY'] = randomPass()
jwt = JWTManager(app)

app.register_blueprint(asigBP,url_prefix="/asignatura")
app.register_blueprint(profBP,url_prefix="/profesores")
app.register_blueprint(usersBP,url_prefix="/users")