from Ej1 import *

if __name__ == "__main__":
    lista = []
    for i in range(10):
        hilo = Cajero(i)
        hilo.start()
        lista.append(hilo)
    hilo.join()

    for h in lista:
        h.join()