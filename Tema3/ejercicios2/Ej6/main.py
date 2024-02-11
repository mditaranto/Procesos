from filosofos import *

if __name__ == "__main__":
    lista = []
    for i in range(0,5):
        hilo = Filosofo (f'{i}')
        hilo.start()
        lista.append(hilo)

    for h in lista:
        h.join()