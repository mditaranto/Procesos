import random
from threading import Thread
import time

class Trabajo(Thread):
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        self.tiempo = random.randint(1, 10)

    def run(self):
        print("Soy", self.name, "y estoy trabajando")
        time.sleep(self.tiempo)
        print("Soy", self.name, "y termine de trabajar")