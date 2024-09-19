def fichero(name):
    f=open(name,"r")
    datos=f.readlines()
    lista=[]
    copy=[]
    for i in range(len(datos)):
        lista=datos[i].rstrip()
        copy.append(lista)
    copy=[int(x) for x in datos]
    f.close()
    return sum(copy)

def main():
    name=str(input("Introduzca el nombre del fichero: "))
    print(fichero(name))

if __name__ == '__main__':
    main()
