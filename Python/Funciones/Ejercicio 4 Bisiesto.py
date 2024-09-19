def es_bisiesto(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def main():
    year=int(input("Introduzca el año: "))
    print(es_bisiesto(year))

if __name__ == '__main__':
    main()
