r1 = float(input('Tamanho da primeira reta: '))#reta um
r2 = float(input('Tamanho da segunda reta: '))#reta dois
r3 = float(input('Tamanho da terceira reta: '))#reta tres
maior = r1
s1 = r2 #segmento um
s2 = r3 #segmento dois
if r2 > r1 and r3:
    maior = r2
    s1 = r1 #segmento um
    s2 = r3 #segmento dois
if r3 > r1 and r2:
    maior = r3
    s1 = r1 #segmento um
    s2 = r2 #segmento dois
if s1 + s2 > maior:
    print('Com as retas, {:.2f}, {:.2f}, {:.2f}, é possivel fazer um triangulo.'.format(maior, s1, s2))
else:
    print('Com as retas, {:.2f}, {:.2f}, {:.2f}, não é possivel fazer um triangulo.'.format(maior, s1, s2))