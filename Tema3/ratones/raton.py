from threading import Thread
import time

class Raton(Thread):
    def __init__(self, nombre, tiempoalimento):
        Thread.__init__(self, name=nombre)
        self.tiempoalimento = tiempoalimento 

    def run(self):
        print("Hilo", self.getName())
        print("El raton", self.name, "empieza a comer")
        time.sleep(self.tiempoalimento)
        print("El raton", self.name, "termina de comer")
