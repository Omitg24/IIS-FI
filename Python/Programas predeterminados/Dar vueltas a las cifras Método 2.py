#Dar vuelta a las cifras Método 2

numero=int(input("numero:"))
n=numero
print("las cifras el numero",n,"de la menos a la mas significativa son:",end=" ")
for i in range(len(str(numero))):
    ultimo_digito=n%10
    print(ultimo_digito,end=" ")
    n=n//10