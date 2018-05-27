#  Faca um algoritmo que escreva a tabuada de n no console #

n1 = int(input('tabuada do: '))
counter = 1
result = 0
while counter <= 10:
    result = (n1 * counter)
    print(n1, 'x', counter, '=', result)
    counter += 1
