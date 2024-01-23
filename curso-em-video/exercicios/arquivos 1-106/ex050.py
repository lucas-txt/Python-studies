acumulador = 0
progrecao = 0
for soma in range(1, 7):
    n = int(input('Digite o {}° valor: '.format(soma)))
    if n % 2 == 0:
        acumulador += n 
        progrecao += 1
print('A soma dos {} valores pares que você digitou é: {}'.format(progrecao, acumulador))