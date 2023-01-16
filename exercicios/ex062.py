print('Gerador de Progreção Aritimetica')
print(10*'-=-')
pt = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))

l = 0 #laço
c = 1 #contador
ter = 1 #termos 
cont = 10 #contagem

while ter != 0:
    while c <= 10:
        print('{} >'.format(pt), end=' ')
        pt += raz
        c += 1
    print('PAUSA')

    ter = int(input('Quantos termos você quer mostrar a mais? ')) #termos
    cont += ter #contagem

    for co in range(1, ter+1):
        print('{} >'.format(pt), end=' ')
        pt += raz

print('Fim do programa, você vizualizou {} termos.'.format(cont))
