def main():
    pass

value=int(input("Especifica el valor de inicio de la serie: "))
while value <= 0:
    print("El valor de inicio de la serie debe ser superior a 0")
    value=int(input("Especifica el valor de inicio de la serie: "))

umbral = int(input("Especifica un umbral: "))
while umbral <= 0:
    print("El valor del umbral debe ser superior a 0")
    umbral = int(input("Especifica un umbral: "))

while value < umbral:
    print(value, end=" ")

    aux=value
    accum = 1
    while aux > 0:
        if aux % 10 != 0:
            accum = accum *(aux%10)
        aux = aux//10

    value = value + accum

if __name__ == '__main__':
    main()
