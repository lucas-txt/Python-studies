from datetime import date
contador_jovem = 0
contador_idoso = 0
for idades in range(1, 8):
    nascimento = int(input('Em que ano a {}° pessoa nasceu?'.format(idades)))
    ano = date.today().year 
    if nascimento + 18 >= ano:
        contador_jovem += 1
    else:
        contador_idoso += 1
print('{} pessoas são de maior idade e {} são de menor.'.format(contador_idoso, contador_jovem))
