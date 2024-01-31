import random
from threading import Thread
import time
from main import cond, cola

class consumidor(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        while True:
            with cond:
                while cola.empty():
                    print("Cola vacia")
                    cond.wait()
                cadena = cola.get()
            print("Hilo", self.name, "es esta cogiendo el objeto...")
            time.sleep(random.randint(1, 5))
            print("Objeto cogido: ",cadena)
            

