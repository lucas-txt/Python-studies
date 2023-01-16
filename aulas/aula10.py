# nome = input('Qual o seu nome? ').strip().lower()
# if nome == 'lucas':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tão normal')
# nome = nome.capitalize()
# print('Bom dia {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua media foi {:.1f}'.format(m))
print('PARABENS!' if m >= 7 else 'estude mais')
# if m >= 7:
#     print('Sua media foi boa! Parabens!')
# else:
#     print('Sua media foi ruim! Estude mais!')