from flask import *
import requests
from app.funciones.funciones import *

asigBP = Blueprint("asig", __name__)

asigFichero = "EjercicioAPI2/ficheros/asignatura.json"
profFichero= "EjercicioAPI2/ficheros/profesores.json"

@asigBP.get('/')
def getAsig():
    asig = leerFichero(asigFichero)
    return(asig)

@asigBP.get('/<int:id>')
def getAsignatura(id):
    asig = leerFichero(asigFichero)
    for asigna in asig:
        if asigna['id'] == id:
            return asigna, 200
    return{"error":"Asignatura not found"}, 404

@asigBP.post("/")
def addAsig():
    Asig = leerFichero(asigFichero)
    if request.is_json:
        Asigna = request.get_json()
        Asigna["id"] = _find_nextId()
        
        Asig.append(Asigna)
        escribeFichero(asigFichero,Asig)
        return Asigna, 201
    return {"error":"Request must be JSON"}, 415

@asigBP.put("/<int:id>")
@asigBP.patch("/<int:id>")
def modify_Asig(id):
    Asig = leerFichero(asigFichero)
    if request.is_json:
        newAsig = request.get_json()

        for Asigna in Asig:
            if Asigna["id"] == id:
                for element in newAsig:
                    Asigna[element] = newAsig[element]
                    escribeFichero(asigFichero,Asig)
                return Asigna, 200
        return {"error":"Agignatura not found"}, 404
    
    return {"error": "No valid format"}, 415

@asigBP.delete("/<int:id>")
def delete_Asig(id):
    Asig = leerFichero(asigFichero)
    for Asigna in Asig:
        if Asigna['id'] == id:
            Asigna.remove(Asigna)
            return "{}", 200
    
    return {"error": "Agignatura not found"}, 404

@asigBP.get("/<int:id>/profesores")
def get_Profes(id):
    list = []
    prof = leerFichero(profFichero)
    for profe in prof:
        if profe['id'] == id:
            list.append(profe)
    if len(list) > 0:
        return list, 200
    else:
        return {"error": "No profesores for this asignatura"}, 404

if __name__ == '__main__':
    asigBP.run(debug=True, host='0.0.0.0', port=5050)
