


def soma_numeros(numero):
    tamanho = len(numero)
    soma = 0

    while(tamanho):
        soma += int(numero[tamanho - 1])
        tamanho -= 1 
    
    return soma


def main():
    numero = input().strip()

    if(0 <= int(numero) < 100000):
        resultado = soma_numeros(numero)
        print(resultado)
    else:
        print('-1')

if __name__ == '__main__':
    main()