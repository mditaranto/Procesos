from threading import Thread


def imprimirMensaje(num):
    print("Soy el hilo", num)

if __name__ == '__main__':
    print("soy el hilo principal")

    for i in range(10):
        hilo = Thread(target=imprimirMensaje, args=(i,))
        hilo.start()