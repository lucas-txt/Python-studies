a, b = 1, 5
print('Os valores são \033[7;32;41m{}\033[m e \033[7;32;41m{}\033[m'.format(a, b))
nome = 'lucas'
print('Óla, muito prazer em te conhecer, {}{}{}'.format('\033[0;33;47m', nome, '\033[m'))
cores = {'limpa':'\033[m',
         'ciano':'\033[36m'
         }
cor = 'ciano'
print('a cor selecionada foi {}{}{}'.format(cores['ciano'], cor, cores['limpa']))