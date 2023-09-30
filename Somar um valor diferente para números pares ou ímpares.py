
def eh_par(numero):
    return numero % 2 == 0

def main():
    numero = input()
    numero = int(numero)    

    if(eh_par(numero)):
        numero +=5
    else:
        numero +=8

    print(numero)    


if __name__ == '__main__':
    main()