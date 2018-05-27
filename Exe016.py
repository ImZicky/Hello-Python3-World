#  Faca um algoritmo que escreva no console todas as tabuadas de 1 a 10 usando ao menos uma estrutura for #

cont = int(1)
n = int(0)
res = int(0)
tt = int(0)
for x in range(0, 10):
    tt = tt + 1
    n = n + 1
    res = int(0)
    cont = int(0)
    print('{:->5} {}'.format(' TABUADA DO ', tt))
    for z in range(0, 10):
        cont = cont + 1
        res = n * cont
        print('{} x {} = {}'.format(n, cont, res))
