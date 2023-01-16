nome = str(input('qual é o seu nome? ')).title()
if nome == 'Lucas':
    print('que nome bonito')
elif nome == 'Pedro' or nome == 'maria' or nome == 'paulo':
    print('que nome comun')
elif nome in 'Ana Claudia Jessica Amanda':
    print('belo nome feminino')
else:
    print('seu nome é tão normal')
print('tenha um bom dia {} '.format(nome))