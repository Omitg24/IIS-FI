#Calcular numero de digitos

n=int(input("Dame un número:"))
original=n
digitos=0
while n>0:
    digitos=digitos+1
    n=n//10
print(digitos)