aluno = {}
aluno['nome'] = input('Nome: ') 
aluno['media'] = float(input('Media: '))
print(10*'-=-')
for k, v in aluno.items():
    print(f'    --{k} é igual a {v}')

if aluno['media'] >= 7:
    print(f'    --Situação é igual a aprovado')
elif aluno['media'] >= 5:
    print(f'    --Situação é igual a recuperação')
else:
    print(f'    --Situação é igual a reprovado')
