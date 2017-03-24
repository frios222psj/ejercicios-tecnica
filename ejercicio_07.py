# Crear una calculadora. El usuario deberá ingresar un valor,luego una operación
# (1 para sumar, 2 para restar, 3 para dividir, 4 para multiplicar) y un segundo valor
# para completar el calculo.El sistema deberá mostrar el resultado.

valor_1 = input("Ingrese su primer valor: ")
print("Ingrese la operacion que desee realizar: ")
print("1 Sumar")
print("2 Restar")
print("3 Dividir")
print("4 Multiplicar")

calc = input("operacion deseada: ")
valor_2 = input("Ingrese el segundo valor: ")

valor_1 = float(valor_1)
valor_2 = float(valor_2)

if (calc == "1"):
    print(valor_1 + valor_2)
elif (calc == "2"):
    print(valor_1 - valor_2)
elif (calc == "3"):
    print(valor_1 / valor_2)
elif (calc == "4"):
    print(valor_1 * valor_2)
else:
    print("Operacion incorrecta")
