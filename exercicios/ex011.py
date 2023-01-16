altura = float(input('Digite a altura da parede:'))
largura = float(input('Digite a largura da parede:'))
print('Com as dimenções {} x {}, sua parede tem {}m². Para pintar essa parede você vai precisar de {}L de tinta'.format(altura, largura, altura*largura, (altura*largura)/2))