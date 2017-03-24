#Almacenar 5 números por teclado y mostrar el promedio de ellos

lista_n = []
numero1 = input("Escriba un numero: ")
numero2 = input("Escriba un numero: ")
numero3 = input("Escriba un numero: ")
numero4 = input("Escriba un numero: ")
numero5 = input("Escriba un numero: ")

lista_n.append(numero1)
lista_n.append(numero2)
lista_n.append(numero3)
lista_n.append(numero4)
lista_n.append(numero5)
n_suma = float(numero1) + float(numero2) + float(numero3) + float(numero4) + float(numero5)
promedio = n_suma / 5
print (promedio)
print ("se puede optimizar")

