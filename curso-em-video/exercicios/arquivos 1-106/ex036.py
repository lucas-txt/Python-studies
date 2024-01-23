val = float(input('Qual o valor da casa? ')) #valor 
sal = float(input('Qual o salario do comprador? ')) #salario
escolha = int(input('''Você quer medir o pagamento em meses ou anos?
[1]Meses
[2]Ano
'''))
if escolha == 1:
    mt = 'meses' #medidor tempo
elif escolha == 2:
    mt = 'anos' #medidor tempo
tem = int(input('Em quantos {} você quer pagar a casa? '.format(mt)))
if escolha == 2:
    tem = tem * 12
if val/tem > (sal/100)*30:
    print('as parcelas ficam com o valor de {:.2f}, então você não pode comprar essa casa.'.format(val/tem))
else:
    preco = val/tem
    print('Compra aprovada, as suas parecelas ficam no valor de {:.2f} por {}.'.format(preco, mt))
