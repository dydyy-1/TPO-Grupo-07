import random
## VARIABLES GLOBALES
#Listas de usuarios:
idUsuarios=[-1]
nombreAdmin=["Administrador"]
contrasenaAdmin=["-1"]

#Listas de turnos
idTurnos=[] #ID DEL TURNO
nombreUsuarios=[]
idClienteTurno=[] #IDS DE USUARIOS
estadosTurnos=[]
tiposTurnos=[]
diasTurnos=[]
horaTurnos=[]


## FUNCIONES
def busquedaSecuencial_pos(unaLista, item):
    pos = 0
    while pos < len(unaLista):
        if unaLista[pos] == item:
            return True, pos
        pos += 1
    return False, -1

def ordenamientoSeleccion(lista):
    for i in range(len(lista)-1):
        for j in range (i+1,len(lista)):
            if lista[i] > lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux

def buscarUsuario(lista_idsUsuarios,listaNombres,lista_idsTurnos,listaEstados):
    if len(lista_idsTurnos) == 0 or len(lista_idsUsuarios)==0:
        print("\n Error. No hay turnos/usuarios registrados.")
        return

    id= int(input("Ingrese el ID del usuario para buscar: "))
    encontrado, pos = busquedaSecuencial_pos(lista_idsUsuarios,id)
    
    if encontrado:
            if len(lista_idsTurnos) != 0:
                if listaEstados[pos] == 1:
                    print(f"Datos del usuario: \n ID: {lista_idsUsuarios[pos]}, \n Nombre : {listaNombres[pos]}, \n ID del turno: {lista_idsTurnos[pos]} \n Estado del turno: En proceso. ")
                else:
                    print(f"Datos del usuario: \n ID: {lista_idsUsuarios[pos]}, \n Nombre : {listaNombres[pos]}, \n ID del turno: {lista_idsTurnos[pos]} \n Estado del turno: Finalizado ")
            else:
                print(f"Datos del usuario: \n ID: {lista_idsUsuarios[pos]}, \n Nombre : {listaNombres[pos]}, \n No se encontraron turnos registrados.")
    else:
        print("\n No se encontró el usuario. ")
        return


def eliminarUsuario(lista_idsTurnos, lista_idsClientes, listaEstados,listaNombres):
    if len(lista_idsTurnos) == 0 or len(lista_idsClientes)==0:
        print("\n Error. No hay turnos/usuarios registrados.")
        return

    print("\n Turnos existentes:")
    for i in range(len(lista_idsTurnos)):
        print(f"{i+1}. ID Turno: {lista_idsTurnos[i]}, Cliente: {lista_idsClientes[i]}, Estado: {listaEstados[i]}, Nombre: {listaNombres[i]}")
    
    pos = int(input("Seleccione el número del turno que desea eliminar: ")) - 1
    while pos <0 or pos>=len(lista_idsTurnos):
        print("Selección inválida.")
        pos = int(input("Seleccione el número del turno que desea eliminar: ")) - 1

    # Eliminación en paralelo
    lista_idsTurnos.pop(pos)
    lista_idsClientes.pop(pos)
    listaEstados.pop(pos)
    listaNombres.pop(pos)

    print("\n Turno eliminado con éxito.")

def mostrarUsuario(lista_idsUsuarios,lista_idsTurnos):
    if len(lista_idsUsuarios)==0:
        print("\n Error. No hay turnos/usuarios registrados.")
        return
    
    print("\n Mostrando usuarios...")
    if len(lista_idsTurnos)==0:
        for i in range(len(lista_idsUsuarios)):
            print(f"\n {i+1}. ID de Usuario: {lista_idsUsuarios[i]}, Nombre: {nombreUsuarios[i]}")
    else:
        for i in range(len(lista_idsUsuarios)):
            print(f"\n {i+1}. ID de Usuario: {lista_idsUsuarios[i]}, Nombre: {nombreUsuarios[i]}")
            print("--> ID del turno: ", idTurnos[i])
            
            print("--> Estado del turno: ", end="")
            if estadosTurnos[i]==1:
                print("En proceso.")
            else:
                print("Finalizado")
            
            print("--> Tipo de turno: ", end="")
            if tiposTurnos[i]==1:
                print("Caja.")
            elif tiposTurnos[i]==2:
                print("Préstamo.")
            else:
                print("Atención al cliente.")

            print("--> Día del turno: ", end="")
            if diasTurnos[i]==1:
                print("Lunes")
            elif diasTurnos[i]==2:
                print("Martes")
            elif diasTurnos[i]==3:
                print("Miércoles")
            elif diasTurnos[i]==4:
                print("Jueves")
            else:
                print("Día: Viernes")
            
            print("--> Hora del turno: ", horaTurnos[i], "hs")


