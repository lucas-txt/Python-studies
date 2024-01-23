from biblioteca.arquivo import *
from biblioteca.interface import *
from time import sleep  

arq = r'C:\Users\lucas\OneDrive\Documentos\coisas-de-programacao\curso-em-video\python\exercicios\pastas 107 - 115\ex115\biblioteca\arquivo\cadastros.txt'

if not ArquivoExiste(arq):
    CriarArquivo(arq)


pessoas = []
while True:
    escolha = menu('Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'sair do sistema')

    if escolha == 1:
        titulo('OPÇÃO 1')
        for c in pessoas:
            print(f'{c[0]}:   {c[1]:<10}')
        LerArquivo(arq)
        
    elif escolha == 2:
        titulo('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = int(input(('Idade: ')))
        cadastrar(arq, nome, idade)
    elif escolha ==3:
        titulo('FIM!!!')
        break
    sleep(0.6)
