#  Crie um programa que leia nomes ponha-os em uma lista (vetor) e então escolha um aleatóriamente #

import random
cont = 1
alunos = []
for i in range(0, 4):
    x = str(input('+++ Qual o nome do {}° aluno? > '.format(cont)))
    alunos.append(x)
    cont = cont + 1

print("O ALUNO ESCOLHIDO FOI ", random.choice(alunos))
