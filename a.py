def busquedaSecuencial_pos(unaLista, item):
    pos = 0
    encontrado = False
    parar = False
    while pos < len(unaLista) and not encontrado and not parar:
        if unaLista[pos] == item:
            encontrado = True
        else:
            if unaLista[pos] > item:
                parar = True
            else:
                pos = pos+1
    return encontrado,pos


def buscarUsuario(lista_idsUsuarios,listaNombres,lista_idsTurnos,listaEstados):
    buscar = int(input("Buscar usuario con: \n 1. ID \n 2. Nombre: "))
    while buscar != 1 and buscar !=2:
        print("Error. Seleccione una de las siguientes: ")
        buscar = int(input("Buscar usuario con: \n 1. ID \n 2. Nombre: "))
    
    if buscar == 1:
        id= int(input("Ingrese el ID del usuario para buscar: "))
        encontrado, pos = busquedaSecuencial_pos(lista_idsUsuarios,id)
        
    else:
        nombre= input("Ingrese el ID del usuario para buscar: ")
        encontrado, pos = busquedaSecuencial_pos(listaNombres,nombre)
    
    if encontrado:
            if len(lista_idsTurnos) != 0:
                if listaEstados[pos] == 1:
                    print(f"Datos del usuario: \n ID: {lista_idsUsuarios[pos]}, \n Nombre : {listaNombres[pos]}, \n ID del turno: {lista_idsTurnos[pos]} \n Estado del turno: En proceso. ")
                else:
                    print(f"Datos del usuario: \n ID: {lista_idsUsuarios[pos]}, \n Nombre : {listaNombres[pos]}, \n ID del turno: {lista_idsTurnos[pos]} \n Estado del turno: Finalizado ")
            else:
                print(f"Datos del usuario: \n ID: {lista_idsUsuarios[pos]}, \n Nombre : {listaNombres[pos]}, \n No se encontraron turnos registrados.")
    else:
        print("No se encontró el usuario. ")
        return