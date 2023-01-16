from random import randint
from time import sleep
# jpc == jogada do pc
jpc = randint(1, 3)
# jpl == jogada player
jpl = int(input('''
Seuas opções:
\033[32m[1]Pedra
\033[35m[2]Papel
\033[34m[3]Tesoura\033[m
Qual a sua jogada? '''))

print('\033[33mPEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA\033[m')

if jpl == 1:
    print('Você: \033[32mpedra\033[m')
elif jpl == 2:
    print('Você: \033[35mpapel\033[m')
elif jpl == 3:
    print('Você: \033[34mtesoura\033[m')
else:
    print('Você: valor invalido')

if jpc == 1:
    print('Computador: \033[32mpedra\033[m')
elif jpc == 2:
    print('Computador: \033[35mpapel\033[m')
elif jpc == 3:
    print('Computador: \033[34mtesoura\033[m')

if jpl == 1:
    if jpc == 1:
        print('Resultado: empate')
    elif jpc == 2:
        print('Resultado: computador vence')
    elif jpc == 3:
        print('Resultado: você vence')
    else:
        print('Resultado: computador vence')
elif jpl == 2:
    if jpc == 1:
        print('Resultado: você vence')
    elif jpc == 2:
        print('Resultado: empate')
    elif jpc == 3:
        print('Resultado: computador vence')
    else:
        print('Resultado: computador vence')
elif jpl == 3:
    if jpc == 1:
        print('Resultado: computador vence')
    elif jpc == 2:
        print('Resultado: você vence')
    elif jpc == 3:
        print('Resultado: empate')
    else:
        print('Resultado: computador vence')
else:
    print('\033[31m[ERRO]\033[m')
