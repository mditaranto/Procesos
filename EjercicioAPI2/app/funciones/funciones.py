import string
from flask import *
import random

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
    
# Contraseña aleatoria
def randomPass():
    chars = string.ascii_letters
    password = ""
    
    for a in range(10):
        password += random.choice(chars)
        
    return(password)