def es_primo(n):
    for i in range(n//2,1,-1):
        if n%i==0:
            return False
    return True

def main():
    n=int(input("Introduzca un número: "))
    while n>0:
        if es_primo(n)==True:
            print("Es primo")
        elif es_primo(n)==False:
            print("No es primo")
        n=int(input("Introduzca un número: "))

if __name__ == '__main__':
    main()

##def es_primo(n):
##    for i in range(1,n):
##        if(n%i!=0):
##            continue
##        elif i!=1 and i!=n and n%i==0:
##            return "no es primo"
##            break
##    else:
##        return "Es primo"
##
##def main():
##    n=int(input())
##    while n>0:
##        print(es_primo(n))
##        n=int(input())
##
##
##if __name__ == '__main__':
##    main()