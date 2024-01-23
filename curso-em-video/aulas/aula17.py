lanches = ['hamburguer', 'suco', 'pizza', 'pudim']
# lanches[1] = 'refri'
# print(lanches)
# lanches.append('cockie')
# print(lanches)
# lanches.insert(3, 'cachorro quente')
# print(lanches)
# lanches.pop(-1)
# lanches.sort()
# print(lanches)

valores = []

# valores.append(5)
# valores.append(9)
# valores.append(4)
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}')
# print('fim')

# for cont in range(0, 5):
#     valores.append(input('Digite um valor: '))
# print(valores)

a = [2, 3, 4, 7]

# b = a sere para cirar uma ligação
b = a[:] # serve para copiar as listas 
b[2] = 8
print(f'lista A: {a}')
print(f'lista B: {b}')