#  Faca um algoritmo que calcule area de poligonos #


def start():
    print('-------------------------------------------------------')
    print('             CALCULADORAS DE AREAS')
    print('-------------------------------------------------------')
    print('*******************************************************')
    print('   Quadrado, Circulo, Triângulo, Trapézio ou Losângo')
    print('*******************************************************')


cald = input('*** Quero calcular a área de um: ')

if (cald == 'circulo') or (cald == 'c'):
    start()
    print('')
    print('----------------------------------------')
    print('          ÁREA DE CÍRCULOS')
    print('----------------------------------------')
    pi = 3.14
    med = str(input('*** Qual a unidade de medida utilizada? > '))
    r = float(input('*** Qual o tamanho do raio? > '))
    a = pi*(r*r)
    print('*** O circulo tem área de: {:.2f}'.format(a), med, '².')

if (cald == 'triangulo') or (cald == 'tri'):
    start()
    print('')
    print('----------------------------------------')
    print('          ÁREA DE TRIANGULOS')
    print('----------------------------------------')
    med = str(input('*** Qual a unidade de medida? > '))
    b = float(input('*** Quanto mede a base? > '))
    h = float(input('*** Qual a altura? > '))
    a = (b * h) / 2
    print('*** A área do triangulo citado é: {:.2f}'.format(a), '².')

if (cald == 'trapezio') or (cald == 'tra'):
    start()
    print('----------------------------------------')
    print('          AREA DE TRAPÉZIO')
    print('----------------------------------------')
    nome = str(input('*** Qual a unidade de medida usada? > '))
    b1 = float(input('*** Qual o tamanho da primeira base? > '))
    b2 = float(input('*** Qual o tamanho da segunda base? > '))
    h = float(input('*** Qual o tamanho da altura do Trapézio? > '))
    a = ((b1+b2)*h)/2
    print('*** A área é de: {:.2f}'.format(a), nome, '².')

if (cald == 'losango') or (cald == 'l'):
    start()
    print('----------------------------------------')
    print('          AREA DE LOSANGO')
    print('----------------------------------------')
    nome = str(input('*** Qual a unidade de medida usada? > '))
    l1 = float(input('*** Qual o tamanho da primeira Linha Diagonal? > '))
    l2 = float(input('*** Qual o tamanho da segunda? > '))
    a = (l1 * l2) / 2
    print('*** A área é de: {:.2f}'.format(a), nome, '².')

if (cald == 'quadrado') or (cald == 'q'):
    start()
    print('----------------------------------------')
    print('          ÁREA DE QUADRADOS')
    print('----------------------------------------')
    med = str(input('*** Qual a unidade de medida utilizada? > '))
    l1 = float(input('*** Qual o tamanho do primeiro lado? > '))
    l2 = float(input('*** Qual o tamanho do segundo lado? > '))
    a = (l1*l2)
    print('*** O quadrado tem área de: {:.2f}'.format(a), med, '².')
