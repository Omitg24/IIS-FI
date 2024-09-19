# Modifica el programa en Python desarrollado enel ejercicio anterior para que,
# en lugar de especificar un umbral, se especifique el número de iteraciones a
# realizar para estimar el valor de e.

def main():
    pass

e=0.0
count=0
factorial=1

iterations= int(input("Especifica el número de iteraciones para el calculo de e: "))
while iterations <= 0:
    print("El número de iteraciones debe ser superior a 0")
    iterations=int(input("Especifica el número de iteraciones para el calculo de e: "))

for i in range (iterations):
    e=e+1/factorial
    count=count+1
    factorial=factorial*count

print("La aproximación de e es {}".format(e))

if __name__ == '__main__':
    main()
