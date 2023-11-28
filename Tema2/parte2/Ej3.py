from multiprocessing import*
import random
import time

def funcion1(rutaFichero):
    fichero = open(rutaFichero, "w")
    for i in range(6):
        fichero.write(str(random.randint(1, 10)) + "\n"  )
    fichero.close()

def funcion2(nombreAlumno, rutaFichero):
    fichero = open(rutaFichero, "r")
    ficheroMedias = open("medias.txt", "w")
    suma = 0
    for i in fichero:
        suma += int(i)
        media = suma / 6
        ficheroMedias.write(nombreAlumno + " " + str(media) + " " + "\n")
    fichero.close()
    ficheroMedias.close()

def funcion3(rutaFichero):
    fichero = open(rutaFichero, "r")
    mayor = ["", 0]
    for i in fichero:
        alumno = i.split(" ")
        if int(alumno[1]) > mayor[1]:
            mayor[0] = alumno[0]
            mayor[1] = int(alumno[1])
    fichero.close()
    print("El alumno con mayor media es " + mayor[0] + " con una media de " + mayor[1] + "\n")


if __name__ == "__main__":
    rutas = []
    for i in range(10):
        ruta = "parte2/Alumnos/alumno" + str(i) + ".txt"
        rutas += [("Alumno"+str(i) ,ruta)]
        funcion1(ruta)
    pool = Pool(processes=10)
    pool.starmap(funcion2, rutas)

    p3 = Process(target=funcion3, args=("medias.txt",))
    p3.start()
