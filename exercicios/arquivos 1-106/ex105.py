def notas(*num, sit=False):
    """
    -> Serve para analisar uma quantidade indefinidada de numeros e retornar o maior, menor e a media dos valores
        :param *num: recebe os numeros a serem considerados
        :param sit: decide se a situação deve ser incluida na resposta
    """
    
    notas = {}
    notas['total'] = len(num)
    notas['maior'] = max(num)
    notas['menor'] = min(num)
    notas['media'] = sum(num)/len(num)

    if sit:
        if notas['media'] >= 7:
            notas['situação'] = 'BOA'
        elif notas['media'] >= 5:
            notas['situação'] = 'MEDIANA'
        else:
            notas['situação'] = 'RUIM'
    return notas

resp = notas(5.5, 9.4, 10, sit=True)
print(resp)