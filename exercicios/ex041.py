from datetime import date
ano = date.today().year
an = int(input('Em que ano você nasceu?')) #ano de nascimento
idade = ano-an
print('atleta de {} anos'.format(idade))
if idade < 10:
    print('clacificação: \033[36mMIRIN\033[m')
elif idade < 15:
    print('clacificação: \033[32mINFANTIL\033[m')
elif idade < 20:
    print('clacificação: \033[34mJUNIOR\033[m')
elif idade < 26:
    print('clacificação: \033[31mSÊNIOR\033[m')
else:
    print('clacificação: \033[35mMASTER\033[m')