from libros import *

if __name__ == "__main__":
    lista = []
    for i in range(1,5):
        hilo = Libro(i)
        hilo.start()
        lista.append(hilo)
    hilo.join()

    for h in lista:
        h.join()