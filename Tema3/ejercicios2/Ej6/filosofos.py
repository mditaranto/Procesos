import random
from threading import Thread, Condition
import time

class Filosofo(Thread):
    palito = [False, False, False, False, False]
    cond = Condition()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        while True:

            print("El filosofo", self.name, "esta pensando")
            time.sleep(random.randint(1, 5))
        
            Filosofo.cond.acquire() #Aqui puede ir un with y no hace falta el release
            while Filosofo.palito[int(self.name)]:
                print("El filosofo", self.name, "esta esperando los palitos", self.name)
                Filosofo.cond.wait()
                
            print("El filosofo", self.name, "ha cogido el palito izq")
            Filosofo.palito[int(self.name)] = True

            while Filosofo.palito[(int(self.name)+1)%5]:
                print(f"El filósofo {self.name} está esperando los palitos {str(int(self.name) + 1)}")
                Filosofo.cond.wait()

            print("El filosofo", self.name, "ha cogido el palito der")
            Filosofo.palito[(int(self.name)+1)%5] = True
            Filosofo.cond.release()

            print("El filosofo", self.name, "esta comiendo")
            time.sleep(random.randint(1, 5))
            print("El filosofo", self.name, "ha terminado de comer")

            with Filosofo.cond:
                Filosofo.palito[int(self.name)] = False
                Filosofo.palito[(int(self.name)+1)%5] = False
                Filosofo.cond.notifyAll()

