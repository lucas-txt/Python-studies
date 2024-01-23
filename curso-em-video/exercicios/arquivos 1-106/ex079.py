valores = []
valores.append(int(input('Digite um valor: ')))
print('Valor adicionado com sucesso...')
while True:
    escolha = input('\033[32mQuer continuar? [S/N] \033[m').upper().strip()[0]
    if escolha == 'N':
        break
    valor = int(input('Digite um valor: '))
    fim = 0
    for p, v in enumerate(valores):
        if v == valor:
            fim += 1
    if fim == 0:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
print(f'Você digitou os valores', end=' ')
valores.sort()
for p, v in enumerate(valores):
    print(v, end=' ')
    