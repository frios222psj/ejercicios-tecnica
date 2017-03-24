#  Diseñar un programa que permita al usuario cotizar valores en dólares y euros. Considerando que el
# dólar esta a $15.60 y el euro a $17.90, calcular el valor en pesos del monto ingresado por el usuario
# en la moneda seleccionada.

moneda = input("A que moneda desea cambiar los $? (Dolar/ Euro)")

if( moneda=="Dolar"):
    imp = input("Ingrese Monto:$ ")
    imp = float(imp)
    imp_dolar = imp * 15.60
    print(imp_dolar)
elif (moneda == "Euro"):
    imp = input("Ingrese Monto:$ ")
    imp = float(imp)
    imp_euro = imp * 17.90
    print(imp_euro)
else:
    print("Moneda Incorrecta, hasta luego...")
