# Diseñar un programa que solicite al operador un usuario y una contraseña, y que valide que esos datos
# sean correctos para permitir el ingreso al sistema.

usuario = input("usuario: ")
print(usuario)
if(usuario == "Fer" ):
    clave = input("Password: ")
    if(clave == "12345"):
        print("Bienvenido al Sistema")
    else:
        print("su clave es incorrecta")
else:
    print("usuario no existente")
