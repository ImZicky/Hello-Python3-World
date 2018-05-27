#  Faça um algoritmo que determine se um ano x é bissexto ou não #


def intro():
    ano = int(input('Diga um ano ai meu velho: '))
    return ano


def calculobi(a):
    if a % 4 == 0:
        print('O ano é bisexto!')
    elif (a % 100 == 0) and (a % 400 != 0):
        print('O ano não é bisexto')
    else:
        print('O ano não é bisexto')


anus = intro()

calculobi(anus)
