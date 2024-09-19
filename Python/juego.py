
def jugada(a,b):

    if a=="O":
        if b=="X":
            return 1
        if b=="[]":
            return 2
        if b=="O":
            return 0
    if a=="X":
        if b=="X":
            return 0
        if b=="[]":
            return 1
        if b=="O":
            return 2
    if a=="[]":
        if b=="X":
            return 2
        if b=="[]":
            return 0
        if b=="O":
            return 1

    """
        - [String, String] Recibe dos simbolos (O,[], o X), uno de cada jugador
        - [Int] Devuelve un 1 si ganó "a", un dos si ganó "b" y un 0 si hubo empate.
    """


def pedirTiradas(tiradas):
    m=[]
    for i in range(1, tiradas+1):
        t=[]
        for j in range(3):
            t.append(mostrarMenuJugada("Tirada "+ str(i) + "Jugada " + str(j+1) + "/3: "))
        m.append(t)
    return m


def mostrarMenuJugada(pos):
    print("0.................Piedra")
    print("[].................Papel")
    print("X.................Tijera")
    t=input(pos)
    while t not in["0","[]","X"]:
        t=input("Jugada incorrecta, Vuelve a probar" + str(pos)+"\t")
    return t


def jugar(m1, m2):

    puntos1=0
    puntos2=0
    tiradas1=0
    tiradas2=0
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            res=jugada(m1[i][j], m2[i][j])
            if res==1:
                puntos1=puntos1+1
            if res==2:
                puntos2=puntos2+1
        if puntos1>puntos2:
            tiradas1=tiradas1+1
        elif puntos1<puntos2:
            tiradas2=tiradas2+1
        puntos1=0
        puntos2=0
    res=[tiradas1,tiradas2]
    return res

    """
        - [List, List] Recibe dos matrices con las tiradas y jugadas de cada jugador
        - [List] Devuelve una lista con dos posiciones, en la primera se devolverá
                 las tiradas ganadas por el primer jugador y en la segunda, del segundo jugador.

            Para contabilizar una tirada a un jugador, este deberá ganar más jugadas que el otro,
            en caso de empate no se contabilizará nada

    """

def mostrarTablero(t):
    for i in range(len(t)):
        for j in range(len(t[i])):
            print(t[i][j], end="\t")
        print()


def main():
    numTiradas=int(input("¿Cuantas tiradas quieres jugar?"))
    tableroA=pedirTiradas(numTiradas)
    tableroB=pedirTiradas(numTiradas)



    print("Jugadas del Jugador 1")
    mostrarTablero(tableroA)
    print("Jugadas del Jugador 2")
    mostrarTablero(tableroB)

    resultados=jugar(tableroA,tableroB)
    print("Tiradas del Jugador 1: ", resultados[0])
    print("Tiradas del Jugador 2: ", resultados[1])
    if (resultados[0]>resultados[1]):
        print("Gana el Jugador 1")
    elif (resultados[0]<resultados[1]):
        print("Gana el Jugador 2")
    else:
        print("Empate")



if __name__ == '__main__':
    main()