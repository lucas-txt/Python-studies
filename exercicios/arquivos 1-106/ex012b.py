v = float(input('Digite o valor de um produto:'))
d = float(input('Digite o desconto do produto:'))
print('O produto de R${:.2f} com o desconto de {:.0f}% custara R${:.2f}'.format(v, d, (v/100)*(100-d)))