# Escribe un programa en Python que calcule la media de todos los números
# introducidos por el usuario por  teclado.  El  final  de  la  secuencia  de
# números  vendrá  indicado  por  la  introducción  del  valor  0. Mostrar el
# resultado con dos dígitos decimales.


def main():
    pass
suma=0.0
count=0

finished=False
while not finished:
    numbers=float(input("Siguiente número: "))
    if numbers!=0:
        suma=suma+numbers
        count=count+1
    else:
        finished=True
print("La media aritmética es {:.2f}".format(suma/count))

if __name__ == '__main__':
    main()
