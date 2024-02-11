from Carniceria import *

if __name__ == "__main__":
    lista = []
    for i in range(1,10):
        hilo = Carniceria(i)
        hilo.start()
        #Aqui no se para que sirve el join
        lista.append(hilo)
    hilo.join()

    for h in lista:
        h.join()