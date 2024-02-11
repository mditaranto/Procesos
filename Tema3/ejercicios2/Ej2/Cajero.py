from threading import Thread, Semaphore
import random
import time

class Cajero(Thread):
    #Es un lock porque solo entra 1 hilo a la vez
    semafaro = Semaphore(1) #Esto esta mal, deberia ser un lock

    def __init__(self, num):
        Thread.__init__(self, name=num)

    def run(self):
        print("El hilo", self.name, "esta esperando a ser atendido")
        Cajero.semafaro.acquire()
        print("El hilo", self.name, "esta siendo atendido")
        time.sleep(random.randint(1, 5))
        print ("El hilo", self.name, "ha sido atendido")
        Cajero.semafaro.release()