def verificar(nascimento):
    from datetime import date


    ano = date.today().year
    idade = ano - nascimento
    if idade <= 15:
        msg = 'NÃO VOTA'
    elif idade <= 17:
        msg = 'VOTO OPICIONAL'
    elif idade <= 65:
        msg = 'VOTO OBRIGATORIO' 
    else:
        msg = 'VOTO OPICIONAL'
    return f'com {idade} anos: {msg}'
    

print(verificar(int(input('Em que ano você nasceu? '))))
