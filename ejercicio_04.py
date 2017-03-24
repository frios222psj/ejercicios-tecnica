# Diseñar un programa que solicite al operador un usuario. Los posibles nombres
# de usuario son "admin" y "operador". En caso de ser admin, se muestra la leyenda
# "Bienvenido Administrador", en caso de ser operador, "Bienvenido Operador", y
# en caso de ser otro usuario distinto, se muestra "Usuario desconocido".
# En caso de que el usuario haya ingresado admin u operador, se le solicita la
# contraseña, sino, se termina la ejecución.

usuario = input("Ingrese su nombre de usuario: ")

if (usuario == "admin"):
    contrasena = input("Ingrese su Clave: ")
    if (contrasena == "12345"):
        print ("Bienvenido Administrador" )
    else :
        print ("Acceso denegado")
elif (usuario == "operador" ):
    clave = input("Ingrese su Clave: ")
    if (clave == "123"):
        print ("Bienvenido Operador")
    else:
        print ("Acceso denegado")
else:
    print ("usuario desconocido")
