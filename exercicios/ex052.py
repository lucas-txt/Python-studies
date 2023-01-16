n = int(input('Digite um numero: '))
total = 0
for numero in range(1, n+1):
    if n % numero == 0: 
        print('\033[36m {} \033[m'.format(numero), end=' ')
        total += 1
    else:
        print('\033[31m {} \033[m'.format(numero), end=' ')
if total == 2:
    print('\n O numero {} é primo pois só é divisivel por 1 e por ele mesmo'.format(n))
else:
    print('O numero {} não é primo pois é divisivel por mais de 2 numeros'.format(n))