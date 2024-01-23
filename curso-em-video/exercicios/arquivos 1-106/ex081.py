numeros = []
cinco = ' não '
while True:
    numeros.append(int(input('Digite um valor: ')))
    esc = input('Quer continuar? [S/N] ')
    if 5 in numeros:
        cinco = ' '
    if esc in 'Nn':
        break
print(f'Você digitou {len(numeros)} elementos')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
print(f'O valor 5{cinco}faz parte da lista ')
