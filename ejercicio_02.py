##2.Escribir el algoritmo que, a partir de la cantidad de bancos de un aula y la
# cantidad de alumnos inscriptos para un curso, permita determinar si alcanzan los
# bancos existentes. De no ser así informar cuantos bancos sería necesario agregar

cant_bancos = 30
cant_alumnos = 35

if(cant_bancos >= cant_alumnos):
    print("Alcanzan los bancos")
else:
    print("No alcanzan")
    faltantes = cant_alumnos - cant_bancos
    print("Bancos faltantes  " + str(faltantes))
