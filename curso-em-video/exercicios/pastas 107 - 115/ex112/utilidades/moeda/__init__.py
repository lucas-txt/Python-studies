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


def linha():
    print(30*'-')

def resumo(n, a=10, r=10):
    linha()
    print('RESUMO DO VALOR'.center(30))
    linha()
    print(f'''Preço analizado:   {moeda(n)}
Dobro do preço:    {dobro(n, m=True)}
Metade do preço:   {metade(n, m=True)}
{a}% de aumento:    {aumentar(n, a, m=True)}
{r}% de redução:    {diminuir(n, r, m=True)}''')
    linha()