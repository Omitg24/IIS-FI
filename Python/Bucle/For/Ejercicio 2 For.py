n=int(input("Introduzca un número: "))
factorial=1
for i in range(1,n+1,1):
    factorial=factorial*i
print(n,"! = ",factorial)