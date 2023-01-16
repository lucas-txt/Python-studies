print(10*'\033[36m-=-')
print('Banco')
print(10*'\033[36m-=-\033[m')
valor = int(input('Qual valor você quer sacar? R$'))
nota_1 = nota_10 = nota_20 = nota_50 = 0
while valor > 0:
    if valor >= 50:
        valor -= 50
        nota_50 += 1
    elif valor >= 20:
        valor -= 20
        nota_20 += 1
    elif valor >= 10:
        valor -= 10
        nota_10 += 1
    else:
        valor -= 1
        nota_1 += 1
if nota_50 > 0: print(f'total de {nota_50} cedulas de 50R$') if nota_50 > 1 else print(f'total de {nota_50} cedula de 50R$')
if nota_20 > 0: print(f'total de {nota_20} cedulas de 20R$') if nota_20 > 1 else print(f'total de {nota_20} cedula de 20R$')
if nota_10 > 0: print(f'total de {nota_10} cedulas de 10R$') if nota_10 > 1 else print(f'total de {nota_10} cedula de 20R$')
if nota_1 > 0: print(f'total de {nota_1} cedulas de 1R$') if nota_1 > 1 else print(f'total de {nota_1} cedula de 1R$')
for c in range(0, 5):
    print(c)