def main():
    pass

x=int(input("Especifica el valor del cual mostrar los múltiplos: "))
while x<=0:
    print("El valor del número debe de ser mayor que cero")
    x=int(input("Especifica el valor del cual mostrar los múltiplos: "))

a=int(input("Especifica el inicio del intervalo: "))
b=int(input("Espeecifica el final del intervalo: "))

if a % x !=0:
    a=a+x-a%x

for i in range(a,b+1,x):
    print(i,end=" ")

if __name__ == '__main__':
    main()
