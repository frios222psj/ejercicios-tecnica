# Escribir un programa que genere una escalera de pipe lines como la siguiente: (por cada linea, agregar un _ bajo adelante).

cantidad = 1
while (cantidad <= 10):
    pipe = "_" * (cantidad - 1)
    print (pipe + "|")
    cantidad += 1
