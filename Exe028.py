#  Faca um algotimo que diga se uma pessoa com o nome x tem ou não 'Silva' no nome #

nome = str(input('Qual o seu nome > '))
ts = nome.upper().find('SILVA')

if ts >= 0:
    print('Seu nome tem Silva!!')
else:
    print('Seu nome NÃO tem Silva...')
