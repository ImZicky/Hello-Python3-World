#  Brinque com a biblioteca Math #
import math

num = float(input(' +++ NÚMERO: '))
raiz = math.sqrt(num)
prabaixo = math.floor(num)
pracima = math.ceil(num)
truncado = math.trunc(num)
fatorial = math.factorial(num)
pot = pow(num, 2)


print(num, '\n', "{:.2f}\n".format(raiz), prabaixo, '\n', pracima, '\n', truncado, '\n',fatorial, '\n', pot)
