from multiprocessing import *

import time

# Definir una función para sumar los números del 1 al n
def sum_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
    print(f'La suma total de 1 hasta {n}: {total}')

if __name__ == "__main__":
    # Obtener el tiempo de inicio
    inicio = time.time()

    # Crear un nuevo proceso y ejecutar la función sum_numbers con el argumento 5
    p1 = Process(target=sum_numbers, args=(5,))
    p1.start()

    # Obtener el tiempo de finalización
    fin = time.time()

    # Imprimir el tiempo de ejecución
    print(f'Tiempo de ejecución: {fin - inicio}')
    print(f'Tiempo de ejecución: {fin - inicio}')



