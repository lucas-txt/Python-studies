s = float(input('Quanto você recebe?'))
if s > 1250:
    s = 110*(s/100)
    print('Você recebeu um aumento de salario de 10%, seu salario agora é de {:.2f}'.format(s))
else: 
    s = 115*(s/100)
    print('Você recebeu um aumento de slaario de 15%, seu salario agora é de {:.2f}'.format(s))