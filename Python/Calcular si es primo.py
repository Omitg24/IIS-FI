#Calcular si es primo

n=int(input("Dame un número entero"))
for i in range(1,n):
    if(n%i!=0):
        continue
    elif i!=1 and i!=n and n%i==0:
        print(n,"no es primo")
        break
else:
    print(n,"es un número primo")