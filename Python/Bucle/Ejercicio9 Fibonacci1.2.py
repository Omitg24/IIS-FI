def main():
    pass

value=int(input("Especifica el valor de inicio de la serie: "))
while value <= 0:
    print("El valor de inicio de la serie debe ser superior a 0")
    value=int(input("Especifica el valor de inicio de la serie: "))

numero = int(input("Especifica el número de elementos a mostrar: "))
while numero <= 0:
    print("El valor del número de elementos a mostrar debe ser superior a 0")
    numero = int(input("Especifica el número de elementos a mostrar: "))

for i in range(numero):
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
