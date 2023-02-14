import moeda

n = float(input('Digite o preço: R$'))
print(f'A metade de R${n} é R${moeda.metade(n)}')
print(f'O dobro de R${n} é R${moeda.dobro(n)}')
print(f'Aumentando 10% temos R${moeda.aumentar(n)}')