def titulo(mensagem):
    print(30*'-')
    print(mensagem)
    print(30*'-')

# titulo('CURSO EM VIDEO')





def soma(a, b):
    soma = a + b
    print(soma)
# def soma(a, b):
#     print(f'A = {a} B = {b}')
#     soma = a + b
#     print(f'A soma de A + B é igual a {soma}')

# soma(2, 8)
# soma(b=2, a=8)



def contador(*num):
    total = len(num)
    soma = 0
    for c in num:
        soma += c
    print(f'Total: {total} | Soma: {soma}')

# contador(1, 3, 7, 9)
# contador(1, 5)
# contador(1, 9, 5)





def dobra(lista):
    cont = 0
    while cont < len(lista):
        lista[cont] *= 2
        cont +=1

        
valores = [3, 5, 1, 8]
dobra(valores)
# print(valores)