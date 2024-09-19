def calificación(n):
    if n>=0 and n<5:
        print("Suspenso")
    elif n>=5 and n<7:
        print("Aprobado")
    elif n>=7 and n<9:
        print("Notable")
    elif n>=9 and n<10:
        print("Sobresaliente")
    elif n==10:
        print("Matrícula de Honor")

def main():
    n=int(input("Introduzca la nota del alumno: "))
    calificación(n)

if __name__ == '__main__':
    main()
