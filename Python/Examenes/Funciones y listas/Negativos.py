def extrae_negativos(a):
    negativos=[]
    for i in lista:
        if i<0:
            negativos.append(i)

    for negativo in negativos:
        lista.remove(negativo)
    return negativos

##def extrae_negativos(lista):
##    # creación de la lista de negativos
##    negativos=[x for x in lista if x<0]
##    # se quitan de la original los negativos
##    [lista.remove(x) for x in negativos]
##    # se devuelven los negativos
##    return negativos

lista=[10,11,-7,4.5,-2,-2,6.3,8,-1]
print("lista antes", lista)
negativos=extrae_negativos(lista)
print("lista después", lista)
print("negativos", negativos)