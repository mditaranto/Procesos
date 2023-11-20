from multiprocessing import Process, Pipe

def procceso1(conn):
    conn.send("Hola desde el proceso 1")
    conn.close()

def proccess2(conn):
    mensaje = conn.recv()
    print("mensaje recibido: ", mensaje)
    conn.close()

if __name__ == "__main__":
    left, right = Pipe()
    p1 = Process(target=procceso1, args=(left,))
    p2 = Process(target=proccess2, args=(right,))

    p1.start()
    p2.start()