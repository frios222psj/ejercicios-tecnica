# Pedir al usuario que ingrese 10 números, almacenarlos en un array
# y mostrarlos en pantalla al finalizar la carga.
cont = 0
num = []
while(cont < 10):
    num.append(input("Ingrese un número: "))
    cont = cont + 1
print(num)
