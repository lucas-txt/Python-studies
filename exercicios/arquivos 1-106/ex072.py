numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 
    'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 
    'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um numero de 0 a 20: '))
    if 0 <= numero <= 20:
        break
    print('[ERRO]tente novamente. ', end='')
print(f'Voce digitou o numero {numeros[numero]}')
