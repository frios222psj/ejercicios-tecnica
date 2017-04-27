# Crear una función que busque los elementos de una lista que coinciden con un valor
# dado, y los reemplace por otro también dado

def reemplazar_enlista(lis, busco,remp):
    lreemp = []

    for el in lis:
        if(l == busco):
            lremp.append(remp)
        else:
            lremp.append(l)
    return lremp

lista_original = ["MariCris","Mika","Carina","Vero","Facu","Mauricio","Kevin","Cristian","Fer"]
lista_reemplazada = reemplazar_enlista(lista_original, "Boc.A", "No-B","B.entral", "ri.B.er")

print(lista_reemplazada)

