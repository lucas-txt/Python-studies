def linha(tamanho=42):
    print(tamanho*'-')


def titulo(msg, tamanho=42):
    linha(tamanho)
    print(msg.center(tamanho))
    linha(tamanho)

def menu(*escolhas):
    titulo('MENU PRINCIPAL')
    for p, v in enumerate(escolhas):
        print(f'\033[33m{p+1} - \033[36m{v}\033[m')
    linha()
    while True:
        try:
            escolha = int(input('\033[34mSua opção: \033[m'))
        except:
            print('\033[31m[ERRO] digite um numero inteiro valido\033[m')
        else:
            if escolha <= len(escolhas):
                return escolha 
            print('\033[31m[ERRO] Digite uma opção valida\033[m')

