from flask import Blueprint, jsonify

countriesBP = Blueprint("countries", __name__)

@countriesBP.get("/countries")
def get_countries(): 
    countries = leeFichero() 
    return jsonify(countries)

@countriesBP.get("/countries/int:id") 
def get_country(id): 
    countries = leeFichero() 
    for country in countries: 
        if country['id'] == id: 
            return country, 200
    return {"error": "Country not found"}, 404

