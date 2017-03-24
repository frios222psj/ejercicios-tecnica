#Solicitar una frase al usuario, y mostrar cuantas vocales hay en la frase.

contador = 0
f = input("Ingresar una frase: ")
for lt in f:

    if (lt == "a"):
        contador = contador + 1

    elif (lt == "e"):
            contador = contador + 1

    elif (lt == "i"):
            contador = contador + 1

    elif (lt == "o"):
            contador = contador + 1

    elif (lt == "u"):
        contador = contador + 1

print ("")
print ("Cant_vocal " + str(contador) + " Vocales")

