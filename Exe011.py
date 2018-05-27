#  Faça um algoritmo que calcule a area de uma parede e diga quantos litros de tinta serão necessários para pintá-la,
#  sabendo que 1 litro pinta 2 metros quadrados #

print('{:=^30}'.format(' INICIO '))
parede = float(input('Quantos metros essa parede tem: '))
litros = parede / 2
print('serão necessários {} litros...'.format(litros))
print('{:=^30}'.format(' FINAL '))
