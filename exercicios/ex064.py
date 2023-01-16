n, c, soma = 0, 0, 0
n = int(input('Digite um numero [999 para parar]: '))
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um numero [999 para parar]: '))
print('Você digitou {} numeros e a soma deles é {}.'.format(c, soma))
