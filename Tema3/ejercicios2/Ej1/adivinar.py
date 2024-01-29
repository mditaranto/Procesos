import random
from threading import Thread, Lock

class adivinar(Thread):

    numero = random.randint(0, 100)
    numeroacertado = False
    bloqueo = Lock()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        while True:

            adivinar.bloqueo.acquire()
            if not adivinar.numeroacertado:
                adivinar.bloqueo.release()
                numeroaleatorio = random.randint(0, 100)
                if numeroaleatorio == adivinar.numero:
                    adivinar.bloqueo.acquire()
                    adivinar.numeroacertado = True
                    adivinar.bloqueo.release()
                    print(f"{self.name} ha acertado el numero {adivinar.numero}")
                    break
                else:
                    print(f"{self.name} ha dicho el numero {numeroaleatorio} y no ha acertado")
            else:
                print("Otro hilo ya ha acertado")
                break

            


