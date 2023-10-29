from flask import *
import requests
from app.funciones.funciones import *

profBP = Blueprint("prof", __name__)

rutaFichero = "ejercicioAPI2/ficheros/profesores.json"

# Encuentra el siguiente id para asignar
def _find_nextId():
    prof = leerFichero(rutaFichero)
    return max(profe['id'] for profe in prof) + 1

# Devuelve los profesores en el directorio
@profBP.get('/')
def getProf():
    prof = leerFichero(rutaFichero)
    return jsonify(prof)

# Devuelve el profesor en el directorio
@profBP.get('/<int:id>')
def getProfe(id):
    prof = leerFichero(rutaFichero)
    for profe in prof:
        if profe['id'] == id:
            return profe, 200
    return{"error":"profesor not found"}, 404

@profBP.post("/")
def addProfe():
    prof = leerFichero(rutaFichero)
    if request.is_json:
        profe = request.get_json()
        profe["id"] = _find_nextId()
        prof.append(profe)
        escribeFichero(rutaFichero, prof)
        return profe, 201
    return {"error":"Request must be JSON"}, 415

# Actualiza un recurso
@profBP.put("/<int:id>")
@profBP.patch("/<int:id>")
def modify_profe(id):
    prof = leerFichero(rutaFichero)
    if request.is_json:
        newProf = request.get_json()

        for profe in prof:
            if profe["id"] == id:
                for element in newProf:
                    profe[element] = newProf[element]
                    escribeFichero(rutaFichero,prof)
                return profe, 200
        return {"error":"profesor not found"}, 404
    
    return {"error": "No valid format"}, 415

# Elimina un recurso
@profBP.delete("/<int:id>")
def delete_profe(id):
    prof = leerFichero(rutaFichero)
    for profe in prof:
        if profe['id'] == id:
            prof.remove(profe)
            return "{}", 200
    
    return {"error": "Profesor not found"}, 404

if __name__ == '__main__':
    profBP.run(debug=True, host='0.0.0.0', port=5050)