#  Faça um algoritmo que diga o novo salário de um funcionário sabendo que foi aumentado em 15% #

print('{:=^40}'.format(' I N I C I O '))
nome = input('Qual o nome do funcionário: ')
sala = float(input('Qual o salário atual de ' + nome + ": "))
resp = input('Você quer abaixar [ab] o salário ou aumentar [au] o salário: ')
if resp == 'au':
    aum = float(input('Qual o aumento que vc vai dar: '))
    nsala = sala + aum
    print('O novo salário será de {:.f2} Reais'.format(nsala))
    print('')
    print('{:=^40}'.format(' F I N A L '))
elif resp == 'ab':
    aba = float(input('Qual o valor que vc vai tirar: '))
    nsala = sala - aba
    print('O novo salário será de {:.f2} Reais'.format(nsala))
    print('{:=^40}'.format(' F I N A L '))
else:
    print('... ERROR, YOU PROBABLY DIGITED IT WRONG ...')
    print('{:=^40}'.format(' F I N A L '))
