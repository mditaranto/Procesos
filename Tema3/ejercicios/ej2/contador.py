from threading import Thread

class contadorThread(Thread):
    contador = 0

    def __init__(self, num):
        Thread.__init__(self, name=num)

    def run(self):
        while contadorThread.contador < 1000:
            contadorThread.contador += 1
            print(f"{self.name}: {contadorThread.contador}")

