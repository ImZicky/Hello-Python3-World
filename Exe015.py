#  Faca um algoritmo que calcule o preco de locacao de um carro baseado no preco por km e por dia de locação #

print('{:=^30}'.format(' INICIO '))
print('')
km = float(input('Quantos km vc rodou: '))
dia = int(input('Quantos dias vc ficou com o carro: '))
pref = (km * 0.15) + (dia * 60)
print('')
print('You must pay R${:.2f}'.format(pref))
print('{:=^30}'.format(' FINAL '))
