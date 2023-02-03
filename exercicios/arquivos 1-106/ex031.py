distancia = float(input('Qual a distância da sua viagem?'))
if distancia <= 200:
    print('O valor da sua viagem é de R${:.2f}'.format(distancia * 0.5))
else:
    print('O valor da sua viagem é de R${:.2f}'.format(distancia * 0.45))
