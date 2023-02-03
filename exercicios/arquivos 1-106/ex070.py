print(30*'\033[33m-')
print('LOJA DO LUKINHAS')
c = menor = mil = total = 0
while True:
    c += 1 
    print(f'\033[33mPRODUTO {c}',25*'\033[33m-\033[m')

    nome = input('Nome do produto: ')
    valor = float(input('Preço: R$'))
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N] ').upper().strip()[0]

    total += valor # para saber o total
    if valor > 1000: # para saber quantos produtos custam mais de 1000
        mil += 1 
    if c == 1 or valor < menor: # para saber o menor
        menor = valor
        barato = nome

    if escolha == 'N':
        break

print('\033[36mCONTA', 24*'\033[36m-\033[m')
if c == 1:
    print(f'Você comprou {c} produto')
else:
    print(f'Você comprou {c} produtos')
print(f'O total da compra foi: {total:.2f}')
if mil == 1:
    print(f'Temos {mil} produto custando mais de 1000R$')
else:
    print(f'Temos {mil} produtos custando mais de 1000R$')
print(f'O produt0 mais barato é {barato} de {menor:.2f}R$\n')
