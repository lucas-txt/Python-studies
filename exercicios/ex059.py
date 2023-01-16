from time import sleep
n1 = int(input('\033[33mPrimeiro valor: \033[m'))
n2 = int(input('\033[33mSegundo valor: \033[m'))
escolha = 0
while escolha != 5:
    escolha = int(input('''\033[32m    [1] somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa
>>>>>> Qual a sua opção? \033[m'''))
    if escolha == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
        print(10*'\033[36m-=-\033[m')
    elif escolha == 2:
        print('O resultado de {} X {} é {}'.format(n1, n2, n1*n2))
        print(10*'\033[36m-=-\033[m')
    elif escolha == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
        print(10*'\033[36m-=-\033[m')
    elif escolha == 4:
        n2 = int(input('\033[33mDigite novamente o segundo valor: \033[m'))
        n1 = int(input('\033[33mDigite novamente o primeiro valor: \033[m'))
        print('Valores registrados')
        print(10*'\033[36m-=-\033[m')
    elif escolha != 5: 
        print('Numero invalido, tente novamente.')
        print(10*'\033[36m-=-\033[m')
print('Finalizando programa... ')
sleep(1.5)
print('\033[33mFim!!! Volte sempre.\033[m')
print(10*'\033[36m-=-\033[m')
