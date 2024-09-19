1.#Escriba una función abundantecercano(n), al que se le pasa un entero (n>=100)
##y calcule y devuelva el número entero abundante que finalice en 6 más próximo,
##por encima o por debajo, al n recibido. En caso de empate, prima el que está por debajo

def suma_divisores(n):
    suma=0
    for i in range(n-1,0,-1):
        if n%i==0:
            suma=suma+i
    return suma

def inferior(n):
    a=n
    while True:
        cadena=str(a)
        if cadena[-1]=="6" and a<suma_divisores(a):
            return a
        a=a-1

def superior(n):
    b=n
    while True:
        cadena=str(b)
        if cadena[-1]=="6" and b<suma_divisores(b):
            return b
        b=b+1

def abundante_cercano(n):
    valor_por_arriba=superior(n)
    valor_por_debajo=inferior(n)
    dist_arriba=valor_por_arriba-n
    dist_abajo=valor_por_debajo-inferior(n)
    if dist_arriba<dist_abajo:
        return valor_por_arriba
    else:
        return valor_por_debajo

def main():
    n=int(input("Introduce el número: "))
    while n<100:
        n=int(input("Introduce el número, debe ser mayor o igual a 100: "))
    print("La suma de los divisores es: ", suma_divisores(n))
    print("El abundante más cercano es: ", abundante_cercano(n))

if __name__ == '__main__':
    main()
