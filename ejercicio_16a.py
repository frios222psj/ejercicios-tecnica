# Obtener el menor numero de una lista cualquiera de números

lista_num = [67,56,32,66,90,987,65,9,6,76]
n_menor = lista_num[0]
for n in lista_num:
    if (n < n_menor):
        n_menor = n
print ("La lista de números es: " + str (lista_num))
print ("El menor valor de la lista es: " + str(n_menor))



