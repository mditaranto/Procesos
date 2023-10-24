from utils.functions import *

from flask import Blueprint, jsonify, request

ficheroProf = "Ejercicio2API/Ficheros/profesores.json"
ficheroAsig = "Ejercicio2API/Ficheros/asignatura.json"

profBP = Blueprint('prof', __name__)

def find_next_id():
    prof = leeFichero(ficheroProf)
    max = prof[0]["id"]
    for profe in prof:
        if profe["id"] > max:
            max = profe["id"]

    return max+1

@profBP.get('/')
def get_prof():
    prof = leeFichero(ficheroProf)
    return jsonify(prof)

@profBP.get("/<int:id>")
def get_prof(id):
    prof = leeFichero(ficheroProf)
    for profe in prof:
        if profe['id'] == id:
            return profe, 200
    return {"error": "Country not found"}, 404