def busquedaSecuencial(unaLista, item):
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

def modificarCliente(lista_idsClientes, listaNombres):
    if len(lista_idsClientes) == 0:
        print("\n Error. No hay clientes registrados para modificar.")
        return

    print("\n Clientes existentes:")
    for i in range(len(lista_idsClientes)):
        print(f"{i+1}. ID Cliente: {lista_idsClientes[i]}, Nombre: {listaNombres[i]} ")
    
    pos = int(input("Seleccione el número del cliente que desea modificar: ")) - 1
    while pos < 0 or pos >= len(lista_idsClientes):
        print("Selección inválida.")
        pos = int(input("Seleccione el número del cliente que desea modificar: ")) - 1
    
    print("Ingrese los nuevos datos para el cliente:")
    nuevo_id = int(input("Nuevo ID de cliente: "))
    
    while busquedaSecuencial(lista_idsClientes, nuevo_id):
        print("Error. El ID ya existe.")
        nuevo_id = int(input("Nuevo ID de cliente: "))
    
    nuevo_nombre= input("Ingrese el nuevo nombre del usuario: ")

    # Modificación en listas paralelas
    lista_idsClientes[pos] = nuevo_id
    listaNombres[pos]=nuevo_nombre

    print("\n Datos del cliente modificados con éxito.")

def modificarIDTurno(lista_idsTurnos,indiceLista):
    nuevo_id = int(input("Nuevo ID del turno: "))
    while busquedaSecuencial(lista_idsTurnos, nuevo_id):
        print("Error. El ID ya existe.")
        nuevo_id = int(input("Nuevo ID del turno: "))
    
    lista_idsTurnos[indiceLista] = nuevo_id
    print("ID modificado con éxito")

def modificarHoraTurno(listaHorasTurnos,indiceLista):
    print("Hora del turno actual: ",listaHorasTurnos[indiceLista], "hs")
    confirmar= int(input("¿Desea modificar la hora asociada? \n 1. Si \n 2. No: "))
    while confirmar != 1 and confirmar !=2:
        print("\n Error.")
        confirmar= int(input("¿Desea modificar la hora asociada? \n 1. Si \n 2. No: "))
    
    if confirmar == 2:
        return
    
    nueva_hora=int(input("Ingrese la nueva hora: (entre 7 y 18 hs): "))
    while nueva_hora < 7 or nueva_hora>18:
        print("\n Error")
        nueva_hora=int(input("Ingrese la nueva hora: (entre 7 y 18 hs): "))
    
    listaHorasTurnos[indiceLista]= nueva_hora
    print("Hora modificada con éxito")

def modificarDiaTurno(listaDiasTurnos,indiceLista):
    print("Día del turno actual:", end="")
    if listaDiasTurnos[indiceLista]==1:
        print("Lunes")
    elif listaDiasTurnos[indiceLista]==2:
        print("Martes")
    elif listaDiasTurnos[indiceLista]==3:
        print("Miércoles")
    elif listaDiasTurnos[indiceLista]==4:
        print("Jueves")
    else:
        print("Día: Viernes")
    
    confirmar= int(input("¿Desea modificar el día asociado? \n 1. Si \n 2. No: "))
    while confirmar != 1 and confirmar !=2:
        print("\n Error.")
        confirmar= int(input("¿Desea modificar el día asociado? \n 1. Si \n 2. No: "))
    
    if confirmar == 2:
        return
    
    nuevo_dia=int(input("Ingrese el nuevo día: \n 1. Lunes \n 2. Martes \n 3. Miércoles \n 4. Jueves \n 5. Viernes \n :"))
    while nuevo_dia < 1 or nuevo_dia>5:
        print("\n Error")
        nuevo_dia=int(input("Ingrese el nuevo día: \n 1. Lunes \n 2. Martes \n 3. Miércoles \n 4. Jueves \n 5. Viernes \n :"))
    
    listaDiasTurnos[indiceLista]= nuevo_dia
    print("Día modificado con éxito")

