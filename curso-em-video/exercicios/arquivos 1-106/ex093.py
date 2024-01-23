jogador = dict()

jogador['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

jogador['gols'] = []
for c in range(0, partidas):
    jogador['gols'].append(int(input(f'    -Quantos gols {jogador["nome"]} fez na {c+1}° partida? '))) 
    
jogador['total'] = sum(jogador['gols'])

print(10*'-=-')
print(jogador)

print(10*'-=-')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}') 

print(10*'-=-')
print(f'{jogador["nome"]} jogou {partidas}')
for p, v in enumerate(jogador['gols']):
    print(f'    => Na {p+1}° partida {jogador["nome"]} fez {v} gols')
print(f'Total de {jogador["total"]} gols')
