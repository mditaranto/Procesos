from threading import Thread

class contarVocales(Thread):
    def __init__(self, vocal):
        Thread.__init__(self)
        self.texto = "ejercicios/ej4/texto.txt"
        self.vocal = vocal  

    def run(self):
        vocales = 0
        with open(self.texto, "r", encoding="utf-8") as file:
            letras = file.read()
            vocales = letras.count(self.vocal)
        print(f"hay {vocales} vocales {self.vocal} en el texto")