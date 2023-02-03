from time import sleep
c = ('\033[m',   #0 - sem cor
     '\033[31m', #1 - vermelho
     '\033[32m', #2 - verde
     '\033[33m', #3 - amarelo
     '\033[37m', #4 - laranja
     '\033[36m', #5 - azul
     )

def ajuda(comando):
    return help(comando)

def titulo(msg, cor=0):
    msg = msg.upper().strip()
    print(c[cor], end='')
    print((len(msg)+4)*'~')
    print(f'  {msg}')
    print((len(msg)+4)*'~')
    print(c[0], end='')

while True:
    titulo('  SISTEMA DE AJUDA PyHELP', 2)

    fun = input('Função ou biblioteca >>> ').strip().lower()
    sleep(.3)
    if fun.upper() == 'FIM':
        titulo('  FIM DO PROGRAMA', 1)
        break

    titulo(f"  ACESSANDO O MANUAL DO COMANDO {fun}  ", 5)

    sleep(.7)
    print(c[1], end='')
    ajuda(fun)
    print(c[0], end='')

