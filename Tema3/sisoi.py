from threading import Thread

class Sisoi(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        print("Soy el hilo", self.num)