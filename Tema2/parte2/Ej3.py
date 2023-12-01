from multiprocessing import*
import random
import time

def generar_notas(rutaFichero):
    with open(rutaFichero, "w") as fichero:
        for _ in range(6):
            nota = round(random.uniform(1, 10), 2)  # Generar número aleatorio con decimales
            fichero.write(f"{nota}\n")

def calcular_media(nombreAlumno, rutaFichero):
    with open(rutaFichero, "r") as fichero:
        notas = fichero.readlines()
        notas = [float(nota.strip()) for nota in notas]  # Convertir a números y eliminar saltos de línea
        media = round(sum(notas) / len(notas), 2) if notas else 0.0  # Calcular la media o asignar 0 si no hay notas
        with open("parte2\Alumnos\medias.txt", "w") as ficheroMedias:
            ficheroMedias.write(f"{nombreAlumno} {media}\n")

def obtener_maxima():
    with open("medias.txt", "r") as fichero:
        max_nota = 0
        max_alumno = ""
        for linea in fichero:
            nota, alumno = linea.split()
            nota = float(nota)
            if nota > max_nota:
                max_nota = nota
                max_alumno = alumno
        print(f"La nota máxima es {max_nota} obtenida por el alumno {max_alumno}")

if __name__ == "__main__":
    rutas = []
    
    # Proceso 1: Generar notas para 10 alumnos
    for i in range(10):
        ruta = f"parte2\Alumnos\Alumno{i + 1}.txt"
        rutas.append((f"Alumno{i + 1}", ruta))
        generar_notas(ruta)
    
    # Proceso 2: Calcular la media para cada alumno
    with Pool(processes=10) as pool:
        pool.starmap(calcular_media, rutas)
    
    # Proceso 3: Obtener la nota máxima
    obtener_maxima()
