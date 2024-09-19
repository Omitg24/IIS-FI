#Dar vueltas a las cifras

n=int(input("Dame un número"))
numero=n
print("Las cifras del número",n,"de la menos a la mas significativa son:",end=" ")
while n >0:
    ultimo_digito=n%10
    print(ultimo_digito,end =" ")
    n=n//10
if numero==0:
    print(0,end=" ")
print()