import random
import multiprocessing 

#En esta funcion se generan las temperaturas en ficheros txt dentro de una carpeta
def generar_temp(nombre_fichero) -> None:
    #Las temperaturas son random de 0 al 20 y se crean 24 con 2 decimales
    temperaturas = [round(random.uniform(0, 20), 2) for a in range(24)]
    with open(f"ejercicio1/diciembre/{nombre_fichero}", 'w') as file:
        for temp in temperaturas:
            #Se escriben en el fichero
            file.write(f"{temp}\n")

#En esta funcion se encuentra la temperatura maxima de los ficheros que guardan las temperaturas
def encontrar_maxima(nombre_fichero) -> None:
    #Se establece una temperatura maxima (Que es la minima posible)
    max_temp = 0
    with open(f'ejercicio1/diciembre/{nombre_fichero}.txt', 'r') as temp:
        #Se comprueba 1 por 1 y si es mayor que la actual, se actualiza la variable
        for line in temp:
            temperatura = float(line)
            if temperatura > max_temp:
                max_temp = temperatura
    #Luego se escribe la temperatura en el fichero
    with open('ejercicio1/diciembre/maximas.txt', 'w') as maximas:
        maximas.write(f"{nombre_fichero}:{max_temp}")

#En esta funcion se encuentra la temperatura minima de los ficheros que guardan las temperaturas
def encontrar_minima(nombre_fichero) -> None:
    #Se establece una temperatura minima (Que es la maxima posible)
    min_temp = 20
    with open(f'ejercicio1/diciembre/{nombre_fichero}.txt', 'r') as temp:
        #Se comprueba 1 por 1 y si es menor que la actual, se actualiza la variable
        for line in temp:
            temperatura = float(line)
            if temperatura < min_temp:
                min_temp = temperatura

    #Luego se escribe la temperatura en el fichero
    with open('ejercicio1/diciembre/minimas.txt', 'w') as minimas:
        minimas.write(f"{nombre_fichero}:{min_temp}")


if __name__ == "__main__":

    #El primer proceso se ejecuta 31 veces con la funcion generar_temp y se 
    # envia como parametro un string, la x que servira como los dias del mes
    for x in range (31):        
        proceso = multiprocessing.Process(target=generar_temp, args=(f"{x+1}-12.txt",))
        proceso.start()

    #El segundo y tercer proceso se ejecutan 31 veces con la funcion encontrar_minima y encontrar_maxima y se 
    # envia como parametro un string, la x que servira como los dias del mes
    for x in range (31):
        proceso2 = multiprocessing.Process(target=encontrar_minima, args=(f"{x+1}-12",))
        proceso3 = multiprocessing.Process(target=encontrar_maxima, args=(f"{x+1}-12",))
        proceso2.start()
        proceso3.start()


