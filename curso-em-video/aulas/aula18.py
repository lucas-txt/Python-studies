# teste = list()
# teste.append('gustavo')
# teste.append('40')
# galera = list()
# galera.append(teste[:])
# teste[0] = 'maria'
# teste[1] = '22'
# galera.append(teste[:])
# print(galera)



# galera = [['joão', 19], ['ana', 33], ['joaquim', 13], ['maria', 45]]
# for p in galera:
#     print(p[0])




galera = list()
dado = list()
tot_men = tot_mai = 0
for c in range(0, 5):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        tot_mai += 1
    else:
        print(f'{p[0]} é menor de idade')
        tot_men += 1

print(f'Temos {tot_mai} maiores de idade e {tot_men} menores de idade')