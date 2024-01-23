from random import randint
from time import sleep
print(29*'-=-x') 
print('Estou pensando em um numero ente 0 e 5, tente adivinhar.')
print(29*'-=-x')
nu = int(input('Em que numero o computador pensou? ')) #Numero Usuario
nc = randint(0, 5) #Numero Computador
print('PROCESSANDO...')
sleep(1)
if nu == nc: 
    print('Você acertou, parabens!!!')
else: 
    print('Eu pensei no {}, você errou, tente de novo.'.format(nc))
