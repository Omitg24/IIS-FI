n=int(input("Introduzca números positivos: "))
contador=0
maximo=0
while n!=0 and not n<0:
    contador=contador+1
    if n>maximo:
        maximo=n
        contador2=contador
    n=int(input("Introduzca números positivos: "))
print("El mayor número es {} y se proporc2ionó en la posición {}".format(maximo,contador2))