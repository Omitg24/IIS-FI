number=int(input("Introduzca el número: "))
print("ESCOGE UNA OPCIÓN. Calcular:", "\na) El cuadrado del número", "\nb) El cubo del número", "\nc) El doble del número")

Option=str(input("La Opción elegida es: "))

if Option=="a":
    x=number**2
    print("El cuadrado del número {} es {}".format(number,x))
elif Option=="b":
    x=number**3
    print("El cubo del número {} es {}".format(number,x))
elif Option=="c":
    x=number*2
    print("El doble del número {} es {}".format(number,x))
