def ordenada(lista):
    for i in range(1,len(lista)):
        if lista[i]<lista[i-1]:
            return False
    return True

# def ordenada(lista):
    # se recorre la lista mirando si algún elemento es menor que el anterior
    # empezando en 1 para que el anterior sea 0
    # fallos=sum([1 for i in range(1,len(lista)) if lista[i]<lista[i-1]])
    # return fallos==0

def main():
    lista=[9,11,10,20]
    lista2=["Ana", "Juan", "Teresa"]
    print(ordenada(lista))
    print(ordenada(lista2))

if __name__ == '__main__':
    main()
