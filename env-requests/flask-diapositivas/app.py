from flask import *
import json

# Crea una nueva instancia de una aplicación Flask que se utilizará para manejar 
# solicitudes web y definir rutas, vistas y comportamientos específicos de la aplicación.
# __name__ variable especial en Python que se refiere al nombre del módulo en el que se encuentra el código.
app = Flask(__name__)

countries = [
    {
        "area": 513120,
        "capital": "Bangkok",
        "id": 1,
        "name": "Thailand"
    },
    {
        "area": 7617930,
        "capital": "Canberra",
        "id": 2,
        "name": "Australia"
    },
    {
        "area": 4000,
        "capital": "Londres",
        "name": "Inglaterra",
        "id": 4
    },
    {
        "area": 12654789,
        "capital": "London",
        "name": "United Kingdom",
        "id": 5
    }
]

def leeFichero():
    archivo = open("database.json", "r")
    countries = json.load(archivo)
    archivo.close()
    return countries

def escribeFichero(countries):
    archivo = open("database.json", "w")
    json.dump(countries, archivo)
    archivo.close()

# Función que calcula el siguiente id. Coge el máximo id que encuentra
# en la lista y le suma 1
def find_next_id():
    #countries = leeFichero()
    max = countries[0]["id"]
    for country in countries:
        if country["id"] > max:
            max = country["id"]

    return max+1

# @app hace referencia al objeto de tipo Flask creado al inicio
@app.get("/countries/") 
# Dentro de los paréntesis indicamos la ruta que se usará para hacer la petición
# Al escribir esa ruta en el navegador se ejecutará la siguiente función
def get_countries():
    countries = leeFichero()
    # jsonify convierte en formato json la lista que hemos definido
    # como base de datos
    return countries


# A la dirección de countries se le añade la posibilidad
# de indicar un id que será el id del país a mostrar
@app.get("/countries/<int:id>")
# Parámetro de entrada el id 
def get_country(id):
    countries = leeFichero()
    # Buscamos el id del país
    for country in countries:
        if country['id'] == id:
            return country, 200
    # Si no se encuentra, mensaje de error y 404
    return {"error": "Country not found"}, 404


# En este caso indicamos que la petición es de tipo POST
@app.post("/countries")
# definimos la función correspondiente
def add_country():
    countries = leeFichero()
    # Comprobamos si la petición cumple con el formato json
    if request.is_json:
        # Guardamos el formato JSON
        country = request.get_json()
        # Le asignamos un nuevo id
        country["id"] = find_next_id()
        # Añadimos el nuevo país a nuestra lista
        countries.append(country)
        escribeFichero(countries)
        # Devolvemos el país en formato diccionario y 201
        return country, 201
    # Si la petición no cumple con el formato JSON
    return {"error": "Request must be JSON"}, 415

# En este caso indicamos que la petición es de tipo PUT
# Como tenemos que modificar un país concreto, en la dirección de la petición se tendrá que
# indicar el id del país a modificar
@app.put("/countries/<int:id>")
@app.patch("/countries/<int:id>")
# definimos la función correspondiente
def modify_country(id):
    countries = leeFichero()
    # Se comprueba si la petición que nos ha llegado cumple con el formato json
    if request.is_json:
        # Creamos una variable donde guardamos el formato JSON, que coincide con un diccionario
        newCountry = request.get_json()
        # Tenemos que coger de nuestra lista de países, el país concreto a modificar, para lo cual
        # habrá que buscarlo por su id
        for country in countries:
            if country["id"] == id:
                # Modificamos todos los atributos del país con los nuevos valores indicados en el json
                for element in newCountry:
                    country[element] = newCountry[element]
                escribeFichero(countries)
                # Devolvemos el país en formato diccionario y el código 200 para indicar que se ha modificado
                return country, 200
    # Si la petición no cumple con el formato JSON devuelve un mensaje de error y el código 415
    return {"error": "Request must be JSON"}, 415

# A la dirección de countries se le añade la posibilidad
# de indicar un id que será el id del país a eliminar
@app.delete("/countries/<int:id>")
# Se debe añadir como parámetro de entrada el id que se 
# indica en la dirección
def delete_country(id):
    countries = leeFichero()
    # Como hay que eliminar un país concreto, tendremos que buscar 
    # en la lista el id del país que se ha indicado en la petición
    for country in countries:
        if country['id'] == id:
            countries.remove(country)
            escribeFichero(countries)
            # Si se encuentra el país, se devuelve el país ya vacío más el código 200
            return {}, 200
    # Si no se encuentra, se devuelve mensaje de error y código 404
    return {"error": "Country not found"}, 404

if __name__=='__main__':  
    # por defecto usará la ip 0.0.0.0 y el puerto 5000
    # Esto implica que nuestra página web puede ser accesible desde otro ordenador
    # Al ponerlo en modo debug si se produce un error nos mostrará información relevante
    app.run(debug=True, host='0.0.0.0', port=5050)
