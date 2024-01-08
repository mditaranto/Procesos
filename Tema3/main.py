from sisoi import Sisoi


print("soy el hilo principal")

for i in range(10):
    hilo = Sisoi(i)
    hilo.start()
    