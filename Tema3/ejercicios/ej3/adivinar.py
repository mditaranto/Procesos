import random
from threading import Thread

class adivinar(Thread):

    numero = random.randint(0, 100)
    numeroacertado = False

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        while not adivinar.numeroacertado:
            numeroaleatorio = random.randint(0, 100)

            if numeroaleatorio == adivinar.numero:
                adivinar.numeroacertado = True
                print(f"{self.name} ha acertado el numero {adivinar.numero}")
                break
            else:
                print(f"{self.name} ha dicho el numero {numeroaleatorio} y no ha acertado")



