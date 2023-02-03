from random import choice
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do sehundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
a5 = input('Digite o nome do quinto aluno: ')
alunos = [a1, a2, a3, a4, a5]
print('O aluno escolhido foi: {}'.format(choice(alunos)))