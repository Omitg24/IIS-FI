lista=[12,3,56,13,78,78,999,109]
i=int(input("Introduzca el primer valor: "))
j=int(input("Introduzca el segundo valor: "))

a=lista[j]
b=lista[i]
lista[i]=a
lista[j]=b

print(lista)

if lista[i]<lista[j]:
    print(i)
elif lista[i]>lista[j]:
    print(j)