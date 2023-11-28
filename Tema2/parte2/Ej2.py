from multiprocessing import *
import random
import time

def proceso1(cola):
    ruta = ""
    for i in range(1, 10):
        ruta = (str)(random.randint(0, 255)) + "." + (str)(random.randint(0, 255)) + "." + (str)(random.randint(0, 255)) + "." + (str)(random.randint(0, 255))
        cola.put(ruta)
    cola.put(None)

def proceso2(cola, pipa):
    ruta = cola.get()
    while ruta is not None:
        rutadiv = ruta.split(".")
        if (int(rutadiv[0]) >= 223):
            print(f'La ruta {ruta} es clase D, no se enviara')
        else:
            pipa.send(ruta)
        ruta = cola.get()
    pipa.send(None)

def proceso3(pipa):
    ruta = pipa.recv()
    while ruta is not None:
        rutadiv = ruta.split(".")
        if (int(rutadiv[0]) <= 127):
            print(f'La ruta {ruta} es clase A')
        elif (int(rutadiv[0]) <= 191):
            print(f'La ruta {ruta} es clase B')
        elif (int(rutadiv[0]) <= 223):
            print(f'La ruta {ruta} es clase C')
        ruta = pipa.recv()

if __name__ == "__main__":
    inicio = time.time()
    cola = Queue()
    left, right = Pipe()

    p1 = Process(target=proceso1, args=(cola,))
    p2 = Process(target=proceso2, args=(cola, left,))
    p3 = Process(target=proceso3, args=(right,))

    p1.start()
    p2.start()
    p3.start()

    fin = time.time()
    print(f'Tiempo de ejecución: {fin - inicio}')