def modificarTipoTramite(listaTiposTurnos,indiceLista):
    print("Tipo de turno actual: ", end="")
    if listaTiposTurnos[indiceLista]==1:
        print("Caja.")
    elif listaTiposTurnos[indiceLista]==2:
        print("Préstamo.")
    else:
        print("Atención al cliente.")

    confirmar= int(input("¿Desea modificar la hora asociada? \n 1. Si \n 2. No: "))
    while confirmar != 1 and confirmar !=2:
        print("\n Error.")
        confirmar= int(input("¿Desea modificar la hora asociada? \n 1. Si \n 2. No: "))
    
    if confirmar == 2:
        return
    
    nuevo_tipo=int(input("Ingrese el nuevo tipo de trámite: \n 1. Caja \n 2. Préstamo \n 3. Atención al cliente: "))
    while nuevo_tipo < 1 or nuevo_tipo>3:
        print("\n Error")
        nuevo_tipo=int(input("Ingrese el nuevo tipo de trámite: \n 1. Caja \n 2. Préstamo \n 3. Atención al cliente: "))
    
    listaTiposTurnos[indiceLista]= nuevo_tipo
    print("Tipo de trámite modificado con éxito")

def modificarEstadoTurno(listaEstados,indiceLista):
    print("Estado de turno actual: ", end="")
    if listaEstados[indiceLista]==1:
        print("En proceso.")
    else:
        print("Finalizado.")

    confirmar= int(input("¿Desea modificar el estado de turno? \n 1. Si \n 2. No: "))
    while confirmar != 1 and confirmar !=2:
        print("\n Error.")
        confirmar= int(input("¿Desea modificar el estado de turno? \n 1. Si \n 2. No: "))
    
    if confirmar == 2:
        return
    
    nuevo_estado=int(input("Ingrese el estado de turno: \n 1. En proceso \n 2. Finalizado."))
    while nuevo_estado != 1 and nuevo_estado!=2:
        print("\n Error")
        nuevo_estado=int(input("Ingrese el estado de turno: \n 1. En proceso \n 2. Finalizado."))
    
    listaEstados[indiceLista]= nuevo_estado
    print("Estado de turno modificado con éxito")

def modificarTurno(lista_idsTurnos,lista_idsClientes):
    if len(lista_idsTurnos) == 0:
        print("\n No hay turnos registrados para modificar.")
        return

    continuar = 1
    while continuar == 1:
        print("\n Turnos existentes:")
        for i in range(len(lista_idsTurnos)):
            print(f"{i+1}. ID Turno: {lista_idsTurnos[i]}, Cliente: {lista_idsClientes[i]}")
        
        pos = int(input("Seleccione el número del turno que desea modificar: ")) - 1
        while pos < 0 or pos >= len(lista_idsTurnos):
            print("Selección inválida.")
            pos = int(input("Seleccione el número del turno que desea modificar: ")) - 1
        
        print("Cúal de los siguientes datos desea modificar? \n 1. ID de turno. \n 2. Hora del turno \n 3. Día del turno. \n 4. Tipo de trámite. \n 5. Estado del turno")
        opcion= int(input("Elija su opción: "))
        while opcion <1 or opcion >5:
            print("Error. Elija una de las siguientes: ")
            print("Cúal de los siguientes datos desea modificar? \n 1. ID de turno. \n 2. Hora del turno \n 3. Día del turno. \n 4. Tipo de trámite. \n 5. Estado del turno")
            opcion= int(input("Elija su opción: "))                
        
        if opcion == 1:
            modificarIDTurno(lista_idsTurnos,pos)
        elif opcion == 2:
            modificarHoraTurno(horaTurnos,pos)
        elif opcion == 3:
            modificarDiaTurno(diasTurnos,pos)
        elif opcion == 4:
            modificarTipoTramite(diasTurnos,pos)
        elif opcion == 5:
            modificarEstadoTurno(estadosTurnos,pos)

        continuar= int(input("¿Desea modificar otro dato? \n 1. Si \n 2. No: "))
        while continuar !=1 and continuar != 2:
            print("Error. Seleccione una de las siguientes opciones: ")
            continuar= int(input("¿Desea modificar otro dato? \n 1. Si \n 2. No: "))
        
    print("\n Turno modificado con éxito.")


def verFinalizados(listaTramites,listaEstados):
    if len(listaTramites) == 0:
        print("\n Error. No hay turnos registrados.")
        return
    
    existenTurnos= 0
    print("\n Lista de turnos finalizados: ")
    for i in range(len(listaTramites)):
        if listaEstados[i] == 2:
            print("ID del turno:", listaTramites[i])
            existenTurnos = 1
    if existenTurnos ==0:
        print("No se encontraron turnos finalizados.")

