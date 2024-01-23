from random import sample
p1 = input('Digite um nome: ')
p2 = input('Digite um segundo nome: ')
p3 = input('Digite um terceiro nome: ')
p4 = input('Digite um quarto nome: ')
p5 = input('Digite um quinto nome: ')
lista = [p1, p2, p3, p4, p5]
ordem = sample(lista, k=len(lista))
print('A ordem sorteada foi: {}'.format(ordem))