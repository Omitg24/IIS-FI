def split_data(lines):
    campos=lines.split(",")
    campos[1]=int(campos[1])
    campos[2]=int(campos[2])
    return campos

def main():
    f_in=open("input.csv","r")
    f_out=open("output.csv","w")
    line=f_in.readline()
    while line!="":
        linea_completa=split_data(line)
        pobalcion=linea_completa[1]+linea_completa [2]
        f_out.write(linea_completa[0]+" - "+str(pobalcion)+"\n")
        line=f_in.readline()

    f_in.close()


if __name__ == '__main__':
    main()
