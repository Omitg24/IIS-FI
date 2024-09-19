def main():
    numero=int(input("Introduzca el numero: "))
    b=int(input("Introduzca la base: "))
    while b<2 or b>10:
        b=int(input("Introduzca la base, debe ser mayor que 2 y menor o igual a 10: "))
    n=numero
    cadena=""
    while n>0:
        resto=n%b
        n=n//b
        cadena=str(resto)+cadena

    print(numero, "en base ", b, " es: ", cadena)

if __name__ == '__main__':
    main()
