from multiprocessing import *
import time

def leer_archivo(cola):
    f = open('Ej7.txt', 'r')
    for linea in f:
        numero = linea.split()
        cola.put(numero)
    cola.put(None)

def suma(cola):
    numeros = cola.get()
    while numeros is not None:
        total = 0
        numeros.sort()
        for i in range(int(numeros[1]), int(numeros[0])-1, -1):
            total += i
        print(f'La suma total es = {total}')
        numeros = cola.get()


if __name__ == "__main__":
    inicio = time.time()
    queue = Queue()

    p1 = Process(target=leer_archivo, args=(queue,))
    p2 = Process(target=suma, args=(queue,))

    p1.start()
    p2.start()

    fin = time.time()
    print(f'Tiempo de ejecución: {fin - inicio}')


