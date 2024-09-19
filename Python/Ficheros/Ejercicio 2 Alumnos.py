def numero_de_alumnos():
    f=open("alumnos.txt","r")
    datos=f.readlines()
    f.close()
    return len(datos)

def coincide_apellido(linea,apellido):
    f=open("alumnos.txt","r")
    datos=f.readlines()
    if apellido in datos[linea]:
        return True
    else:
        return False
    f.close()

def porcentaje(apellido):
    f=open("alumnos.txt","r")
    datos=f.readlines()
    count=0.0
    for i in range(len(datos)):
        if apellido in datos[i]:
            count=count+1
    return (count/len(datos))*100
    f.close()

def palabras_en_nombre(linea):
    f=open("alumnos.txt","r")
    datos=f.readlines()
    c=0
    for linea in datos:
        c=datos.split()
    return len(c)
    f.close()

def main():
##    l1=int(input("Introduzca una linea: "))
##    a1=str(input("Introduzca un apellido: "))
##    l2=int(input("Introduzca otra linea: "))
##    a2=str(input("Introduzca otro apellido: "))

    l1=1
    a1="Duque"
    l2=3
    a2="Fernandez"
    print()
    print("-------------Programas-------------")
    print()
    print("El número de alunnos es: ", numero_de_alumnos())
    if coincide_apellido(l1,a1)==True:
        print("El apellido coincide")
    else:
        print("El apellido no coincide")
    print("El porcentaje de alumnos con ", a1," es ", round(porcentaje(a2),3),"%")
    print(f"El número de palabras en la linea {l2} es: ", palabras_en_nombre(l2))

if __name__ == '__main__':
    main()
