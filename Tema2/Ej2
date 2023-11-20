from multiprocessing import *
import time

def sum_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
    print(f'La suma total de 1 hasta {n}: {total}')

    return total

if __name__ == "__main__":
    inicio = time.time()
    pool = Pool(processes=3)
    numeros = [5,10,300]

    resultados = pool.map(sum_numbers, numeros)

    pool.close()
    fin = time.time()
    print(f'Tiempo de ejecución: {fin - inicio}')
    print(resultados)

