# Faca um algoritmo que calcule uma hipotenusa #

from math import hypot

print('{:+^50}'.format(' INICIO '))

cateto2 = float(input(' ### Qual o tamanho do cateto oposto: '))
cateto1 = float(input(' ### Qual o tamanho cateto Adjacente meu brotha: '))

hipo = hypot(cateto1, cateto2)

print('{}'.format('-')*50)
print()
print('O tamanho da hipotenusa é {:.2f}'.format(hipo))
print('{:+^50}'.format(' FIM '))
