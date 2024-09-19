def split_data(lines):
    campos=lines.split(",")
    campos[1]=int(campos[1])
    campos[2]=int(campos[2])
    return campos

def main():
    f=open("input.csv","r")
    line=f.readline()
    while line!="":
        linea_completa=split_data(line)
        if linea_completa[2]>linea_completa[1]:
            print(linea_completa[0], "Ya que ", linea_completa[2], ">", linea_completa[1])
        line=f.readline()

    f.close()


if __name__ == '__main__':
    main()
