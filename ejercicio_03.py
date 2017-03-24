# Diseñar un algoritmo que aplique un descuento del 10%
# al monto total de una compra si el pago es de contado

monto = 100
de_contado = input("Contado? (si/no): ")
if(de_contado == "si"):
    contado = True
else:
    contado = False
if(contado):
    porc = monto * 10 / 100
    print(monto - porc)
else:
    print(monto)
