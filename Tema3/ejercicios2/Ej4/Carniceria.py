from threading import Thread, Semaphore
import random
import time

class Carniceria(Thread):
    carniceria = Semaphore(4)
    charcuteria = Semaphore(2)

    def __init__(self, num):
        Thread.__init__(self, name=num)
        self.carne = False
        self.embutido = False

    def run(self):
        while not self.carne or not self.embutido:
            if (Carniceria.carniceria.acquire(blocking = False) and not self.carniceria):
                with Carniceria.carniceria:
                    print("El cliente", self.name, "esta siendo atendido")
                    time.sleep(random.randint(1, 10))
                    print ("El cliente", self.name, "ha terminado en la carniceria")
                    self.carne = True
               
            if (Carniceria.charcuteria.acquire(blocking = False) and not self.charcuteria):
                with Carniceria.charcuteria:
                    print("El cliente", self.name, "esta siendo atendido")
                    time.sleep(random.randint(1, 10))
                    print ("El cliente", self.name, "ha terminado en la charcuteria")
                    self.embutido = True
            

