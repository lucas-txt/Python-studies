from datetime import datetime 

ctps = {}

ctps['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
ctps['sexo'] = input('Sexo [M/F]: ').upper()[0]
ctps['idade'] = datetime.now().year - nascimento 
ctps['ctps'] = int(input('Carteira de trabalho [0 se não tem]: '))
if ctps['ctps'] != 0:
    ctps['contratação'] = int(input('Ano de contratação: '))
    ctps['salario'] = float(input('Salario: R$'))
    if ctps == 'F':
        ctps['aposentadoria'] = ctps['contratação'] + 25 - nascimento
    else:
        ctps['aposentadoria'] = ctps['contratação'] + 30 - nascimento

print(10*'-=-')

for k, v in ctps.items():
    print(f'    --{k} tem o valor {v}')