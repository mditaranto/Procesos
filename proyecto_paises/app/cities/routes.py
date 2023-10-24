from flask import Blueprint, jsonify

rutaFichero = "proyecto_paises\app\cities.json"
citiesBP = Blueprint("cities", __name__)

@citiesBP.get("/cities")
def get_cities(): 
    cities = leeFichero() 
    return jsonify(cities)

@citiesBP.get("/cities/int:id") 
def get_city(id): 
    cities = leeFichero() 
    for city in cities: 
        if cities['id'] == id: 
            return city, 200 
    return {"error": "city not found"}, 404

