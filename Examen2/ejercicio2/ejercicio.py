from multiprocessing import *

#En esta funcion se busca por departamento a los empleados y se envia mediante Pipe a otro proceso
def buscar_departamento(tuberia, depart):
    with open(f"ejercicio2/salarios.txt", 'r') as file:
        #Recogemos la informacion del fichero
        for line in file.readlines():
            array = line.split(";")
            nombre = array[0]
            apellido = array[1]
            salario = array[2]
            deptmto = array[3].split()
            #Si el departamento es el mismo, se envia la informacion via Pipe
            if str(depart) == deptmto[0]:
                tuberia.send(f"{nombre};{apellido};{salario}")
        #Cuando no hay mas, se envia none
        tuberia.send(None)

#En esta funcion se busca a los empleados que tengan al menos el salario minimo y se envian mediante Pipe a otro proceso
def salario_minimo(tuberia, salarioMin, tuberia2):
    #Recoge la informacion enviada
    info = tuberia.recv()
    #Mientras, no sea none se ejecuta
    while (info is not None):
        salario = info.split(";")
        #Si el salario es mayor o igual, se envia la informacion via otro Pipe
        if salario[2] >= salarioMin :
            tuberia2.send(info)
        info = tuberia.recv()
    #Cuando no hay mas, se envia None
    tuberia2.send(None)

#En esta funcion se escriben los empleados ya filtrados en un fichero txt
def escribir_empleados(tuberia2):
    #recoge la informacion
    info = tuberia2.recv()
    with open(f'ejercicio2/empleados.txt', 'w') as file:
        #Mientras no sea none, se escribe en el fichero
        while (info is not None):
            nombre, apellido, salario = info.split(";")
            file.write(f"{apellido} {nombre}, {salario} \n")
            info = tuberia2.recv()
        tuberia2.close()

if __name__ == "__main__":
    #En este caso la tuberia es mas optima ya que envia datos de un punto a otro que es 
    # justo lo necesario
    tuberiaizq, tuberiader = Pipe()
    tuberia2izq, tuberia2der = Pipe()

    depart = input("Por favor introduzca un departamento: ")
    salarioMin = input("Por favor introduzca un salario minimo: ")

    #Se declaran el primer proceso que ejecuta la funcion buscar_departamento
    proceso1 = Process(target=buscar_departamento, args=(tuberiaizq, depart, ))
    #Se declaran el primer proceso que ejecuta la funcion salario_minimo
    proceso2 = Process(target=salario_minimo, args=(tuberiader, salarioMin, tuberia2izq, ))
    #Se declaran el primer proceso que ejecuta la funcion escribir_empleados
    proceso3 = Process(target=escribir_empleados, args=(tuberia2der, ))

    #Se ejecutan los procesos
    proceso1.start()
    proceso2.start()
    proceso3.start()