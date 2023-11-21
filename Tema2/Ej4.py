from multiprocessing import *
import time

def leer_archivo(cola):
    f = open('numeros.txt', 'r')
    for linea in f:
        numero = (linea)
        cola.send(numero)
    cola.send(None)
    cola.close()
    
def sum_numbers(cola):
    total = 0
    numero = cola.recv()
    while numero != None:
        numero = int(numero)
        total += numero
        numero = cola.recv()
    print(f'La suma total es {total}')

if  __name__=="__main__":
    inicio = time.time()
    left, right = Pipe()
    p1 = Process(target=leer_archivo, args=(left,))
    p2 = Process(target=sum_numbers, args=(right,))

    p1.start()
    p2.start()
    fin = time.time()
    print(f'Tiempo de ejecución: {fin - inicio}')

