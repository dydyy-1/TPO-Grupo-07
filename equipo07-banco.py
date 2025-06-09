import random

def busquedaSecuencialOrdenada(unaLista, item):
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
    return encontrado

def modificarTurno(lista_idsTurnos, lista_idsClientes):
    if len(lista_idsTurnos) == 0:
        print("No hay turnos registrados para modificar.")
        return

    print("\nTurnos existentes:")
    for i in range(len(lista_idsTurnos)):
        print(f"{i+1}. ID Turno: {lista_idsTurnos[i]}, Cliente: {lista_idsClientes[i]}, Estado: {estadosTurnos[i]}")
    
    pos = int(input("Seleccione el número del turno que desea modificar: ")) - 1
    while pos < 0 or pos >= len(lista_idsTurnos):
        print("Selección inválida.")
        pos = int(input("Seleccione el número del turno que desea modificar: ")) - 1
    
    print("Ingrese los nuevos datos para el turno:")
    nuevo_id = int(input("Nuevo ID del turno: "))
    
    while busquedaSecuencialOrdenada(lista_idsTurnos, nuevo_id):
        print("Error. El ID ya existe.")
        nuevo_id = int(input("Nuevo ID del turno: "))
        
    nuevo_cliente = int(input("Nuevo ID del cliente: "))
    while busquedaSecuencialOrdenada(lista_idsClientes, nuevo_cliente):
        print("Error. El ID ya existe.")
        nuevo_cliente = int(input("Nuevo ID del cliente: "))
    
    nuevo_estado = input("Nuevo estado del turno: \n 1. En proceso \n 2. Finalizado.")
    while nuevo_estado != 1 and nuevo_estado != 2:
        print("Error. Ingrese un estado válido.")
        nuevo_estado = input("Nuevo estado del turno: \n 1. En proceso \n 2. Finalizado.")

    # Modificación en listas paralelas
    lista_idsTurnos[pos] = nuevo_id
    lista_idsClientes[pos] = nuevo_cliente
    estadosTurnos[pos] = nuevo_estado

    print("Turno modificado con éxito.")


def verFinalizados(listaTramites,listaEstados):
    print("\n Lista de turnos finalizados: ")
    for i in range(len(listaTramites)):
        if listaEstados[i] == 2:
            print("ID del turno:", listaTramites[i])

def verActivos(listaTramites,listaEstados):
    print("\n Lista de turnos activos: ")
    for i in range(len(listaTramites)):
        if listaEstados[i] == 1:
            print("ID del turno:", listaTramites[i])

def generarTramite(listaTramites,listaEstados,lista_idsUsuarios):
    cont = 0
    cantidad = len(lista_idsUsuarios)
    #Generar ids de turnos:
    if cantidad == 0:
        print("Error. Hay 0 usuarios.")
        return
    while cont < cantidad:
            tramiteId = random.randint(1, 999)
            encontrado= busquedaSecuencialOrdenada(listaTramites, tramiteId)
            if encontrado == False:
                listaTramites.append(tramiteId)
                cont +=1
      
    for i in range(cantidad):
        turnosEstado=random.randint(1,2)
        listaEstados.append(turnosEstado)
        
    for i in range(cantidad):
        print("ID:", listaTramites[i])
        if listaEstados[i] == 1:
            print("Estado: En proceso")
        else:
            print("Estado: Finalizado")

def RegistrarUsuario(listaUsuarios, listaNombres):
    cantidad = int(input("Ingrese la cantidad de usuarios para registrar: "))
    cont = 0
    
    while cantidad <= 0:
        print("Error. La cantidad tiene que se mayor a 0.")
        cantidad = int(input("Ingrese la cantidad de usuarios para registrar: "))              

    while cont < cantidad:
        id = int(input("Ingrese el id del usuario a registrar (cuatro dígitos): "))
        while id < 1000 or id > 9999: #Validamos que sea de 4 dígitos
            id = int(input("Error. Ingrese el id del usuario a registrar (cuatro dígitos): "))
        
        while busquedaSecuencialOrdenada(listaUsuarios, id):
            print("Error. El ID ya existe.")
            id = int(input("Ingrese el id del usuario a registrar (cuatro dígitos): "))
        
        listaUsuarios.append(id)
        
        nombre=input("Ingrese su nombre y apellido: ")
        listaNombres.append(nombre)
        cont += 1
                           

def login(listaUsuarios, listaContrasenas, listaNombres):
    usuarioExiste = 0
    claveIncorrecta = 1

    while usuarioExiste == 0:
        preguntarUsuario = int(input("Ingrese su id de usuario: "))
        for i in range(len(listaUsuarios)):
            if preguntarUsuario == listaUsuarios[i]:
                usuarioExiste = 1
                indexUsuario = i
        if usuarioExiste == 0:
            print("Error. Usuario no existente.")

    while claveIncorrecta == 1:
        preguntarContrasenia = str(input("Ingrese su contraseña: "))
        if preguntarContrasenia == listaContrasenas[indexUsuario]:
            claveIncorrecta = 0
            print("Contraseña correcta. Bienvenido/a", listaNombres[indexUsuario], "!")
        else:
            print("Error. Contraseña incorrecta.")

