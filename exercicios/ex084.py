pessoas = list()
while True:
    pessoa = list()
    pessoa.append(input('Nome: '))
    pessoa.append(int(input('Peso: ')))
    pessoas.append(pessoa[:])

    if len(pessoas) == 1:
        maior = menor = pessoas[0][1]

    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]

    esc = ' '
    while esc not in 'NS':
        esc = input('Quer continuar: [S/N] ').strip().upper()[0]
    if esc != 'S':
        break

print(f'Ao todo você cadastrou {len(pessoas)} pessoas')

print(f'O maior peso foi {maior}KG do', end=' ')
for contador in pessoas:
    if pessoas[contador][1] == maior:
        print(f'[{pessoas[contador][0]}]', end=' ')
        
print(f'\nO menor peso foi {menor} do', end=' ')
for contador in pessoas:
    if pessoas[contador][1] == menor:
        print(f'[{pessoas[contador][0]}]', end=' ')