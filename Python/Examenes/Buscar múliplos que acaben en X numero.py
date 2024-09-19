
def main():
    n=0
    encontrados=0
    a=int(input("Introduzca el número de múltiplos a buscar: "))
    b=int(input("Introduzca el número en el que deben acabar los multiplos: "))
    c=int(input("Introduzca el número del cual se van a buscar sus múltiplos: "))
    while encontrados<a:
        n=n+1
        if (n%100==b) and (n%c==0):
            print(n)
            encontrados=encontrados+1


if __name__ == '__main__':
    main()
