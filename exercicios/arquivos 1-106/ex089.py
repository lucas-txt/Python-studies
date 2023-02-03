turma = []

while True:
    escolha = ' '

    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    n3 = float(input('Nota 3: '))
    media = (n1+n2+n3)/3

    turma.append([nome, [n1, n2, n3], media])

    while escolha not in 'sn':
        escolha = input('Quer continuar? [S/N]').lower().strip()[0]
    if escolha == 'n':
        break

print(10*'-=-')
print('No. Nome        Média')
print('------------------------')
for c in range(0, len(turma)):
    print(f'{c+1:<4}', end='')
    print(f'{turma[c][0]:<12}', end='')
    if turma[c][2] >= 9.5:
        print(f'\033[36m{turma[c][2]:.2f}\033[m')
    elif turma[c][2] >= 7:
        print(f'\033[32m{turma[c][2]:.2f}\033[m')
    elif turma[c][2] >= 5:
        print(f'\033[34m{turma[c][2]:.2f}\033[m')
    else:
        print(f'\033[31m{turma[c][2]:.2f}\033[m')
print('------------------------')

while True:
    boletim = int(input('Digite o numero do aluno para ver o boletim [999 para]: '))
    if boletim == 999:
        break

    print(f'As notas do {turma[boletim-1][0]} são')
    for c in range(0, len(turma[boletim-1][1])):
        if turma[boletim-1][1][c] > 9.5:
            print(f'    \033[36mNota {c+1}: {turma[boletim-1][1][c]}\033[m')
        elif turma[boletim-1][1][c] > 7:
            print(f'    \033[32mNota {c+1}: {turma[boletim-1][1][c]}\033[m')
        elif turma[boletim-1][1][c] > 5:
            print(f'    \033[34mNota {c+1}: {turma[boletim-1][1][c]}\033[m')
        else:
            print(f'    \033[31mNota {c+1}: {turma[boletim-1][1][c]}\033[m')
print('<<<---FIM--->>>')
