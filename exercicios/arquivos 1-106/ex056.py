media_idade = 0
idade_masc = 0
cont_fem = 0
nome_masc = ''

for dados in range(1, 6):
    print('----- {}° PESSOA -----'.format(dados)) #para decoração

#para coletar os dados
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()

#para a media de idade
    media_idade += idade 

#para descobrir qual o homen mais velho e coletar seu nome
    if sexo == 'M' or 'MASCULINO' and (idade_masc < idade or dados == 1): 
        idade_masc = idade
        nome_masc = nome

#para descobrir quantas mulheres tem menos de 20 anos
    if sexo == 'F' or 'FEMININO': 
        if idade < 20:
            cont_fem += 1

#resultados
print('A media de idade do grupo é {:.0f}.'.format(media_idade/5))
print('O homen mais velho do grupo tem {} anos e se chama {}.'.format(idade_masc, nome_masc))
print('Ao todo são {} mulheres com menos de 20 anos no grupo.'.format(cont_fem))
