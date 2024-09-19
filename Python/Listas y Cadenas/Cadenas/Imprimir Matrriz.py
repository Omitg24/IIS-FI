matriz=[["a","b","c","d"],["e","f","g","h"],["i","j","k","l"]]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
##        if matriz[i][j]=='f':
##            matriz[i][j]='X'
        print(matriz[i][j], end=" ")
    print()