from contador import *

for i in range(10):
    hilo = contadorThread(i)
    hilo.start()