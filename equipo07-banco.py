import random

def RegistrarUsuario(listaUsuarios, listaContrasenas, listaNombres):
    cantidad = int(input("Ingrese la cantidad de usuarios para registrar: "))
    cont = 0
    
    while cantidad <= 0:
        print("Error. La cantidad tiene que se mayor a 0.")
        cantidad = int(input("Ingrese la cantidad de usuarios para registrar: "))              

    while cont < cantidad:
        id = int(input("Ingrese el id del usuario a registrar (cuatro dígitos): "))
        while id < 1000 or id > 9999: #Validamos que sea de 4 dígitos
            id = int(input("Error. Ingrese el id del usuario a registrar (cuatro dígitos): "))
        
        listaUsuarios.append(id)
        contrasena = str(input("Ingrese la contraseña del usuario a registrar (mínimo 5 caracteres): "))
        
        #Validación contraseña:
        while len(contrasena) < 5: #Validamos que tenga 5 dígitos
            contrasena = str(input("Error. Ingrese la contraseña del usuario a registrar: (mínimo 5 caracteres): "))
        
        nombre=input("Ingrese su nombre y apellido: ")
        listaNombres.append(nombre)
        listaContrasenas.append(contrasena)
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
    print("Menú de gestión de usuarios: \n 0. Volver al menú principal \n 1. Registrar usuario \n 2. Eliminar usuario \n 3. Modificar datos de un usuario \n 4. Ver todos los usuarios")
    opcionMenu = int(input("Ingrese el número correspondiente para acceder: ")) 
    while opcionMenu != 0:
        while opcionMenu != 0 and (opcionMenu < 1 or opcionMenu > 4): #Validación de la opción de Menú
            if opcionMenu != 0:
                print("\n Error. Seleccione una de las opciones siguientes.")
                print("Menú de gestión de usuarios: \n 0. Volver al menú principal \n 1. Registrar usuario \n 2. Eliminar usuario \n 3. Modificar datos de un usuario \n 4. Ver todos los usuarios")
                opcionMenu = int(input("Ingrese el número correspondiente para acceder: "))
        
        #Luego de validar opciones:
        if opcionMenu == 1:
            RegistrarUsuario(idUsuarios, contrasenasUsuarios,nombreUsuarios)
        elif opcionMenu == 2:
            print("")
        elif opcionMenu == 3:
            print("")
        elif opcionMenu == 4:
            print("")
        
        # Cuando se terminan las otras funciones:
        print("\n Abriendo menú de usuarios...")
        print("Menú de gestión de usuarios: \n 0. Volver al menú principal \n 1. Registrar usuario \n 2. Eliminar usuario \n 3. Modificar datos de un usuario \n 4. Ver todos los usuarios")
        opcionMenu = int(input("Ingrese el número correspondiente para acceder: "))
    
    print("Volviendo para atrás... \n")

def menuTurnos():
    print("\n Abriendo menú de turnos...")
    print("Menú de gestión de turnos: \n 0. Volver al menú principal \n 1. Registrar nuevo turno \n 2. Finalizar turno \n 3. Ver turnos activos \n 4. Ver turnos finalizados \n 5. Ver estadísticas")
    opcionMenu = int(input("Ingrese el número correspondiente para acceder: ")) 
    while opcionMenu != 0:
        while opcionMenu != 0 and (opcionMenu < 1 or opcionMenu > 5): #Validación de la opción de Menú
            if opcionMenu != 0:
                print("\n Error. Seleccione una de las opciones siguientes.")
                print("Menú de gestión de turnos: \n 0. Volver al menú principal \n 1. Registrar nuevo turno \n 2. Finalizar turno \n 3. Ver turnos activos \n 4. Ver turnos finalizados \n 5. Ver estadísticas")
                opcionMenu = int(input("Ingrese el número correspondiente para acceder: "))
        
        #Luego de validar opciones:
        if opcionMenu == 1:
            print("")
        elif opcionMenu == 2:
            print("")
        elif opcionMenu == 3:
            print("")
        elif opcionMenu == 4:
            print("")
        elif opcionMenu == 5:
            print("")

        # Cuando se terminan las otras funciones:
        print("\n Abriendo menú de turnos...")
        print("Menú de gestión de turnos: \n 0. Volver al menú principal \n 1. Registrar nuevo turno \n 2. Finalizar turno \n 3. Ver turnos activos \n 4. Ver turnos finalizados \n 5. Ver estadísticas")
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