from random import randint
from time import sleep

jogos = []

print(10*'\033[33m-=-\033[m')
print('Joga na mega sena')
print(10*'\033[33m-=-\033[m')

quant = int(input('Quantos jogos você quer que eu sortei? '))
print(f'\033[33m-=-=-=-SOERTEANDO {quant} JOGOS-=-=-=-\033[m')

for c in range(0, quant):
    cont = 0
    lista = []
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])

    sleep(0.8)
    print(f'Jogo {c+1}: numeros sorteados foram {lista}')
sleep(0.8)
print('\033[33m-=-=-=-=- <BOA SORTE> -=-=-=-=-\033[m')


