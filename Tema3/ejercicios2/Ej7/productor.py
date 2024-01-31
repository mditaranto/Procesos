import random
from threading import Thread
import time

from main import cond, cola

class Productor(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        while True:
            cadena = "objeto"
            with cond:
                while cola.full():
                    print("Cola llena")
                    cond.wait()
                cola.put(cadena)

            print("hilo", self.name, "produciendo...")
            time.sleep(random.randint(1, 5))
            print("Hilo", self.name, "ha terminado de producir")
            cond.notifyAll()

        