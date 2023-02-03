n1 = float(input('Primeiro numero: '))
n2 = float(input('Segundo numero: '))
if n1 > n2:
    print('O \033[34mprimeiro\033[m numero é maior')
elif n2 > n1:
    print('O \033[34msegundo\033[m numero é maior')
else:
    print('Os \033[34mdois\033[m numeros são iguais')
