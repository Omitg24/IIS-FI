letter=str(input("Introduzca un carácter: "))
x=0
finished=False
while not finished:
    letter=str(input("Introduzca un carácter: "))
    if letter=="a":
        x=x+1
        print("El numero de veces que aparece a es {}".format(x))
    if letter==".":
        finished = True
