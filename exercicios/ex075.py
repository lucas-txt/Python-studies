numeros = (int(input('Digite um numero: ')),
        int(input('Digite outro numero: ')),
        int(input('Digite outro numero: ')),
        int(input('Digite outro numero: ')))
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 aparece na {numeros.index(3)+1}° posição')
else:
    print('O numero tres não foi digitado')
print('Os valores pares dsigitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
 