año=int(input("El año es: "))

if año%4==0 and not año%100==0:
    print("{} es BISIESTO ya que es divisible por 4 y no divisible por 100".format(año))
elif año%4==0 and año%100==0 and año%400==0:
    print("{} es BISIESTO ya que es divisible por 4, por 100 y por 400".format(año))
elif año%4==0 and año%100==0 and not año%400==0:
    print("{} NO es BISIESTO ya que es divisible por 4, por 100 y no por 400".format(año))
elif año%4!=0:
    print("{} NO es BISIESTO ya que no es divisible por 4".format(año))