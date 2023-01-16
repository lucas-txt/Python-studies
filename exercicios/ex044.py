valor = float(input('Quanto foi gasto nas compras: '))
#fp == forma de pagamento
fp = int(input('''FORMAS DE PAGAMENTO
\033[36m[1] A vista no dinheiro
\033[32m[2] A vista no cartão
\033[33m[3] 2x no cartão
\033[31m[4] 3x ou mais no cartão\033[m
-------------------------
\033[35mForma de pagamento selecionada: \033[m'''))
if fp == 1:
    valor = (valor/100)*90
    print('Por ser a vista e no dinheiro você recebe desconto e as compras ficam no valor de R${:.2f}.'.format(valor))
elif fp == 2:
    valor = (valor/100)*95
    print('Por ser a vista você recebe desconto e as compras ficam no valor de R${:.2f}.'.format(valor))
elif fp == 3:
    parcela = valor/2
    print('Parcelando em duas vezes o valor é de R${:.2f} e as parcelas ficam a R${:.2f} cada.'.format(valor, parcela))
elif fp == 4:
    valor = (valor/100)*120
    qp = int(input('Em quantas vezes você quer parcelar? ')) #quantidade de parcelas
    parcela = valor/qp
    print('Parcelando em {} vezes, o valor das compras fica a {}, com cada parcela custando {}.'.format(qp, valor, parcela))
else:
    print('Opção invalida.')