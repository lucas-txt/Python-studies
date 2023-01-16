n = int(input('Digite um numero para saber a sua tabuada: '))
for tabuada in range(1, 11):
    print('{} X {} = {}'.format(n, tabuada, n * tabuada))