from flask import *

# Leemos el fichero json
def leerFichero(nombreFichero):
    archivo = open(nombreFichero, "r")
    data = json.load(archivo)
    archivo.close()
    return data

# Escribimos en el fichero json
def escribeFichero(nombreFichero,data):
    archivo = open(nombreFichero, "w")
    json.dump(data, archivo)
    archivo.close()