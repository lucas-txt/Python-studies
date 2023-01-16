from random import randint
numero = randint(1, 10)
chute = int(input('\033[31m Estou pensando em um numero de 1 a 10. Tente adivinhar... \033[m'))
tentativas = 1
while chute != numero:
    print('Você errou, tente novamente... ')
    if chute > numero:
        print('Eu pensei em um numero menor')
    else:
        print('Eu pensei em um numero maior')
    chute = int(input('\033[31mEstou pensando em um numero de 1 a 10. Tente adivinhar... \033[m'))
    tentativas += 1
if tentativas != 1:
    print('Você acertou com {} tentativas.'.format(tentativas))
else:
    print('Você acertou com {} tentativa.'.format(tentativas))
