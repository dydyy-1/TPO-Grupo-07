import random

tramites = []
turnos=[]

def generarTramite(listaTramites,listaEstados):
    cantidad = int(input("Ingrese la cantidad de turnos para generar: "))
    #Generar ids de turnos:
    for i in range(cantidad):
        tramite_id = random.randint(1, 999)
        listaTramites.append(tramite_id)
    #Generar número de estado:
    for i in range(cantidad):
        turnosEstado=random.randint(1,2)
        listaEstados.append(turnosEstado)
        

    for i in range(cantidad):
        print("ID:", tramites[i])
        if turnos[i] == 1:
            print("Estado: En proceso")
        else:
            print("Estado: Finalizado")

generarTramite(tramites,turnos)