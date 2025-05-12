usuarios = ["prueba","prueba2"]
contrasenas = ["123","prueba2"]

def login(listaUsuarios, listaContrasenas):
    usuarioExiste = 0
    claveIncorrecta = 1

    while usuarioExiste == 0:
        preguntarUsuario= str(input("Ingrese su nombre de usuario: "))
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
            print("Contraseña correcta. Bienvenido/a", listaUsuarios[indexUsuario],"!")
        else:
            print("Error. Contraseña incorrecta.")


login(usuarios,contrasenas)

def menuInicio():
    print("""Menú de opciones:
1. 
2.
3.
4.
5. Salir.""")
    finalizarPrograma = int(input("Ingrese el número correspondiente para acceder: "))
    opcionMenu = finalizarPrograma
    while finalizarPrograma != 0:
        while finalizarPrograma !=0 and (opcionMenu <1 or opcionMenu>5):
            if opcionMenu != 0:
                print("\n Error. Seleccione una de las opciones siguientes.")
                print("""Menú de opciones:
        1. 
        2.
        3.
        4.
        5.""")
                opcionMenu = int(input("Ingrese el número correspondiente para acceder: "))
            else:
                finalizarPrograma = 0 #Finalizar programa
        if opcionMenu == 1:
            print("Opción 1.")
    
    print("Finalizando programa")    
        
      

menuInicio()