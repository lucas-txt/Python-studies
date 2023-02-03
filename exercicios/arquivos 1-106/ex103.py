def jogador(nome=None, gols=0):
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0  
    if not nome.strip().isalpha():
        nome = '<desconhecido>'
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'
    

nome = input('O nome do jogador: ')
gols = input('Número de gols: ')
print(jogador(nome, gols))