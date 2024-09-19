from math import sqrt
from math import pow
def distancia(a,b):
    return sqrt((pow(a,2)+pow(b,2)))

def main():
    a=int(input("Introduzca una coordenada: "))
    b=int(input("Introduzca otra coordenada: "))
    print(distancia(a,b))

if __name__ == '__main__':
    main()
