marc_menor = 0
marc_maior = 0
for pesos in range (1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(pesos)))
    if pesos == 1:
        marc_menor = peso
        marc_maior = peso
    else:
        if marc_menor > peso:
            marc_menor = peso
        if marc_maior < peso:
            marc_maior = peso
print('A pessoa com maior peso tem {}KG'.format(marc_maior))
print('A pessoa com menor peso tem {}KG'.format(marc_menor))
