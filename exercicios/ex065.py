resposta = 'S '
soma, c, maior, menor = 0, 0, 0, 0
while resposta != 'N':
    n = int(input('Digite um numero: '))
    soma += n
    if c == 1:
        maior = menor = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n

    resposta = input('\033[33mQuer continuar? [\033[32ms\033[33m/\033[31mn\033[33m\033[33m]\033[m').upper().strip()[0]
    c += 1
    
print('Você digitou {} numeros e a media deles é {:.2f}'.format(c, soma/c))
print('O maior numero foi {} e o menor {}'.format(maior, menor))