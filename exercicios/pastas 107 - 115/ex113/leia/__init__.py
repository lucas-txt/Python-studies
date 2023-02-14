def LeiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except:
            print('\033[31m[ERRO] Por favor, digite um numero real valido.\033[m')


def LeiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
            return valor
        except:
            print('\033[31m[ERRO] Por favor, digite um numero real valido\033[m')