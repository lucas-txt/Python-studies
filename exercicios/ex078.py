valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c+1}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if maior < valores[c]:
            maior = valores[c]
        if menor > valores[c]:
            menor = valores[c]

print(10*'-=-')
print(f'Você digitou os valores', end=' ')
for c, valor in enumerate(valores):
    print(valor, end=' ')
print(f'\nO maior valor digitado foi {maior} nas posições', end=' ')
for posição, valor in enumerate(valores):
    if valor == maior:
        print(posição+1, end='...')
print(f'\nO menor valor digitado foi {menor} nas posições', end=' ')
for posição, valor in enumerate(valores):
    if valor == menor:
        print(posição+1, end='...')