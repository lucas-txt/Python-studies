n = int(input('Digite um numero para calcular seu fatorial: '))
print('\033[32mCalculando {}! ='.format(n), end=' ')
resultado = 1
while n != 0:
    if n == 1:
        print('\033[32m{} = {}\033[m'.format(n, resultado), end=' ')
    else:
        print('\033[32m{} X\033[m'.format(n), end=' ')
    resultado *= n
    n -= 1 