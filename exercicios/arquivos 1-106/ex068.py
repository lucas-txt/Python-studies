from random import randint
print(10*'\033[33m-=-')
print('Vamos jogar par ou impar ')
print(10*'-=-')
vit = 0
EscJog = ' '
while True:
    NumJog = int(input('\033[36mDigite um valor: '))
    while EscJog not in 'IP':
        EscJog = input('Você quer par ou impar? [P/I] ').strip().upper()[0]
    NumCom = randint(1, 5)

    print(30*'\033[32m-')
    NumFim = NumJog + NumCom
    print(f'Você jogou {NumJog} e o computador {NumCom}, um total de {NumFim} ', end='')
    print('deu par.' if NumFim % 2 == 0 else 'deu impar.')
    print(30*'\033[32m-\033[m')

    if EscJog == 'P':
        if NumFim % 2 == 0:
            print('\033[33mjogador vence\033[m')
            vit += 1
        else:
            print('\033[33mComputador vence\033[m')
            break
    elif EscJog == 'I':
        if NumFim % 2 ==0:
            print('\033[33mComputador vence\033[m')
            break
        else:
            print('\033[33mjogador vence\033[m')
            vit += 1
    
    print('Vamos jogar de novo....')
    
if vit == 1:
    print(f'GAME OVER! Você venceu {vit} vez.')
else:
    print(f'GAME OVER! Você venceu {vit} vezes.')
