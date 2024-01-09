from multiprocessing import *
import random
import time

def proceso1(ruta):
    for i in range(1, 6):
        num = random.randint(1, 10)
        