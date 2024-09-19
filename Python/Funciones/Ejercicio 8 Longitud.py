from math import sqrt
from math import pi
from math import pow

def distancia(a,b):
    return sqrt((pow(a,2)+pow(b,2)))
def longitud(a,b):
    return 2*pi*distancia(a,b)

def main():
    a=int(input("Introduzca una coordenada: "))
    b=int(input("Introduzca otra coordenada: "))
    print(longitud(a,b))

if __name__ == '__main__':
    main()
