##Dado un número natural n, escribe un programa que proporcione la siguiente salida

n=int(input())
print()

for i in range(1,n+1):
    print(i)
    for j in range(1, i+1):
        print(j, end=" ")