def verActivos(listaTramites,listaEstados):
    if len(listaTramites) == 0:
        print("Error. No hay turnos registrados.")
        return
    
    existenTurnos= 0
    print("\n Lista de turnos activos: ")
    for i in range(len(listaTramites)):
        if listaEstados[i] == 1:
            print("ID del turno:", listaTramites[i])
            existenTurnos = 1
    if existenTurnos ==0:
        print("\n No se encontraron turnos activos.")

def generarTipoTurno(listaTurnos, listaTipos):
    if len(listaTurnos) == 0:
        print("\n Error. No hay turnos registrados.")
        return

    for i in range(len(listaTurnos)):
        tipoTurno = random.randint(1, 3)
        listaTipos.append(tipoTurno)

def generarDiaTurno(listaTurnos, listaDias):
    if len(listaTurnos) == 0:
        print("\n Error. No hay turnos registrados.")
        return

    for i in range(len(listaTurnos)):
        turnoDia = random.randint(1, 5)
        listaDias.append(turnoDia)

def generarHoraTurno(listaTurnos,listaHoras):
    if len(listaTurnos) == 0:
        print("\n Error. No hay turnos registrados.")
        return
    
    for i in range(len(listaTurnos)):
        hora= random.randint(7,18)
        listaHoras.append(hora)

def generarTramite(listaTramites,listaEstados,lista_idsUsuarios):
    cont = 0
    cantidad = len(lista_idsUsuarios)
    #Generar ids de turnos:
    if cantidad == 0:
        print("Error. Hay 0 usuarios.")
        return
    while cont < cantidad:
            tramiteId = random.randint(1, 999)
            encontrado= busquedaSecuencial(listaTramites, tramiteId)
            if encontrado == False:
                listaTramites.append(tramiteId)
                cont +=1
    
    print("\n Ordenando lista...")
    print("Lista antes de ordenar:", listaTramites)
    ordenamientoSeleccion(listaTramites)
    print("Lista después de ordenar:", listaTramites)

    for i in range(cantidad):
        #Generamos el estado del turno:
        turnosEstado=random.randint(1,2)
        listaEstados.append(turnosEstado)
    
    generarTipoTurno(listaTramites, tiposTurnos)
    generarDiaTurno(listaTramites, diasTurnos)
    generarHoraTurno(listaTramites,horaTurnos)
    
    cont=0
    for i in range(cantidad):
        cont+=1
        print(f"\n {cont}. \n")
        print(f"ID del turno: {listaTramites[i]}")
        
        #Print estado:
        if listaEstados[i]== 1:
            print("Estado: En proceso.")
        else:
            print("Estado: Finalizado.")
        
        #Print tipo de trámite:
        if tiposTurnos[i]==1:
            print("Tipo de trámite: Caja.")
        elif tiposTurnos[i]==2:
            print("Tipo de trámite: Préstamo.")
        else:
            print("Tipo de trámite: Atención al cliente.")
        
        #Print del día
        if diasTurnos[i]==1:
            print("Día: Lunes")
        elif diasTurnos[i]==2:
            print("Día: Martes")
        elif diasTurnos[i]==3:
            print("Día: Miércoles")
        elif diasTurnos[i]==4:
            print("Día: Jueves")
        else:
            print("Día: Viernes")
        
        # Print de la hora:
        print("Hora del turno:", horaTurnos[i], "hs")

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
        
        while busquedaSecuencial(listaUsuarios, id):
            print("Error. El ID ya existe.")
            id = int(input("Ingrese el id del usuario a registrar (cuatro dígitos): "))
        
        listaUsuarios.append(id)
        
        nombre=input("Ingrese su nombre y apellido: ")
        listaNombres.append(nombre)
        cont += 1
                           

def login(listaUsuarios, listaContrasenas, nombreAdmin):
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
            print("Contraseña correcta. Bienvenido/a", nombreAdmin[indexUsuario], "!")
        else:
            print("Error. Contraseña incorrecta.")

