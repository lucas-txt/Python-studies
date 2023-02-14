def leia(msg):
    from utilidades import moeda

    while True:
        valor = input(msg).strip().replace(',','.')
        if valor.isalpha() or valor == '':
            print(f'\033[31m[ERRO] {valor} é um preço invalido \033[m')
        else:
            return float(valor)
        