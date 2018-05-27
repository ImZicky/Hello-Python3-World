# Disseque uma String com .is#

oq = input('Escreva algo aqui: ')

print('Está todo em maiúsculo: {}'.format(oq.isupper()))
print('Está todo em minusculo: {}'.format(oq.islower()))
print('É um número: {}'.format(oq.isnumeric()))
print('É ou são letras: {}'.format(oq.isalpha()))
print('São letras e ou números: {}'.format(oq.isalnum()))
print('Só tem espaços: {}'.format(oq.isspace()))
print('Está com alguma Capital Letter: {}'.format(oq.istitle()))
print('A variável é do tipo: {}'.format(type(oq)))
