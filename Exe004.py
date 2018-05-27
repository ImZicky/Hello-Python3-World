#  Faca um algoritmo que funcione como um banco, ele te pergunta qual operação você quer fazer (Saque / Deposito /
# Conversão de Valores) e mostra na tela as respostas #

nome = str(input('Qual o seu nome? > '))
ordem = str(input('O que vc quer fazer? > '))


def title():
    print('----------------------------------------')
    print('         ', nome, '`s', ' Bank')
    print('----------------------------------------')


if (ordem == 'saque') or (ordem == 'saq') or (ordem == 'Saque') or (ordem == 'Saq'):
    title()
    n1 = float(input('Quanto vc tem no banco agora? > '))
    n2 = float(input('Quanto vc quer sacar? > '))
    if n1 > n2:
        restot = n1 - n2
        print('Você tem agora: {:.2f}'.format(restot))
    elif n1 < n2:
        restot = n2 - n1
        print('Você deve: {:.2f}'.format(restot))
    elif n1 == n2:
        print(nome, ' Você pegou tudo mesmo!?...')

if (ordem == 'deposito') or (ordem == 'dep') or (ordem == 'Deposito') or (ordem == 'Dep'):
    title()
    n1 = float(input('Quanto vc tem no banco agora? > '))
    n2 = float(input('Quanto vc quer depositar? > '))
    restot = (n1 + n2)
    print(nome, ' você agora tem R$ {:.2f}'.format(restot))

if (ordem == 'converter') or (ordem == 'conv') or (ordem == 'Converter') or (ordem == 'Conv'):
    title()
    print('Dollar, Euro, Libras ou Yuan')
    din = str(input('Qual unidade monetária? > '))
    if (din == 'dollar') or (din == 'Dollar') or (din == 'D') or (din == 'dollar'):
        uni = 3.30
        n1 = float(input('quantos dollares vc quer converter? > '))
        restot = n1 * uni
        print('São: R$ {:.2f}'.format(restot))

    elif (din == 'Euro') or (din == 'e') or (din == 'euro'):
        uni = 3.80
        n1 = float(input('quantos euros vc quer converter? > '))
        restot = n1 * uni
        print('São: R$ {:.2f}'.format(restot))

    elif (din == 'Libra') or (din == 'l') or (din == 'libra'):
        uni = 4.40
        n1 = float(input('quantas libras vc quer converter? > '))
        restot = n1 * uni
        print('São: R$ {:.2f}'.format(restot))

    elif (din == 'Yuan') or (din == 'y') or (din == 'yuan'):
        uni = 0.50
        n1 = float(input('quantos Yuans vc quer converter? > '))
        restot = n1 * uni
        print('São: R$ {:.2f}'.format(restot))
