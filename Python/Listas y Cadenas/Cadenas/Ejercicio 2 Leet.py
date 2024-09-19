def leet(frase):
    frase_leet=""
    for car in frase:
        if car in ["a","A", "á", "Á"]:
            frase_leet=frase_leet+"4"
        elif car in ["e","E","é","É"]:
            frase_leet=frase_leet+"3"
        elif car in ["i","I","í","Í"]:
            frase_leet=frase_leet+"1"
        elif car in ["o","O","ó","Ó"]:
            frase_leet=frase_leet+"0"
        else:
            frase_leet=frase_leet+car
    return frase_leet

def main():
    frase="de vuelta a Internet de los años ochenta"
    print(leet(frase))


if __name__ == '__main__':
    main()
