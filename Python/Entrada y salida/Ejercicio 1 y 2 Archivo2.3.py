#Ejercicio 1 y 2

def main():
    pass

name=str(input("El nombre del alumno: "))
mark1=float(input("La primera nota es: "))
mark2=float(input("La segunda nota es: "))

avg=(mark1+mark2)/2
print("La nota media de {} es: {}".format(name,avg))

if avg >= 5:
    print("Aprueba la asignatura: Verdadero")
else:
    print("Aprueba la asignatura: Falso")

if __name__ == '__main__':
    main()
