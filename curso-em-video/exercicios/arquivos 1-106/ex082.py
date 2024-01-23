numeros = []
par = []
imp = []

while True:
    numeros.append(int(input('Digite um numero: ')))
    esc = input('Quer continuar? ').strip()[0]
    if esc in 'Nn':
        break

for contagem, valor in enumerate(numeros):
    if valor % 2 == 0:
        par.append(valor)
for contagem, valor in enumerate(numeros):
    if valor % 2 != 0:
        imp.append(valor)

print(20*'-+-')
print(f'A lista completa {numeros}')
print(f'A lista de pares {par}')
print(f'A lista de impares {imp}')


