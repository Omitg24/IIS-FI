def calculateIMC(w,h):
    return w/h**2

def clasification(w,h):
    if calculateIMC(w,h)<18.5:
        return "Bajo peso"
    elif calculateIMC(w,h)>=18.5 and calculateIMC(w,h)<25.0:
        return "Normal"
    elif calculateIMC(w,h)>=25.0:
        return "Sobrepeso"
    elif calculateIMC(w,h)>=30.0:
        return "Obesidad"

def main():
    w=float(input("Introduce el peso: "))
    h=float(input("Introduce la altura: "))
    print(clasification(w,h))

if __name__ == '__main__':
    main()
