try:
    a = int(input('N1: '))
    b = int(input('N2: '))
    r = a/b
except (ValueError, TypeError):
    print(f'Tivemos um problema com o tipo de dado que você digitou')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados')
except Exception as erro:
    print(f'[ERRO] O erro encontrado foi {erro.__cause__}')
else: 
    print(f'Resultado: {r}')
finally:
    print('Volte sempre')