# Obtener el mayor valor de una lista cualquiera de números

num_mayor = 0
lista_num = [5, 8, 1, 45, 22, 21, 13,115,2,345]
for n in lista_num:
    if (n > num_mayor):
        num_mayor = n
print ("La lista de números es: " + str(lista_num))
print ("El mayor valor de esta lista es: " + str(num_mayor))
