peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso/altura**2
if imc <= 18.5:
    print('Seu imc esta em {:.1f}, você esta abaixo do peso.'.format(imc))
elif imc <= 25:
    print('Seu imc esta em {:.1f}, isso é o ideal.'.format(imc))
elif imc <= 30:
    print('Seu imc esta em {:.1f}, você esta com sobre peso.'.format(imc))
elif imc <= 40:
    print('Seu imc esta em {:.1f}, Você esta com obesidade.'.format(imc))
else:
    print('Seu imc esta em {:.1f}, você esta com obesidade morbida.'.format(imc))
