print('Gerador de Progreção Aritimetica.')
print(10*'-=-')
pt = int(input('Primeiro termo: '))
razao = int(input('Razão da pa: '))
c = 0
while c <= 9:
    print('{} >'.format(pt), end=' ')
    pt += razao
    c += 1
print('FIM!')
