#  Brinque com a biblioteca Random #

#  JOGO DA ADVINHAÇÃO #
import random

num = random.randint(0, 1)
guess = int(input(' Diga um número aí velhinho [0 ou 1] >>> '))

if guess > 1 or guess < 0:
    print('ASSIM N VALE!')

if guess == 1 or guess == 0:
    if guess == num:
        print('PARABÉNS VC ACERTOU MEU CHAPA!!!')
        print(num)
    elif guess != num:
        print('VC PERDEU')
        print(num)
