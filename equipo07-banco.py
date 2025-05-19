usuariosID = [-1]
contrasenas = ["admin"]

def RegistrarUsuario(listaUsuarios, listaContrasenas):
    cantidad = int(input("Ingrese la cantidad de usuarios para registrar: "))
    cont = 0
    while cantidad <= 0:
        print("Error. La cantidad tiene que se mayor a 0.")
        cantidad = int(input("Ingrese la cantidad de usuarios para registrar: "))              

    while cont < cantidad:
        id = int(input("Ingrese el id del usuario a registrar (cuatro dígitos): "))
        while id < 1000 or id > 9999:
            id = int(input("Error. Ingrese el id del usuario a registrar (cuatro dígitos): "))
        listaUsuarios.append(id)
        contrasena = str(input("Ingrese la contraseña del usuario a registrar (mínimo 5 caracteres): "))
        while len(contrasena) < 5:
            contrasena = str(input("Error. Ingrese la contraseña del usuario a registrar: (mínimo 5 caracteres): "))
        listaContrasenas.append(contrasena)
        cont += 1
                           

def login(listaUsuarios, listaContrasenas):
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
            print("Contraseña correcta. Bienvenido/a",
                  listaUsuarios[indexUsuario], "!")
        else:
            print("Error. Contraseña incorrecta.")


login(usuariosID, contrasenas)

def menuUsuarios():
    print("Abriendo menú de usuarios...")
    print("\n Menu de usuarios")
    print(" Menú de opciones: \n 0. Volver atrás. \n 1. Registrar usuario \n 2. Eliminar usuarios \n 3. Modificar datos del usuario")
    opcionMenu = int(input("Ingrese el número correspondiente para acceder: "))  #Variable para finalizar programa o volver para atrás
    while opcionMenu != 0:
        while opcionMenu != 0 and (opcionMenu < 1 or opcionMenu > 3): #Validación de la opción de Menú
            if opcionMenu != 0:
                print("\n Error. Seleccione una de las opciones siguientes.")
                print(" Menú de opciones: \n 0. Volver atrás. \n 1. Registrar usuario \n 2. Eliminar usuarios \n 3. Modificar datos del usuario")
                opcionMenu = int(input("Ingrese el número correspondiente para acceder: "))
        
        if opcionMenu == 1:
            RegistrarUsuario(usuariosID, contrasenas)

def menuInicio():
    print("\n Menu principal")
    print(" Menú de opciones: \n 0. Finalizar programa. \n 1. Usuarios \n 2. Turnos.")
    opcionMenu = int(input("Ingrese el número correspondiente para acceder: "))  #Variable para finalizar programa o volver para atrás
    while opcionMenu != 0:
        while opcionMenu != 0 and (opcionMenu < 1 or opcionMenu > 2): #Validación de la opción de Menú
            if opcionMenu != 0:
                print("\n Error. Seleccione una de las opciones siguientes.")
                print(" Menú de opciones: \n 0. Finalizar programa. \n 1. Usuarios \n 2. Turnos.")
                opcionMenu = int(input("Ingrese el número correspondiente para acceder: "))

        if opcionMenu == 1:
            print("Opción 1.")
            menuUsuarios()

        elif opcionMenu == 2:
            print("")
        
        print(" Menú de opciones: \n 0. Finalizar programa. \n 1. Usuarios \n 2. Turnos.")
        opcionMenu = int(input("Ingrese el número correspondiente para acceder: "))
    
    print("Finalizando programa")

menuInicio()

