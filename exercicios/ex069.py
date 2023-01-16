c_mulher = c_homem = c_idade = 0
while True:
    print(30*'\033[31m-')
    print('CADASTRE UMA PESSOA')
    print(30*'\033[31m-\033[m')
    escolha = sexo = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N]').strip().upper()[0]

    if idade >= 18:
        c_idade += 1
    if sexo == 'M':
        c_homem += 1
    if sexo == 'F':
        if idade < 20:
            c_mulher += 1 

    if escolha == 'N':
        break

print('\033[36mDADOS-------------------------\033[m')

print(f'Total de pessoas com mais de 18 anos: {c_idade}')
print(f'Total de homens cadastrados: {c_homem}')
print(f'Total demulheres com menos de 20 anos: {c_mulher}\n')
