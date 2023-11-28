from multiprocessing import *
import time

def contar_vocal(vocal):
    numVocal = 0
    with open('parte2/letras.txt', 'r') as f:
        letras = f.read()
        numVocal = letras.count(vocal)
    return numVocal
 

if __name__=="__main__":
    inicio = time.time()
    pool = Pool(processes=5)
    letras = ['a','e','i','o','u']
    
    resultados = pool.map(contar_vocal, letras)
    print (resultados)
    fin = time.time()
    print(f'Tiempo de ejecución: {fin - inicio}')
   