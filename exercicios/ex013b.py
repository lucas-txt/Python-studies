s = float(input('Digite seu salario:'))
a = float(input('Digite a porcentagem do seu aumento:'))
print('O salario R${:.2f} com um aumento de {:.0f}% vai ser R${:.2f}'.format(s, a, (s/100)*(100+a)))