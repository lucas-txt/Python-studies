frase = input('Digite uma frase: ').strip().lower()
print('A sua frase tem {} letras A'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(1+frase.find('a')))
print('A ultima letra A apareceu na posição {}'.format(1+frase.rfind('a')))
