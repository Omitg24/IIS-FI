def capitalize(frase):
    palabras=frase.split(" ")
    for i in range(len(palabras)):
        palabra=palabras[i]
        palabras[i]=palabra[:1].upper()+palabra[1:]
    return " ".join(palabras)

def main():
    frase="hay mas de 50 trabajadores de Google"
    print(capitalize(frase))

if __name__ == '__main__':
    main()
