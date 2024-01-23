n1 = int(input('um valor:'))
n2 = int(input('outro valor:'))
s = n1 + n2
ss = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
rd = n1 % n2
e = n1 ** n2
print('''
A soma vale: {}
A subtração vale: {}
A multiplicação vale: {}
A divisão vale: {:.3f}
A divisão inteira vale: {}
O resto da divisão vale: {}
A esponeciação vale: {}
'''.format(s, ss, m, d, di, rd, e))