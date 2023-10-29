from flask import * 
from .asignatura.routes import asigBP
from .profesor.routes import profBP

app = Flask(__name__)

app.register_blueprint(asigBP,url_prefix="/asignatura")
app.register_blueprint(profBP,url_prefix="/profesores")