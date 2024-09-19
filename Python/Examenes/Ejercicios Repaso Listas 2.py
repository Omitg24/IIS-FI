def distancia(lista1,lista2):
    dif=abs(len(lista1)-len(lista2))

    count=0
    for i in range(min(len(lista1),len(lista2))):
        if lista1[i]!=lista2[i]:
            count+=1
    dist=dif+count
    return dist

def extrae_negativos(lista):
    lista_n=[]
    for elem in lista:
        if elem<0:
            lista_n.append(elem)
    for elem in lista_n:
       lista.remove(elem)
    return lista, lista_n

def ordenar(lista):
    for i in range(1,len(lista)):
        if lista[i]<lista[i-1]:
            return False
    return True

def inserta_ceros(lista):
    for i in range(len(lista)-1,-1,-1):
        if lista[i]<0:
            lista.insert(i,0)
    return lista

