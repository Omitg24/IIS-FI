def naturales_pares(lista):
    count=0
    for elem in lista:
        if elem>0 and elem%2==0:
            count=count+1
    return count

def change_to_negative(lista):
    count=0
    for i in range(len(lista)):
        if lista[i]>0 and lista[i]%2==0:
            count=count+1
            lista[i]=lista[i]*(-1)
    return lista

def change_to_negative(lista):
    count=0
    listan=[]
    for i in range(len(lista)):
        if lista[i]>0 and lista[i]%2==0:
            count=count+1
            listan.append(lista[i])
            lista[i]=lista[i]*(-1)
    return listan, lista

def lista_fibonacci(n):
    result =[]
    if n >0:
        result.append(0)
    if n >1:
        result.append(1)
    for i in range(2, n):
        result.append(result[-1] +result[-2])
    return result

n=8
print(lista_fibonacci(n))