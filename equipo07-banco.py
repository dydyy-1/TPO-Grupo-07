usuarios = ["prueba","prueba2"]
contrasenas = ["123","prueba2"]

def login():
    usuarioExiste = 0
    
    while usuarioExiste == 0:
        preguntarUsuario= str(input("Ingrese su nombre de usuario: "))
        for i in range(len(usuarios)):
            if preguntarUsuario == usuarios[i]:
                usuarioExiste = 1
                indexUsuario = i
        if usuarioExiste == 0:
            print("Error. Usuario no existente.")

    intentos = 3
    while intentos > 0 and intentos !=99:
        preguntarContrasenia = str(input("Ingrese su contraseña: "))    
        if preguntarContrasenia == contrasenas[indexUsuario]:
            intentos = 99
        else:
            intentos -= 1
            print("Error. Contraseña incorrecta.")
            print("Te quedan", intentos, "intentos.")
    if intentos == 99: #Contraseña correcta
        print("Contraseña correcta. Bienvenido/a", usuarios[indexUsuario],"!")
    else:
        print("Vuelve a intentarlo más tarde.")


login()