from threading import Thread
import time

class Raton(Thread):
    def __init__(self, nombre, tiempoComer):
        Thread.__init__(self)
        self.nombre = nombre
        self.tiempoComer = tiempoComer

    def run(self):
        print("El raton", self.nombre, "empieza a comer")
        time.sleep(self.tiempoComer) #Simula el tiempo de alimentacion del raton
        print("El ratón", self.nombre, "ha terminado de comer")