galera = []
media = 0
while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ')

    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('[ERRO] Apenas F ou M. Tente novamente.')

    while True:
        pessoa['idade'] = int(input('Idade: '))
        if 3 < pessoa['idade'] < 99: 
            media += pessoa['idade']
            break
        print('[ERRO] Idade invalida. Tente novamente.')
    
    while True:
        escolha = input('Quer continuar? [S/N] ').upper()[0]
        if escolha in 'SN':
            break
        print('[ERRO] Escolha invalida. Tente novamente.')
    
    galera.append(pessoa)

    if escolha == 'N':
        break

print(10*'-=-')
print(f'A) Ao todo temos {len(galera)} cadastradas')

media = media/len(galera)
print(f'B) A media de idade é {media:.2f} anos.')

print('C) As mulheres cadastradas foram ', end='')
for c in galera:
    if c['sexo'] == 'F':
        print(c['nome'], end=' ')

print('\nD) Lista de pessoas que estão acima da media: ')
for c in galera:
    if c['idade'] > media:
        print('     ', end='')
        for k, v in c.items():
            print(f' {k} = {v}; ', end='')
        print()

print('<<<-- ENCERRADO -->>>')
