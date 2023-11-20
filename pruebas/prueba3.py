from multiprocessing import Pool
import time


def doble(num):
    return 2*num

def suma(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    inicio = time.time()
    pool = Pool(processes=6)
    numeros = [(1,2),(3,4),(5,6),(7,8)]

    resultados = pool.starmap(suma, numeros)

    pool.close
    fin = time.time()
    print(fin - inicio)
    print(resultados)
