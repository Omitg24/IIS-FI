numero = int(input("Ingresa un numero: "))
i = 0

while numero > 0:
    i = i + 1
    resto = numero % 10
    numero2 = int(numero/10)
    print("Las cifras del número ", numero, " de la menos a la más significativa son: ","%d" % (resto), end = " ")