from datetime import date
ano = date.today().year
an = int(input('Em que ano você nasceu? ')) #ano de nascimento
if ano == 18:
    print('você tem que se alistar esse ano')
elif ano-an > 18:
    print('Quem nasceu em {} tem {} anos'.format(ano, ano-an))
    print('Você ja deveria ter se alistado a {}'.format(ano-(an+18)))
    print('Seu alistamento foi em {} '.format(an+18))
elif ano-an < 18:
    print('Quem nsaceu em babab {} tem {} anos'.format(ano, ano-an))
    print('Ainda faltam {} anos para o seu alistamento'.format((an+18)-ano))
    print('Seu alistamento será em {}'.format(an+18))
elif an > ano or an < 1910:
    print('ano invalido')

