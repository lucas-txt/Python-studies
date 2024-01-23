from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjecente: '))
print('A hipotenusa do seu triangulo é {:3.4f}'.format(hypot(co, ca)))