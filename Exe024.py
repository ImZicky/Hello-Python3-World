#  Manipulando Strings - Brincando um pouquinhozinho #

from random import choice

cursos = ['Ciencia Da Computação', 'Sistema Da Informação', 'Analise e Desenvolvimento De Sistemas']
cc = choice(cursos)

# Fatiamento #

print('Do começo ao sétimo: ', cc[0:7])
print('Do 10 ao final pulando 2: ', cc[10::2])
print('Tudo de um jeito idiota: ', cc[::])


#  Analise #

print('Len: ', len(cc))
print('contando (a[minusculo]): ', cc.count('a'))

print('contando TODOS OS (a): ', cc.upper().count('A'))
print(cc.title())

achar = str(input('Qual palavra vc quer achar nessa variável? > '))

print('Existe essa palavra? > ', achar in cc)

if cc.find(achar) != -1:
    print(achar, ' começa na posição: ', cc.find(achar))
else:
    print('Não existe a palavra "', achar, '" nesta variável')


#  Transformação #
print(cc)
trocar = str(input('Quer Trocar Qual Palavra? > '))
poressa = str(input('Por qual? > '))
newcc = cc.replace(trocar, poressa)
print(newcc.upper())
print(newcc.lower())
print(newcc.title())
print(newcc.capitalize())
print(newcc.strip())


#  Divisão #

div = cc.split()
print(div)


#  Junção #

print(" - ".join(div))
