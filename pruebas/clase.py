from multiprocessing import Process
import time


def menor(num1, num2):
    sumaTotal = 0
    for num in range(num1, num2+1):
        sumaTotal = sumaTotal + num
    print(sumaTotal)

if __name__ == "__main__":
    inicio = time.time()
    
    p1 = Process(target=suma, args=(3,5))