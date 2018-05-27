#  Crie um programa que leia nomes ponha-os em uma lista (vetor) e então escolha uma ordem aleatória para a lista #

import random
cont = 1
lista = []
for i in range(0, 4):
    x = str(input('+++ Qual o nome do {}° aluno? > '.format(cont)))
    lista.append(x)  # AQUI ELE FAZ A LISTA #
    cont = cont + 1

random.shuffle(lista)
print(lista)
