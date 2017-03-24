# Escribir un programa que rellene un array con los números entre
# el 0 y 100 e imprima la lista en pantalla

cont = 0
lis_cont = []
while (cont <= 100):
    lis_cont.append(cont)
    cont = cont + 1
    if (cont == 101):
        print(lis_cont)

