def metade(n, m=False):
    valor =  float(n)/2
    if m:
        return moeda(valor)
    return valor 


def dobro(n, m=False):
    valor = float(n)*2
    if m:
        return moeda(valor)
    return valor


def aumentar(n, p=10, m=False):
    valor = (n/100)*(100+p)
    if m:
        return moeda(valor)
    return valor

def diminuir(n, p=10, m=False):
    valor = (n/100)*(100-p)
    if m:
        return moeda(valor)
    return valor

def moeda(n):
    return f'R${n:.2f}'.replace('.',',')