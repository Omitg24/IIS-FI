# Modifica el programa en Python del ejercicio anterior para que, en lugar de
# introducir la puntuación total obtenida por cada jugador, se introduzca el valor
# de cada carta retirada por los mismos en sus respectivos turnos. Primero jugará
# el jugador 1 su turno entero, y después el jugador 2. El turno del jugador
# terminará cuando bien se plante (se introducirá un númeroinferior o igual a 0
# para indicarlo), o cuando supere los 21 puntos. El programa debe controlar que
# no se introduzcan valores superiores a 11, ya que no existen cartas de tal valor.

def main():
    pass

score1=0
score2=0

finished = False
while score1<=21 and not finished:
    points=int(input("Jugador 1 ({} puntos): ".format(score1)))
    if points > 11:
        print("{} no es un número válido de puntos".format(points))
    elif points > 0:
        score1=score1+points
    else:
        finished = True
print("El jugador 1 terminó su turno con {} puntos".format(score1))

finished = False
while score2<=21 and not finished:
    points=int(input("Jugador 2 ({} puntos): ".format(score2)))
    if points > 11:
        print("{} no es un número válido de puntos".format(points))
    elif points > 0:
        score2=score2+points
    else:
        finished = True
print("El jugador 2 terminó su turno con {} puntos".format(score2))

if score1 > 21 and score2 > 21:
    print("Ambos jugadores pierden con {1} y {2}".format(score1,score2))
elif score1 <=21 and (score2 > 21 or score1> score2):
    print("El jugador 1 gana con {} puntos". format(score1))
elif score2 <=21 and (score1 > 21 or score2 > score1):
    print("El jugador 2 gana con {} puntos".format(score2))
else:
    print("Ambos jugadores han empatado con {} puntos".format(score1))


if __name__ == '__main__':
    main()
