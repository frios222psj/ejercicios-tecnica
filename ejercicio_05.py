# Calcular el promedio de 5 notas ingresadas (notas del 1 al 10).
# Si el promedio es mayor a 7, aprobó la materia, sino reprobó.

n_1 = input("Ingrese la nota 1: ")
n_2 = input("Ingrese la nota 2: ")
n_3 = input("Ingrese la nota 3: ")
n_4 = input("Ingrese la nota 4: ")
n_5 = input("Ingrese la nota 5: ")

n_1 = int(n_1) 
n_2 = int(n_2)
n_3 = int(n_3)
n_4 = int(n_4)
n_5 = int(n_5)

t_notas = n_1 + n_2 + n_3 + n_4 + n_5
t_porcentaje = t_notas / 5


if (t_porcentaje >= 7):
    print ("Aprobado")
else:
    print ("Desaprobado")
