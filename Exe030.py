#  Crie um algoritmo que leia a vel de um carro e multe-o em 7 reais a cada Kilometro passado de 80 #

vel = float(input('Qual a velocidade do seu carro meu velho? > '))
velcerta = 80

if vel > 80:
    print('Que veloz, agora irei multa-lo com 7 reais pra cada quilometro a mais')
    multa = vel - velcerta
    multot = multa * 7
    print('vc vai ter que pagar pra o governo R${:.2f}'.format(multot))
else:
    print('Muito bem, continue sendo um bom motorista...')
