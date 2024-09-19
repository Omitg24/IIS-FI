from operaciones import suma
from operaciones import resta
from entradaSalida import pedirEntero

def mostrarMenu():
    print("------Menu------")
    return int(input("Introduce una opción: "))

def main():
    opcion=mostrarMenu()
    while opcion!=0:
        if opcion==3:
            a=pedirEntero()
            b=pedirEntero()
            print(suma(a,b))
        elif opcion==2:
            a=pedirEntero()
            b=pedirEntero()
            if resta(a,b)>=0:
                print(resta(a,b))
            else:
                print("Resta no puede ser negativa")
        opcion=mostrarMenu()


if __name__ == '__main__':
    main()
