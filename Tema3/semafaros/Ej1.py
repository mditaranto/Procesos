from threading import Thread, Semaphore
import random
import time

class Cajero(Thread):
    semafaro = Semaphore(4)

    def __init__(self, num):
        Thread.__init__(self, name=num)

    def run(self):
        print("El hilo", self.name, "esta comprando")
        Cajero.semafaro.acquire()   
        print("El hilo", self.name, "esta en caja")
        time.sleep(random.randint(1, 10))
        print ("El hilo", self.name, "ha terminado de comprar")
        Cajero.semafaro.release()