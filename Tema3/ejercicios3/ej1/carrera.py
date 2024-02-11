from threading import *
import random
import time

class Carrera(Thread):
    barrera = Barrier(10)
    bloqueo = Lock()
    cuenta = False

    def __init__(self, name):
        Thread.__init__(self, name=name)
        self.empieza = 0.0
        self.termina = 0.0

    def run(self):

        print(self.name, "esperando a que todos los hilos esten listos")
        Carrera.barrera.wait()

        if not Carrera.cuenta :
            with Carrera.bloqueo:
                Carrera.cuenta = True
                for i in range(3, 0, -1):
                    print(i, "...")
                    time.sleep(1)
                print("YA!")

        self.empieza = time.time()
        time.sleep(random.randint(1, 10))
        self.termina = time.time()
        print(self.name, "ha terminado en", self.termina - self.empieza, "segundos")

