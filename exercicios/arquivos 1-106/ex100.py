from random import randint
from time import sleep

def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end=' ')
    for c in range(0, 5):
        lista.append(randint(1, 9))
        print(lista[c], end=' ', flush=True)
        sleep(0.2)
    print('FIM')    

def SomaPar(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero 
    return soma

numeros = []
sorteio(numeros)
print(SomaPar(numeros))