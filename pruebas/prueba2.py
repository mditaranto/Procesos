from multiprocessing import Process
import time
def hello(name):
    print("hello world", name)

def suma(num1, num2):
    res = num1 + num2
    print("suma igual a", res)


if __name__ == "__main__":
    inicio = time.time()
    p1 = Process(target=suma, args=(3,5))
    p1.start()

p1.join()
fin = time.time()
print("Tiempo:", fin - inicio)