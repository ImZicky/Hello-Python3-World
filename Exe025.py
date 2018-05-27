#  Brinque um pouco mais com metodos de str  #

nome = str(input('+++ Qual o seu nome Completo? > ')).strip()
print("Em maiusculas: {}".format(nome.upper()))
print('Em minusculas {}'.format(nome.lower()))
nome = nome.split()
nospace = ''.join(nome)
print('Quantas Letras ao Todo: {}'.format(len(nospace)))
print('Seu primeiro nome é {} e tem: {} letras'.format(nome[0], len(nome[0])))
