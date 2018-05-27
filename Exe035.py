#  Diga se é possivel formar um triangulo ou não a partir dos 3 angulos de um triangulo x #


def inicio():
    cont = 1
    angs = []
    for i in range(0, 3):
        ang = float(input('Diga o angulo do {}º lado: '.format(cont)))
        angs.append(ang)
        cont = cont + 1
    return angs


def analisador_de_tri():
    if (angs[0] < (angs[1] + angs[2])) and (angs[1] < (angs[0] + angs[2])) and (angs[2] < (angs[0] + angs[1])):
        print('É POSSIVEL FAZER UM TRIANGULO!')
    elif (angs[0] == 0) and (angs[1] == 0) and (angs[2] == 0):
        print('VAI TOMAR NO KU SEU USUÁRIO DE MERDA')
    else:
        print('nope, n vai dar nao...')


angs = inicio()

analisador_de_tri()
