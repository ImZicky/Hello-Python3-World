#  Crie um algoritmno que cobre imposto sobre a viagem, se a viagem tem menos que 200km = 0,50 reias por km, se maior
#  que isso = 0,45 por km #


def intro():
    kmv = float(input('Qual a distancia da viagem em km: '))
    return kmv


def calculatax(a):
    tax = 200
    if a <= tax:
        b = a * 0.50
        return b
    else:
        b = a - tax
        c = b * 0.45
        return c


km = intro()

resul = calculatax(km)

print('Voce terá que pagar de passagem R${:.2f}'.format(resul))
