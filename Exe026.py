#  Separando números #

#  Jeito por fatiamento de String:

num = int(input('Diga um número de 0 a 9999: '))
nustr = str(num)

if (num >= 0) and (num <= 9999):
    print(nustr)
    print('A unidade é: {}'.format(nustr[3]))
    print('A dezena é: {}'.format(nustr[2]))
    print('A centena é: {}'.format(nustr[1]))
    print('A milhar é: {}'.format(nustr[0]))
else:
    print('vc digitou o numero errado!!!')

#  OBS: por fatiamento, vc só pode separar do 1000 pra 9999, ou seja, bugs caso o usuário digite '5' #

print()

#  JEITO MATEMÁTICO:

num = int(input('Diga um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(' + UNIDADE: {}\n + Dezena: {}\n + Centena: {}\n + Milhar: {}'.format(u, d, c, m))

#  OBS: Melhor porque o usuário pode digitar qualquer numero abaixo de 1000 e não irá haver bugs (Além de ser + izi)#
