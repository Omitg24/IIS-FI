2. #Dada la siguiente función:

def valor_letra(letra):
    letra = letra.lower()
    if len(letra) > 1 or len(letra) == 0 or not letra.isalpha():
        return 0
    else:
        return 1 + ord(letra) - ord('a')

##Función codigo_palabra que, dada una cadena de caracteres retorna el código
##cabalístico generado como sigue. El código cabalístico se obtiene como la suma
##el valor de cada letra, el valor de cada letra se obtiene con la función valor_letra.

def codigo_palabra(cadena):
    suma=0
    for i in range(len(cadena)):
        c=valor_letra(cadena[i])
        suma=suma+c
    return suma

###Función buscador que recibe una palabra P y una lista con palabras.
##De entre la lista, retorna aquella cuya distancia a P sea menor.
##Si existen varias con la misma distancia se elige la primera.
##La distancia se calcula como el valor absoluto de la diferencia de los códigos de las palabras

def buscador(P,lista):
    result=[]
    for i in range(len(lista)):
        result.append(abs(codigo_palabra(P)-codigo_palabra(lista[i])))
    c=min(result)
    return lista[c]


def main():
    cadena="Hola mundo"
    P="Hola"
    lista=['interpretación','mistica','y','alegorica','del' ,'antiguo','testamento','propia','del','la','tradicion','judia','que','pretende','revelar','un','saber','oculto','acerca','dios','mundo']
    print(f"El codigo de la cadena {cadena} es: ", codigo_palabra(cadena))
    print(f"La palabra con distancia más pequeña a la palabra {P} es: ", buscador(P,lista))


if __name__ == '__main__':
    main()
