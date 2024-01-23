def contador(i, f, p=1):
    """
    ->Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno 
    """

    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')

# contador(0, 10)
# contador(0, 10, 2)





def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

soma_um = somar(3, 7, 9)
soma_dois = somar(2, 8)
# print(f'A primeira soma é {soma_um} e asegunda soma é {soma_dois}')



def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

# n = int(input('Digite um numero para ver seu fatorial: '))
# print(f'O fatorial de {n} é igual a {fatorial(n)}')




def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um numero: '))
if par(num):
    print('É par!')
else:
    print('É impar!')