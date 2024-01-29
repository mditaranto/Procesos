from threading import Thread, Semaphore
import random
import time

class Carniceria(Thread):
    carniceria = Semaphore(4) 

    def __init__(self, num):
        Thread.__init__(self, name=num)


    def run(self):
        Carniceria.carniceria.acquire()
        print("El cliente", self.name, "esta siendo atendido")
        time.sleep(random.randint(1, 10))
        print ("El cliente", self.name, "ha terminado en la carniceria")
        Carniceria.carniceria.release()

