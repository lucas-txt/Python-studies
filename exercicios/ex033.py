n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('terceiro valor: '))

menor = n3
if n1 < n2 and n3:
    menor = n1
if n2 < n3 and n1:
    menor = n2
print('O menor valor é {}'.format(menor))

maior = n3
if n1 > n2 and n3:
    maior = n1
if n2 > n1 and n3:
    maior = n2
print('O maior valor é {}'.format(maior))
