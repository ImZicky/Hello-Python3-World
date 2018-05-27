#  Fatie Uma String #

teste = str('Im Running From My Shadow While It Still Chasing Me Down')
print(teste[0:5])
print(teste[6:9])
print(teste[9:14])
print(teste[15:])
print(teste[::])



cc = len(teste)

for i in range(0, cc):
    cc = cc - 1
    print(teste[cc])
print()
for i in range(0, cc):
    print(teste[i])
