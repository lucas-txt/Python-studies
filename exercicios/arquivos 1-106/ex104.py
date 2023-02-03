def LeiaInt(msg):
    while True:
        n = input(msg).strip()
        if n.isnumeric():
            return int(n) 
        print('\033[31m[ERRO] Tente novamente.\033[m')


n = LeiaInt('Digite um numero: ')
print(f'Você digitou o numero {n}')