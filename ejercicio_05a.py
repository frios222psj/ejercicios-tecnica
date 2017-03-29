# Calcular el promedio de 5 notas ingresadas (notas del 1 al 10).
# Si el promedio es mayor a 7, aprobó la materia, sino reprobó.

lista_nota = []
cant_num = 0

while (cant_num < 5):
    nota = float(input ("Ingrese las notas del alumno: "))
    if (nota <= 10):
        lista_nota.append(nota)
        cant_num += 1
        sum_n = 0
        for n1 in lista_nota:
            sum_n = sum_n + n1
        pro_medio = sum_n / 5
    else:
        print (" La calificacion es del 0 al 10 ")
print ("El promedio es: " + str(pro_medio))
aprob = pro_medio >= 7 
des_aprob = pro_medio <= 6 

if (aprob):
    print ("Aprobado")
else:
    print ("Desaprobado")


