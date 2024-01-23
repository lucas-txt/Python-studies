from unidecode import unidecode
while True:
    while True:
        escolha = int(input('''Oque você quer saber?\033[33m
    [1]Lista do brasileirão
    [2]Os 5 primeiros times do brasileirão
    [3]Os 5 ultimos times do brasileirão
    [4]Times em ordem alfabética
    [5]Em que posição esta o seu time 
    [6]Finalizar programa\033[m
Sua escolha: '''))
        if 1 <= escolha <= 6:
            break
        print('[ERRO]Tente novamente.')

    times = ('corinthians','palmeiras','santos','gremio',
        'cruzeiro','flamengo','vasco','chapecoense',
        'atlético','botafogo','atletico-pr','bahia',
        'sao Paulo','fluminense','sport recife','ec vitoria',
        'curitiba','avai','ponte preta','atletico-go')

    if escolha == 1:
        print('Lista do brasileirão')
        for c in range(0, len(times)):
            if c % 2 == 0:
                print(f'''  {c+1}°\033[36m{times[c]}\033[m''')
            else:
                print(f'''  {c+1}°\033[31m{times[c]}\033[m''')
    elif escolha == 2:
        for c in range(0, 5):
            print(f'''  O {c+1}° time do brasileirão é o {times[c]}''')
    elif escolha == 3:
        for c in range(15, 20):
            print(f'''  O {c+1}° time é {times[c]}''')
    elif escolha == 4:
        print(f'\033[36m{sorted(times)}\033[m')
    elif escolha == 5:
        time = unidecode(input('Qual o seu time? ')).lower().strip()
        print(f'\033[32mO {time} esta na {times.index(time)+1}° posição\033[m')
    elif escolha == 6:
        print('Fim do programa.')
        break
