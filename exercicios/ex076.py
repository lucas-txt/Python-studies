listagem = ('lapis', 2.50,
            'caneta', 5,
            'borracha', 2,
            'caderno', 40,
            'estojo', 20,
            'apontador', 4,
            'mochila', 80)
print(20*'--')
print('LISTAGEM DE PREÇOS')
print(20*'--')
for produto in range(0, len(listagem)):
    if produto % 2 == 0:
        print(f'{listagem[produto]:.<30}', end='')
    else:
        print(f'R${listagem[produto]:<6.2f}')