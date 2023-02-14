import moeda

n = float(input('Digite o preço: R$'))
print(f'A metade de R${moeda.moeda(n)} é R${moeda.moeda(moeda.metade(n))}')
print(f'O dobro de R${moeda.moeda(n)} é R${moeda.moeda(moeda.dobro(n))}')
print(f'Aumentando 10% temos R${moeda.moeda(moeda.aumentar(n))}')