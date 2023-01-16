# cont = 1
# while cont<= 10: #tambem pode receber true para rodar infinitamente 
#     print(cont, '->', end='')
#     cont += 1
# print('Acabou')

# n = s = 0
# while True:
#     n = int(input('Digite um numero: '))
#     if n == 999:
#         break
#     s += n
# # print('A soma vale {}'.format(s))
# print(f'A soma vale {s}')

nome = 'josé'
idade = 33
salario = 1000
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}')

# print('O %s tem %d anos' % (nome, idade)) # python 3.6+
# print('O {} tem {} anos'.format(nome, idade)) #python 3
# print(f'O {nome} tem {idade} anos') #python 2
