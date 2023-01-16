i = int(input('Digite o incio da contagem: '))
f = int(input('Digite o fibal da contagem: '))
s = 0#soma
c = 0#contagem
for progrecao in range(i, f+1):
    if progrecao % 2 == 1 and progrecao % 3 == 0: 
        s += progrecao
        c += 1
print('A soma de todos os {} numeros impares multiplos de tres entre {} e {}, é {}'.format(c, i, f, s))