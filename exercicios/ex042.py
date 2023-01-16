r1 = float(input('Digite o tamanho da primeira reta: ')) #reta um
r2 = float(input('Digite o tamanho da segunda reta: ')) #reta dois
r3 = float(input('Digite o tamanho da terceira reta: ')) #reta tres

maior = r1
m1 = r2 #medida um
m2 = r3 #medida dois
if r2 > r1 and r3:
    maior = r2
    m1 = r3
    m2 = r1
if r3 > r2 and r1:
    maior = r3
    m1 = r1
    m2 = r2
if r1 == r2 and r2 == r3:
    print('Essas retas formam um triangulo equilatero.')
elif r1 == r2 or r2 == r3 or r3 == r1:
    print('Essas retas formam um triangulo isóceles')
elif m1 + m2 > maior:
    print('Essas retas formam um triangulo escaleno')
else:
    print('Essas retas não formam um triangulo')