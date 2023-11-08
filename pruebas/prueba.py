from multiprocessing import *

def hello(name):
    print("Hello world", name)

if __name__ == "__main__":
    p = Process(target=hello, args=("Elena",))
    p.start
    p.join()
    print("Fin main")