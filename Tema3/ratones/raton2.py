from threading import Thread
import time

def comer(nombre, tiempoalimento):
    print("El raton", nombre, "empieza a comer")
    time.sleep(tiempoalimento)
    print("El raton", nombre, "termina de comer")

if __name__ == '__main__':
    print("soy el hilo principal")

    r1 = Thread(target=comer, args=("raton1", 2))
    r2 = Thread(target=comer, args=("raton2", 3))
    r3 = Thread(target=comer, args=("raton3", 1))

    r1.start()
    r2.start()
    r3.start()
