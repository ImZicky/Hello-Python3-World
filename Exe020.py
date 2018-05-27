#  Faca um algoritmo que calcule COSSENO, TANGENTE e SENO de um angulo x #

import math
print('{:+^50}'.format(' I N I C I O '))
print('-'*50)
ang = int(input('+++ Diga um angulo ai meu velho: '))
print('-'*50)
an = math.radians(ang)
cos = math.cos(an)
seno = math.sin(an)
tang = math.tan(an)
print('+++ O cosseno do angulo {} é: {:.2f} \n+++ O seno é {:.2f} \n+++ A tangente é: {:.2f}'.format(ang, cos, seno, tang))
print('-'*50)
print('{:+^50}'.format(' F I N A L '))
