# app.py
from flask import Flask, request, jsonify

# Crea una nueva instancia de una aplicación Flask que se utilizará para manejar 
# solicitudes web y definir rutas, vistas y comportamientos específicos de la aplicación.
# __name__ variable especial en Python que se refiere al nombre del módulo en el que se encuentra el código.
app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

@app.route('/')
def index():
    return'Hola Flask!'

def _find_next_id():
    return max(country["id"] for country in countries) + 1

# @app hace referencia al objeto de tipo Flask creado al inicio
@app.get("/countries") 
# Dentro de los paréntesis indicamos una ruta
def get_countries():
    return jsonify(countries)

@app.get("/countries/<int:id>")
def get_country(id):
    for country in countries:
        if country['id'] == id:
            return country, 200
    return {"error": "Country not found"}, 404

@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415

if __name__=='__main__':  
    # por defecto usará la ip 0.0.0.0 y el puerto 5000
    # Esto implica que nuestra página web puede ser accesible desde otro ordenador
    # Al ponerlo en modo debug si se produce un error nos mostrará información relevante
    app.run(debug=True, host='0.0.0.0')
