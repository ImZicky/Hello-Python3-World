# Faca um algoritmo que diz se a cidade x tem nome de santo #

cidade = str(input('Qual o nome da sua cidade? > '))
ts = cidade.upper().find('SANTO')
ts2 = cidade.upper().find('SÃO')
ts3 = cidade.upper().find('SAN')

if (ts >= 0) or (ts2 >= 0) or (ts3 >= 0):
    print('Sua cidade tem nome de Santo!')
else:
    print('Sua cidade não tem nome de Santo!')
