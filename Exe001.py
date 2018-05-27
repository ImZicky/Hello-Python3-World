#  Faca um algoritmo que  saiba contar de x a y e pular de n em n #

de = int(input('De: '))
ate = int(input('Até: '))
pul = int(input('Pulando de: '))
if (pul == 0) or (de == ate):
    print('error!')
while de <= ate:
    if pul > 0:
        print(de)
        de += pul
    elif pul < 0:
        print(de)
        de += -1*pul

while de >= ate:
    if pul > 0:
        print(de)
        de -= pul
    elif pul < 0:
        print(de)
        de -= -1 * pul
