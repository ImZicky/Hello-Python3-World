print('=' * 50)
print('{} VALIDADOR DE CPF'.format(" " * 15))
print('=' * 50)

array = []
cont = int(10)
i = int(0)
soma = int(0)
d1 = int(0)
d2 = int(0)

for j in range(0, 11):
    cpf = int(input("O numero do seu cpf: "))
    array.append(cpf)

while cont > 1:
        soma = soma + cont * int(array[i])
        cont = cont - 1
        i += 1

resto = soma % 11

if resto < 2:
    d1 = 0
elif resto >= 2:
    d1 = resto - 11

cont = int(11)
i = int(0)
soma = int(0)

while cont > 1:
        soma = soma + cont * int(array[i])
        cont = cont - 1
        i = i + 1

resto = soma % 11

if resto < 2:
    d2 = 0
elif resto >= 2:
    d2 = 11 - resto

if(array[9] == d1) and (array[10] == d2):
    print("CPF VALIDO")
else:
    print("CPF INVALIDO")
