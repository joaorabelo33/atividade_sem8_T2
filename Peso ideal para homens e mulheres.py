

def qual_sexo(sexo):
    if(sexo==2):
        return 'mulheres'
    else:
        return 'homens'

def calcula_algo(altura, sexo):
    resultado = 0
    if(qual_sexo(sexo)=='homens'):
        resultado = (72.7 * altura) - 58
    elif(qual_sexo(sexo)=='mulheres'):
        resultado = (62.1 * altura) - 44.7
    else:
        raise ValueError('Entrada inválida')
    return resultado

def main():
    altura = input()
    sexo = input()
    altura = float(altura)
    sexo = int(sexo)

    resultado = calcula_algo(altura, sexo)

    print(f'{resultado:.2f}')


if __name__ == '__main__':
    main()