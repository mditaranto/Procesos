import random
from threading import Thread, Condition
import time

class Libro(Thread):
    libreria = [False, False, False, False, False, False, False, False, False]
    cond = Condition()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):
        while True:
            seleccionados = random.sample(range(9), 2)
            libro1 = seleccionados[0]
            libro2 = seleccionados[1]

            Libro.cond.acquire()

            while Libro.libreria[libro1] or Libro.libreria[libro2]:
                print("El  estudiante", self.name, "esta esperando los libros", libro1, libro2)
                Libro.cond.wait() 

            Libro.libreria[libro1] = True
            Libro.libreria[libro2] = True
            Libro.cond.release()

            print("El estudiante", self.name, "ha cogido los libros", libro1, libro2)
            time.sleep(random.randint(3,5))
            print("El estudiante", self.name, "ha termina de leer los libros", libro1, libro2)

            with Libro.cond:
                Libro.libreria[libro1] = False
                Libro.libreria[libro2] = False
                Libro.cond.notifyAll()
