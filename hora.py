import random

def modificarTurno(lista_idsTurnos,lista_idsClientes, listaEstados):
    if len(lista_idsTurnos) == 0:
        print("\n No hay turnos registrados para modificar.")
        return

    print("\n Turnos existentes:")
    for i in range(len(lista_idsTurnos)):
        if listaEstados[i]== 1:
            print(f"{i+1}. ID Turno: {lista_idsTurnos[i]}, Cliente: {lista_idsClientes[i]}, Estado: En proceso.")
        else:
            print(f"{i+1}. ID Turno: {lista_idsTurnos[i]}, Cliente: {lista_idsClientes[i]}, Estado: Finalizado.")
    
    pos = int(input("Seleccione el número del turno que desea modificar: ")) - 1
    while pos < 0 or pos >= len(lista_idsTurnos):
        print("Selección inválida.")
        pos = int(input("Seleccione el número del turno que desea modificar: ")) - 1
    
    opcion= int(input("Cúal de los siguientes datos desea modificar?"
    print("Ingrese los nuevos datos para el turno:")
    nuevo_id = int(input("Nuevo ID del turno: "))
    
    while busquedaSecuencial(lista_idsTurnos, nuevo_id):
        print("Error. El ID ya existe.")
        nuevo_id = int(input("Nuevo ID del turno: "))
        
    
    nuevo_estado = int(input("Nuevo estado del turno: \n1. En proceso \n2. Finalizado.\n"))
    while nuevo_estado != 1 and nuevo_estado != 2:
        print("Error. Ingrese un estado válido.")
        nuevo_estado = input("Nuevo estado del turno: \n1. En proceso \n2. Finalizado.\n")

    # Modificación en listas paralelas
    lista_idsTurnos[pos] = nuevo_id
    if nuevo_estado == 1:
        listaEstados[pos] = "En proceso"
    else:
        listaEstados[pos] = "Finalizado"

    print("\n Turno modificado con éxito.")