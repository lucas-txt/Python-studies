n = int(input('Digite um numero: '))
print('''
Analaisando o numero {}:
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}
'''.format(n, n//1%10, n//10%10, n//100%10, n//1000%10))