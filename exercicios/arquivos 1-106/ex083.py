frase = input('Digite sua espressão: ')
fim = contagem = 0
for valor in frase:
    if valor == '(':
        contagem += 1
    if valor == ')':
        contagem -= 1
    if contagem == -1:
        fim = 1
if fim == 1 or contagem != 0:
    print('Expreção invalida')
else:
    print('Expreção valida')


