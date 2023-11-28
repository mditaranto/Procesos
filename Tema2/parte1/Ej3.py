from multiprocessing import *
import time

def leer_archivo(cola):
    f = open('numeros.txt', 'r')
    for linea in f:
        numero = (linea)
        cola.put(numero)
    cola.put(None)
    
def sum_numbers(cola):
    total = 0
    numero = cola.get()
    while numero != None:
        numero = int(numero)
        total += numero
        numero = cola.get()
    print(f'La suma total es {total}')

if  __name__=="__main__":
    inicio = time.time()
    queue = Queue()
    p1 = Process(target=leer_archivo, args=(queue,))
    p2 = Process(target=sum_numbers, args=(queue,))

    p1.start()
    p2.start()
    fin = time.time()
    print(f'Tiempo de ejecución: {fin - inicio}')

