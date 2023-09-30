

def calcular_media(nota_um, nota_dois, nota_tres, media_exercicios):
    media_final = (nota_um + (nota_dois * 2) + (nota_tres * 3) + media_exercicios)/7
    
    return media_final

def mostrar_conceito(nota_um, nota_dois, nota_tres, media_exercicios):
    media_final = calcular_media(nota_um, nota_dois, nota_tres, media_exercicios)
    status = ''
    if(media_final >= 9.0):
        status = 'A'
    if(media_final >= 7.5 and media_final < 9.0):
        status = 'B'
    if(media_final >= 6.0 and media_final < 7.5):
        status = 'C'
    if(media_final >= 4.0 and media_final < 6.0):
        status = 'D'
    if(media_final < 4.0):
        status = 'E'
    return status

def aluno_aprovado(nota_um, nota_dois, nota_tres, media_exercicios):
    status_final = mostrar_conceito(nota_um, nota_dois, nota_tres, media_exercicios)
    status = ''

    if (status_final in ('A,B,C')):
        status = 'Aprovado'
    elif (status_final  in ('D,E')):
        status = 'Reprovado'
    else:
        raise ValueError('Entrada Invalida')

    return status

def main():
    matricula_aluno = input().strip()
    nota_um = float(input())
    nota_dois = float(input())
    nota_tres = float(input())
    media_exercicios = float(input())

    resultado_media = calcular_media(nota_um, nota_dois, nota_tres, media_exercicios)
    resultado_conceito = mostrar_conceito(nota_um, nota_dois, nota_tres, media_exercicios)
    resultado_aprovacao = aluno_aprovado(nota_um, nota_dois, nota_tres, media_exercicios)

    print(f'{matricula_aluno}\n{resultado_media:.2f}\n{resultado_conceito}\n{resultado_aprovacao}')



if __name__ == '__main__':
    main()