def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um numero
    :param numero: O numero a ser calculado
    :param show: (opicional) decide se o calculo vai ser mostrado ou não
    :return: o fatorial de 'numero'
    """
    
    
    total = 1
    if show == True:
        for c in range(numero, 0, -1):
            if c == 1:
                print(c, end=' = ')
            else:
                print(c, end=' X ')
            total *= c
    else:
        for c in range(numero, 0, -1):
            total *= c
        
    return total



print(30 *'-')
print(fatorial(5, show=False))