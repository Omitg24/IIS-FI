def inserta_ceros(lista):
    for i in range(len(lista)-1,-1,-1):
        if lista[i]<0:
            lista.insert(i,0)

##def inserta_ceros(lista):
##    # modifica la lista insertando un cero delante de cada numero negativo
##    i=0 # indice del primer elemento de la lista
##    while i<len(lista):
##        if lista[i]<0: # si es negativo se inserta un cero
##            lista.insert(i,0)
##            i=i+1 # hay que saltar el cero insertado
##        i=i+1 # se pasa al siguiente elemento de la lista
##
##def inserta_ceros(lista):
##    # se crea una lista nueva insertando los ceros antes de los negativos
##    nueva=[]
##    for elemento in lista:
##        if elemento<0:
##            nueva.append(0)
##        nueva.append(elemento)
##    # se reemplaza el contenido de la original por el de la nueva
##    lista[:]=nueva
##
##def inserta_ceros(lista):
##    # se crea una lista nueva insertando los ceros antes de los negativos
##    otra=[]
##    [(otra.append(0),otra.append(x)) if x<0 else otra.append(x) for x in lista]
##    # se reemplaza el contenido de la original por el de la nueva
##    lista[:]=otra

def main():
    lista=[10,11,-7,4.5,-2,-2,6.3,8,-1]
    print("Lista antes: ", lista)
    inserta_ceros(lista)
    print("Lista después: ",lista)

if __name__ == '__main__':
    main()
