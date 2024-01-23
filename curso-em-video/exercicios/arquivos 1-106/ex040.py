n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
nota = (n1+n2+n3)/3
if nota < 5:
    print('Com a media {} o aluno esta \033[31m REPROVADO\033[m'.format(nota))
elif nota < 7:
    print('Com a nota {} o aluno esta de \033[34mRECUPERAÇÂO \033[m'.format(nota))
elif nota <9.5:
    print('Com a nota {} o aluno esta \033[32mAPROVADO\033[m'.format(nota))
else:
    print('Com a nota {} o aluno esta \033[36mAPROVADO COM HONRA\033[m'.format(nota))