def generarEstadisticas(lista_diasTurnos, lista_tiposTurnos):
    if len(lista_diasTurnos)==0:
        print("No hay turnos registrados.")
        return
    
    matrizTurnos=[[0,0,0]for i in range(5)]
    
    for i in range(len(lista_diasTurnos)):
        dia = lista_diasTurnos[i] - 1  # lunes=1 → índice 0
        tipo = lista_tiposTurnos[i] - 1  # tipo 1=caja → índice 0
        matrizTurnos[dia][tipo] += 1
    
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    tipos = ["Caja", "Préstamo", "Atención"]

    print(f"\n {'':15}", end="")
    for tipo in tipos:
        print(f"{tipo:^15}", end="")
    print()

    for i in range(5):
        print(f"{dias[i]:15}", end="")
        for j in range(3):
            print(f"{matrizTurnos[i][j]:15}", end="")
        print()


## PROGRAMA PRINCIPAL
def menuUsuarios():
    print("\n Abriendo menú de usuarios...")
    print("Menú de gestión de usuarios: \n 0. Volver al menú principal \n 1. Registrar usuario \n 2. Eliminar usuario \n 3. Modificar datos de un usuario \n 4. Buscar usuario. \n 5.Ver todos los usuarios.")
    opcionMenu = int(input("Ingrese el número correspondiente para acceder: ")) 
    while opcionMenu != 0:
        while opcionMenu != 0 and (opcionMenu < 1 or opcionMenu > 5): #Validación de la opción de Menú
            if opcionMenu != 0:
                print("\n Error. Seleccione una de las opciones siguientes.")
                print("Menú de gestión de usuarios: \n 0. Volver al menú principal \n 1. Registrar usuario \n 2. Eliminar usuario \n 3. Modificar datos de un usuario \n 4. Buscar usuario. \n 5.Ver todos los usuarios.")
                opcionMenu = int(input("Ingrese el número correspondiente para acceder: "))
        
        #Luego de validar opciones:
        if opcionMenu == 1:
            RegistrarUsuario(idClienteTurno,nombreUsuarios)
        elif opcionMenu == 2:
            eliminarUsuario(idTurnos,idClienteTurno,estadosTurnos,nombreUsuarios)
        elif opcionMenu == 3:
            modificarCliente(idClienteTurno, nombreUsuarios)
        elif opcionMenu == 4:
            buscarUsuario(idClienteTurno,nombreUsuarios,idTurnos,estadosTurnos)
        elif opcionMenu==5:
            mostrarUsuario(idClienteTurno,idTurnos)
        
        # Cuando se terminan las otras funciones:
        print("\n Abriendo menú de usuarios...")
        print("Menú de gestión de usuarios: \n 0. Volver al menú principal \n 1. Registrar usuario \n 2. Eliminar usuario \n 3. Modificar datos de un usuario \n 4. Buscar usuario. \n 5.Ver todos los usuarios.")
        opcionMenu = int(input("Ingrese el número correspondiente para acceder: "))
    
    print("Volviendo para atrás... \n")

def menuTurnos():
    print("\n Abriendo menú de turnos...")
    print("Menú de gestión de turnos: \n 0. Volver al menú principal \n 1. Registrar nuevo turno \n 2. Modificar datos del turno \n 3. Ver turnos activos \n 4. Ver turnos finalizados \n 5. Ver estadísticas.")
    opcionMenu = int(input("Ingrese el número correspondiente para acceder: ")) 
    while opcionMenu != 0:
        while opcionMenu != 0 and (opcionMenu < 1 or opcionMenu > 5): #Validación de la opción de Menú
            if opcionMenu != 0:
                print("\n Error. Seleccione una de las opciones siguientes.")
                print("Menú de gestión de turnos: \n 0. Volver al menú principal \n 1. Registrar nuevo turno \n 2. Modificar datos del turno \n 3. Ver turnos activos \n 4. Ver turnos finalizados \n 5. Ver estadísticas.")
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
            generarEstadisticas(diasTurnos, tiposTurnos)

        # Cuando se terminan las otras funciones:
        print("\n Abriendo menú de turnos...")
        print("Menú de gestión de turnos: \n 0. Volver al menú principal \n 1. Registrar nuevo turno \n 2. Modificar datos del turno \n 3. Ver turnos activos \n 4. Ver turnos finalizados \n 5. Ver estadísticas.")
        opcionMenu = int(input("Ingrese el número correspondiente para acceder: "))
    
    print("Volviendo para atrás... \n")

def menuInicio():
    print("\n Menu principal")
    print("Por favor, registre al menos un cliente y un turno antes de iniciar la ejecución del sistema.")
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


login(idUsuarios, contrasenaAdmin, nombreAdmin)
menuInicio()