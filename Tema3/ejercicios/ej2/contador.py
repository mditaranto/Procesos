from threading import Thread

class contadorThread(Thread):
    contador = 0

    def __init__(self, num):
        Thread.__init__(self, name=num)

    def run(self):
        if (self.contador >= 1000):
            self.contador += 1
            print(f"{self.name}: {self.contador}")

if (__name__ == '__main__'):
    # 10 Thread

    for x in range(10):
        hilo = contadorThread(x)
        hilo.start()