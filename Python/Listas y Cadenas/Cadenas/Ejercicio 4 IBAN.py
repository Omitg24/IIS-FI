def digitos_control(CP,CCC):
    base=CCC+CP+"00"
    base_num=""
    for i in base:
        if not i.isdigit():
            base_num=base_num+str(ord(i)-ord("A")+10)
        else:
            base_num=base_num+1

    return "{:02}".format(98-(base_num%97))

def iban(CP,CCC):
    DC=digitos_control(CP,CCC)
    iban=CP+DC+CCC
    iban_format=iban[:4]
    for i in range(4, len(iban),4):
        iban_format=iban_format+" "+iba[i:(i+4)]
    return iban_format

def main():
    CP=input("Introduce el códgio del país: ")
    CCC=input("Introduce el número de cuenta: ")

if __name__ == '__main__':
    main()
