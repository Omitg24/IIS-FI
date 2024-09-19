def lee_entero():
    """Dado un número entero, lo devuelve """
    return int(input("Introduzca un entero: "))

def mayor():
    """Devuelve el mayor de tres numeros enteros"""
    a=lee_entero()
    b=lee_entero()
    c=lee_entero()
    return max(a,b,c)

print("El mayor de los números es: ", mayor())
