from time import sleep

def linha():
    print(10*'-=-')

def contagem(i, f, p):
    for c in range(i, f, p):
        print(c, end=' ', flush=True)
        sleep(0.4)
    print('FIM')

linha()
print('Contagem de 1 até 10 de 1 em 1: ')
contagem(1, 11, 1)
linha()

print('Contagem de 10 até 0 de 2 em 2')
contagem(10, -2, -2)
linha()

print('Agora é sua vez de personalizar a contagem: ')
inicio = int(input('Inico: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
linha()

print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
contagem(inicio, fim, passo)
