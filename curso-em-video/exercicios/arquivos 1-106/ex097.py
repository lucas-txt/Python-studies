def titulo(msg):
    print((len(msg)+4)*'=')
    print(f'  {msg}  ')
    print((len(msg)+4)*'=')

mensagem = input('O que você quer escrever? ')
titulo(mensagem)