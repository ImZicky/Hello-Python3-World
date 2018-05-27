#  Faça um algoritmo que diga a tabuada de todos os numeros de 1 a 10#

cont1 = 1
cont2 = 1
print('{:=^20}'.format(' INÍCIO '))
while cont2 <= 10:
    print(f'Tabuada do {cont2}')
    while cont1 <= 10:
        r = cont2 * cont1
        print('{} x {} = {}'.format(cont2, cont1, r))
        cont1 += 1
    cont2 += 1
    cont1 = 1
    print('-------------')
print('{:=^20}'.format(' FIM '))
