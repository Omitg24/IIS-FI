def binario(dec):
    b=""
    if dec==0:
        return "0"
    while dec>0:
        b=str(dec%2)+b
        dec=dec//2
    return b

def main():
    num=125
    print(binario(num))

if __name__ == '__main__':
    main()
