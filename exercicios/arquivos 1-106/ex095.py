time = []
while True:
    jogador = {}
    
    jogador['nome'] = input('Nome do jogador: ')

    partidas = int(input(f'Quantas paridas {jogador["nome"]} jogou? '))

    jogador['gols'] = []
    jogador['total'] = 0
    for c in range(0, partidas):
        jogador['gols'].append(int(input(f'    -Quantos gols o {jogador["nome"]} fez na {c+1}° partida? ')))
            
    jogador['total'] = sum(jogador['gols'])
        
    time.append(jogador)

    while True:
        escolha = input('Quer continuar? [S/N]').upper().strip()[0]
        if escolha in 'SN':
            break
        print('[ERRO] Tente novamente')
    if escolha == 'N':
        break

print(14*'-=-')
print('Cod  Nome        Gols                Total')

print(42*'-')
for p, v in enumerate(time):
    print(f'{str(p+1):<3}  {str(v["nome"]):<10}  {str(v["gols"]):<18}  {str(v["total"]):<2}')
    
print(42*'-')
fim = 0
while True:
    while True:
        escolha = int(input('Mostrar dados de qual jogador? [999 para]'))-1
        if escolha == 998:
            fim = 1
            break
        if 0 <= escolha and escolha <= len(time):
            break
        print('[ERRO] Tente novamente')
    if fim == 1:
        break

    print(f' -- Levantamento do jogador {time[escolha]["nome"]}')
    for p, v in enumerate(time[escolha]['gols']):
        print(f'    No {p+1}° jogo fez {v} gols')
    print(42*'-')

print('<<<-- FIM -->>>')