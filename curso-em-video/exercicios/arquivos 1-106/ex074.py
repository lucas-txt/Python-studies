from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {numeros[0]} {numeros[1]} {numeros[2]} {numeros[3]} {numeros[4]}')
print(f'O maior valor sorteado é {max(numeros)}')
print(f'O menor valor sorteado é {min(numeros)}')
