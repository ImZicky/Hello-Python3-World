#Escreva um algoritmo que leia valor em metros, e diga em centimetros e milimetros #

print('{:=^40}'.format(' INICIO '))
m = int(input('Diga uma medida em metros: '))
c = m * 100
mili = c * 10
print('')
print('{}m é igual a {}cm e {}ml'.format(m, c, mili))
print('{:=^40}'.format(' FINAL '))
