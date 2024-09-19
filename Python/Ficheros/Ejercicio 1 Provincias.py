def split_data(lines):
    campos=lines.split(",")
    campos[1]=int(campos[1])
    campos[2]=int(campos[2])
    return campos

def main():
    f=open("input.csv","r")
    lines=f.readlines()

    for i in range(len(lines)):
        fields=split_data(lines[i])
        print(fields[0],"Nº de hombres: ", fields[1], "Nº de mujeres: ", fields[2])

##    line=f.readline()
##    while line!="":
##        linea_completa=split_data(linea)
##        print(linea_completa[0], linea_completa[1], linea_completa[2])
##        line=f.readline()

    f.close()


if __name__ == '__main__':
    main()
