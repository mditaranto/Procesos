from utils.functions import *

from flask import Blueprint, jsonify

rutaFichero = "Ejercicio2API/Ficheros/asignatura.json"
asigBP = Blueprint("asig", __name__)

@asigBP.get('/')
def get_asig():
    asig = leeFichero(rutaFichero)
    return jsonify(asig)

@asigBP.get("/<int:id>")
def get_asig(id):
    asig = leeFichero(rutaFichero)
    for asigna in asig:
        if asigna['id'] == id:
            return asigna, 200
    return {"error": "City not found"}, 404

