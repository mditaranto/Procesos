from multiprocessing import *
import time

def calcular_mayor(num1, num2, cola):
    if num1 > num2:
            cola.send(num1)
            cola.send(num2)
            cola.send(None)
    else: 
        cola.send(num2)
        cola.send(num1)
        cola.send(None)


def suma(cola):
    numeros = cola.recv()
    total = 0
    while numeros is not None:
        total+=numeros
        numeros = cola.recv()
    print(f'La suma total es = {total}')


if __name__ == "__main__":
    inicio = time.time()
    
    left, right = Pipe()
    p1 = Process(target=calcular_mayor, args=(10, 5, left))
    p2 = Process(target=suma, args=(right,))

    p1.start()
    p2.start()

    fin = time.time()
    print(f'Tiempo de ejecución: {fin - inicio}')



