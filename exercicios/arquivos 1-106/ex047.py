i = int(input('Começo da contagem: '))
f = int(input('Final da contagem: '))
if i % 2 != 0:
    i += 1
print('Numeros pares da sua sequencia: ')
for contagem in range(i, f+1, 2):  
        print(contagem, end = ' ')
