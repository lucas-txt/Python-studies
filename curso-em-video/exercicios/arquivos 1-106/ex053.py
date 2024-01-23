frase = input('Digite uma frase: ').lower().strip()
palavras = frase.split() 
junto = ''.join(palavras)

inverso = junto[::-1]  ###FORMA MAIS PRATICA E EFICIENTE###

# inverso = ''
# for letra in range(len(junto)-1, -1, -1):   ###USADO APENAS PARA PRATICAR O FOR###  
#     inverso += junto[letra]

print('{} | {}'.format(junto, inverso))
if junto == inverso:
    print('Essa frase é um palindromo!')
else:
    print('Essa frase não é um palindromo')