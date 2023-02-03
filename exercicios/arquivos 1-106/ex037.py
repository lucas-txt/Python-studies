num = int(input('Digite um numero inteiro: '))
res = int(input('''Escolha uma das bases para converção:
[1]binario
[2]octal
[3]hexadecimal
Sua escolha: 
'''))
if res == 1:
    print('{} covertido para binario é igual a {} '.format(num, bin(num)[2:]))
elif res == 2:
    print('{} covertido para octal é igual a {} '.format(num, oct(num)[2:]))
elif res == 3:
    print('{} covertido para hexadecimal é igual a {} '.format(num, hex(num)[2:]))
else:
    print('Opção invalida')