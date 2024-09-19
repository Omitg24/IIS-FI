a=int(input("La nota 1 es: "))
b=int(input("La nota 2 es: "))
c=int(input("La nota 3 es: "))
d=int(input("La nota 4 es: "))

avg=(a+b+c+d)/4
print("La media es: ", avg)

if avg>=90 and avg <=100:
    print("A")
elif avg>=80 and avg <90:
    print("B")
if avg>=700 and avg <80:
    print("C")
if avg>=60 and avg <70:
    print("D")
if avg>=0 and avg <60:
    print("E")