def menuUsuarios():
    print("\n Abriendo menú de usuarios...")
    print("Menú de gestión de usuarios: \n 0. Volver al menú principal \n 1. Registrar usuario \n 2. Eliminar usuario \n 3. Modificar datos de un usuario \n 4. Buscar usuario. \n 5.Ver todos los usuarios.")
    opcionMenu = int(input("Ingrese el número correspondiente para acceder: ")) 
    while opcionMenu != 0:
        while opcionMenu != 0 and (opcionMenu < 1 or opcionMenu > 4): #Validación de la opción de Menú
            if opcionMenu != 0:
                print("\n Error. Seleccione una de las opciones siguientes.")
                print("Menú de gestión de usuarios: \n 0. Volver al menú principal \n 1. Registrar usuario \n 2. Eliminar usuario \n 3. Modificar datos de un usuario \n 4. Buscar usuario. \n 5.Ver todos los usuarios.")
                opcionMenu = int(input("Ingrese el número correspondiente para acceder: "))
        
        #Luego de validar opciones:
        if opcionMenu == 1:
            RegistrarUsuario(idClienteTurno,nombreUsuarios)
        elif opcionMenu == 2:
            print("")
        elif opcionMenu == 3:
            print("")
        elif opcionMenu == 4:
            print("")
        elif opcionMenu==5:
            print("")
        
        # Cuando se terminan las otras funciones:
        print("\n Abriendo menú de usuarios...")
        print("Menú de gestión de usuarios: \n 0. Volver al menú principal \n 1. Registrar usuario \n 2. Eliminar usuario \n 3. Modificar datos de un usuario \n 4. Buscar usuario. \n 5.Ver todos los usuarios.")
        opcionMenu = int(input("Ingrese el número correspondiente para acceder: "))
    
    print("Volviendo para atrás... \n")

def menuTurnos():
    print("\n Abriendo menú de turnos...")
    print("Menú de gestión de turnos: \n 0. Volver al menú principal \n 1. Registrar nuevo turno \n 2. Modificar datos del turno \n 3. Ver turnos activos \n 4. Ver turnos finalizados \n 5. Eliminar turno \n 6. Ver estadísticas.")
    opcionMenu = int(input("Ingrese el número correspondiente para acceder: ")) 
    while opcionMenu != 0:
        while opcionMenu != 0 and (opcionMenu < 1 or opcionMenu > 5): #Validación de la opción de Menú
            if opcionMenu != 0:
                print("\n Error. Seleccione una de las opciones siguientes.")
                print("Menú de gestión de turnos: \n 0. Volver al menú principal \n 1. Registrar nuevo turno \n 2. Modificar datos del turno \n 3. Ver turnos activos \n 4. Ver turnos finalizados \n 5. Eliminar turno \n 6. Ver estadísticas.")
                opcionMenu = int(input("Ingrese el número correspondiente para acceder: "))
        
        #Luego de validar opciones:
        if opcionMenu == 1:
            generarTramite(idTurnos,estadosTurnos,idClienteTurno)
        elif opcionMenu == 2:
            modificarTurno(idTurnos,idClienteTurno)
        elif opcionMenu == 3:
            verActivos(idTurnos,estadosTurnos)
        elif opcionMenu == 4:
            verFinalizados(idTurnos,estadosTurnos)
        elif opcionMenu == 5:
            print("")

        # Cuando se terminan las otras funciones:
        print("\n Abriendo menú de turnos...")
        print("Menú de gestión de turnos: \n 0. Volver al menú principal \n 1. Registrar nuevo turno \n 2. Modificar datos del turno \n 3. Ver turnos activos \n 4. Ver turnos finalizados \n 5. Eliminar turno \n 6. Ver estadísticas.")
        opcionMenu = int(input("Ingrese el número correspondiente para acceder: "))
    
    print("Volviendo para atrás... \n")

def menuInicio():
    print("\n Menu principal")
    print("Menú de opciones: \n 0. Finalizar programa. \n 1. Gestión de usuarios \n 2. Gestión de turnos.")
    opcionMenu = int(input("Ingrese el número correspondiente para acceder: ")) 
    while opcionMenu != 0:
        while opcionMenu != 0 and (opcionMenu < 1 or opcionMenu > 2): #Validación de la opción de Menú
            if opcionMenu != 0:
                print("\n Error. Seleccione una de las opciones siguientes.")
                print("Menú de opciones: \n 0. Finalizar programa. \n 1. Gestión de usuarios \n 2. Gestión de turnos.")
                opcionMenu = int(input("Ingrese el número correspondiente para acceder: "))
        
        #Luego de validar opciones:
        if opcionMenu == 1:
            menuUsuarios()
        elif opcionMenu == 2:
            menuTurnos()
        
        # Cuando se terminan las otras funciones:
        print("\n Menu principal")
        print(" Menú de opciones: \n 0. Finalizar programa. \n 1. Gestión de usuarios \n 2. Gestión de turnos.")
        opcionMenu = int(input("Ingrese el número correspondiente para acceder: "))
    
    print("Finalizando programa")

#Listas de usuarios:
idUsuarios=[-1]
nombreUsuarios=["Administrador"]
contrasenasUsuarios=["-1"]

#Listas de turnos
idTurnos=[]
idClienteTurno=[]
horaLlegada=[]
tipoTramite=[]
estadosTurnos=[]

login(idUsuarios, contrasenasUsuarios, nombreUsuarios)
menuInicio()