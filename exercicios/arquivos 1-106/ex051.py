print(20*'==')
print('10 TERMOS DE UMA PROGREÇÃO ARITIMETICA')
print(20*'==')
i = int(input('Primeiro termo: ')) #inico
r = int(input('Razão: ')) #razão
for pa in range(1, 10):
    i += r
    print(i, end=' > ')
print('ACABOU')