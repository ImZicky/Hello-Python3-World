#  Faça um algoritmo que leia o preço de um produto e desconte n% do preço #

print('{:=^50}'.format(' I N I C I O '))
prod = float(input('Qual o preço do produto: '))
des = float(input('Qual o %desconto: '))
preq = (prod * des) / 100
pref = prod - preq
print('o produto antes valia {} \nE agora vale {}'.format(prod, pref))
print('{:=^50}'.format(' F I N A L '))
