matriz = [[], [], []]
print('Matriz 3 x 3')
print(10*'-=-')

par = 0
for linha in range(0, 3):    
    for numero in range(0, 3):
        matriz[linha].append(int(input('Digite um valor: ')))
        if matriz[linha][numero] % 2 == 0:
            par += matriz[linha][numero]
print(10*'-=-')

print(f'\033[32m[  *  ]\033[31m[  1  ][  2  ][  3  ]\033[m')
for letra in range(0, len(matriz)):
    if letra == 0:
        print(f'\033[31m[  A  ]\033[m', end='')
    if letra == 1:
        print(f'\033[31m\n[  B  ]\033[m', end='')
    if letra == 2:
        print(f'\033[31m\n[  C  ]\033[m', end='')
    for c in range(0, 3):
        print(f'[{matriz[letra][c]:^5}]', end='')
print('\n-=-', 9*'-=-')

col_tres = matriz[0][1] + matriz[1][1] + matriz[2][1]

print(f'A soma dos numeros pares é {par}')
print(f'A soma dos numeros da terceira coluna é {col_tres}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
