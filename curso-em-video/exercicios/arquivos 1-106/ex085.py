numeros = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        numeros[1].append(n)
    else:
        numeros[0].append(n)
numeros[1].sort()
numeros[0].sort()
print(f'Os valores pares digitados foram: {numeros[1]}') 
print(f'Os valores impares digitados foram: {numeros[0]}') 
