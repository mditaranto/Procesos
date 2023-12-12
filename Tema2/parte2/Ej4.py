import random as rd
import multiprocessing as mp

def generar_notas(nombre_fichero) -> None:
    notas = [round(rd.uniform(1, 10), 2) for _ in range(6)]
    with open(nombre_fichero, 'w') as file:
        for nota in notas:
            file.write(f"{nota}\n")

def calcular_media(notas_fichero, nombre_alumno) -> None:
    notas = []
    with open(notas_fichero, 'r') as file:
        for line in file:
            notas.append(float(line))
    media = sum(notas) / len(notas)
    media_formatted = f"{media:.2f}"
    with open('out/medias.txt', 'a') as medias_file:
        medias_file.write(f"{media_formatted} {nombre_alumno}\n")

def encontrar_maxima() -> None:
    max_nota = -1
    alumno_max = ''
    with open('out/medias.txt', 'r') as medias_file:
        for line in medias_file:
            nota, alumno = line.split()
            nota = float(nota)
            if nota > max_nota:
                max_nota = nota
                alumno_max = alumno
    print(f"{max_nota} {alumno_max}")

if __name__ == "__main__":
    medias_file = open('out/medias.txt', 'w')
    medias_file.write('')
    medias_file.close()

    process_list1 = []
    process_list2 = []

    for x in range(10):
        proceso = mp.Process(target=generar_notas, args=(f"out/Alumno{x + 1}.txt",))
        proceso.start()
        process_list1.append(proceso)

    for x in range(10):
        proceso = mp.Process(target=calcular_media, args=(f"out/Alumno{x + 1}.txt", f"Alumno{x + 1}"))
        proceso.start()
        process_list2.append(proceso)

    for proceso in process_list1:
        proceso.join()

    for proceso in process_list2:
        proceso.join()

    proceso3 = mp.Process(target=encontrar_maxima).start()