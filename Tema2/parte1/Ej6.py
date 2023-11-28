from multiprocessing import *
import time

def calcular_mayor(num1, num2):
    if num1 > num2:
            return(num1, num2)
    else: 
        return(num2, num1)


def suma(num1, num2):
    total = 0
    for i in range(num1, num2-1, -1):
        total+=i
    print(f'La suma total es = {total}')


if __name__ == "__main__":
    inicio = time.time()
    pool = Pool(processes=3)
    numeros = [(10,5), (5,10), (100, 200)]
   
    resultados = pool.starmap(calcular_mayor, numeros)
    resultados2 = pool.starmap(suma, resultados)

    pool.close()
    fin = time.time()
    print(f'Tiempo de ejecución: {fin - inicio}')


