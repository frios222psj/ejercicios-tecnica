# Crear un programa que permita ingresar contactos (como una agenda de contactos).
# El programa deberá tener un menu con 2 opciones. La opción 1 permitirá al usuario
# cargar nombre, y teléfono del contacto. La opción 2 imprimirá el listado de contactos, 
# con un contacto por linea,y sus datos separados por coma.

lista_datos = []
menu = True

while(menu):
    print ("Ingresar (1)-Carga Nombre Y Telefono ")
    print ("")
    print ("Ingresar (2)-Imprimir ")
    print ("")
    opcion = input ("Igrese su opción: ")
    
    if (opcion == "1"):
            print ("")
            m_contactos = {
            "nombre": input("Ingresar su nombre: "),
            "telefono": input("Ingrese su teléfono: ")
            }
            lista_datos.append(m_contactos)


    elif (opcion == "2"):
        print ("")
        for datos in lista_datos:
            print (m_contactos["nombre"] + " , " + m_contactos["telefono"])

    else:
       menu = False
