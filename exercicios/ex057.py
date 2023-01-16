s = input('Qual o seu sexo? [M\F] ').upper().strip()[0]
while s not in 'M F':
    s = input('Qual o seu sexo? [M\F] ').upper().strip()[0]
print('Sexo {} registrado com sucesso.'.format(s))