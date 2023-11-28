from multiprocessing import *
import time

def leer_archivo(cola):
    f = open('Ej7.txt', 'r')
    for linea in f:
        numero = linea.split()
        cola.send(numero)
    cola.send(None)

def suma(cola):
    numeros = cola.recv()
    while numeros is not None:
        total = 0
        numeros.sort()
        for i in range(int(numeros[1]), int(numeros[0])-1, -1):
            total += i
        print(f'La suma total es = {total}')
        numeros = cola.recv()


if __name__ == "__main__":
    inicio = time.time()
    left, right = Pipe()

    p1 = Process(target=leer_archivo, args=(left,))
    p2 = Process(target=suma, args=(right,))

    p1.start()
    p2.start()

    fin = time.time()
    print(f'Tiempo de ejecución: {fin - inicio}')


