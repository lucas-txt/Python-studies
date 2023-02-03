while True:
    print(40*'=')
    n = int(input('Quer ver a tabuada de qual valor? '))
    print(40*'=')
    if n < 0:
        break
    for c in range(1, 11):
        if c == 10:
            print(f'{n}  X {c} = {n*c}')
        else:
            print(f'{n}  X  {c} = {n*c}')
print('\033[32mPrograma finalizado\033[m')