#  Crie um algoritmo que leia um número e mostre seu dobro triplo ea raiz quadrada #

from math import sqrt
n = int(input('diga um número: '))
d = n * 2
t = n * 3
r = sqrt(n)
print('o dobro de {} é {} e o triplo é {} a raiz quadrada é {:.2f}'.format(n, d, t, r))
