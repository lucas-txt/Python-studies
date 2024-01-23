v = float(input('Qual a velocidade atua do carro? '))
if v <= 80:
    print('Parabens, dirija com segurança e ', end = '')
else:
    print('O limite de velocidade é de 80km/h, voce foi multado em RS{:.2f}'.format((v - 80)*7))
print('tenha um bom dia.')
