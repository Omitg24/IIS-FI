#Persistencia aditiva y raiz digital

original=int(input("Dime un numero entero:"))
n=original
persistencia=0
while n>9:
    suma=0
    for i in str(n):
        suma=suma+int(i)
    n=suma
    persistencia=persistencia+1
print("La persistencia aditiva de",original,"es",persistencia,"y su raiz digital",n)