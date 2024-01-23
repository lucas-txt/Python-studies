from random import randint


def mensagem():
    """
    Serve apenas para criar uma linha e adicionar a mensagem "analisando os valores..."
    Não recebe valores
    """
    print(20*'\033[33m-=-\033[m')
    print('Analisando os valores passados...')

def gerar(quantidade):
    cont = 0
    maior = menor = 0

    for c in range(0, quantidade):
        aleatorio = randint(1, 9)
        print(f'\033[32m{aleatorio}\033[m', end=' ')
        cont += 1
        if c == 0:
            maior = aleatorio
            menor = aleatorio
        else:
            if aleatorio > maior:
                maior = aleatorio
            if aleatorio < menor:
                menor = aleatorio
    print(f'Foram informados \033[34m{cont}\033[m valores ao todo.')
    print(f'O maior valor informado foi \033[31m{maior}\033[m e o menor foi \033[36m{menor}\033[m')
    

for c in range(0, 5):
    mensagem()
    gerar(randint(1, 9))