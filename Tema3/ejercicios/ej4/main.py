from contarVocales import *

if __name__ == "__main__":
    vocales = ["a", "e", "i", "o", "u"]
    threads = []
    for vocal in vocales:
        thread = contarVocales(vocal)
        thread.start()
