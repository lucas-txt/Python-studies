from random import randint
from time import sleep
from operator import itemgetter
jogos = {
    'jogador-1':randint(1, 6),
    'jogador-2':randint(1, 6),
    'jogador-3':randint(1, 6),
    'jogador-4':randint(1, 6),
}
ranking = []
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('Valores sorteados: ')

for k, v in jogos.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.8)
print(10*'-=-')
print('Ranking dos jogadores')
for p, v in enumerate(ranking):
    print(f'{p+1}° lugar: {v[0]} com {v[1]} pontos')

