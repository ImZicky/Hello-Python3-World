senha = input('Digite uma senha de até 2 sílabas: ')

vog = ('a', 'e', 'i', 'o', 'u')
cons = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
esp = ('lha', 'lhe', 'lhi', 'lho', 'lhu', 'nha', 'nhe', 'nhi', 'nho', 'nhu')
plu = ('as', 'es', 'is', 'os', 's')
bru = ('r', 'l')

sw = False

for a in vog:  # casa
    for b in cons:
        for ae in vog:
            res = (b + a + b + ae)
            print(res)
            if res == senha:
                print('A senha é: {}'.format(res))
                sw = True
                exit()
            elif res != senha:
                for a in vog:
                    for b in cons:
                        for ae in vog:
                            for be in cons:
                                res = (b + a + be + ae)
                                print(res)
                                if res == senha:
                                    print('A senha é: {}'.format(res))
                                    sw = True
                                    exit()

if not sw:
    for b in cons: #casas 2
        for a in vog:
            for b in cons:
                for a in vog:
                    for p in plu:
                        res = (b + a + b + a + p)
                        print(res)
                        if res == senha:
                            print('A senha é: {}'.format(res))
                            sw = True
                            exit()

if not sw:
    for a in vog:  # casas
        for b in cons:
            for ae in vog:
                for p in bru:
                    res = (b + a + b + ae + p)
                    print(res)
                    if res == senha:
                        print('A senha é: {}'.format(res))
                        sw = True
                        exit()
                    elif res != senha:
                        for a in vog:
                            for b in cons:
                                for ae in vog:
                                    for be in cons:
                                        for p in bru:
                                            res = (b + a + be + ae + p)
                                            print(res)
                                            if res == senha:
                                                print('A senha é: {}'.format(res))
                                                sw = True
                                                exit()


if not sw:  # ilha/s
    for a in vog:
        for ae in esp:
            res = (a + ae)
            print(res)
            if res == senha:
                print('A senha é: {}'.format(res))
                sw = True
                exit()
            elif res != senha:
                for a in vog:
                    for ae in esp:
                        for b in cons:
                            res = (a + ae + b)
                            print(res)
                            if res == senha:
                                print('A senha é: {}'.format(res))
                                sw = True
                                exit()

if not sw:  # abelhas
    for a in vog:
        for b in cons:
            for c in vog:
                for ae in esp:
                    for be in plu:
                        res = (a + b + c + ae + be)
                        print(res)
                        if res == senha:
                            print('A senha é {}'.format(res))
                            sw = True
                            exit()

if not sw: #Pluma
    for b in cons:
        for r in bru:
            for a in vog:
                for be in cons:
                    for ae in vog:
                        res = (b + r + a + be + ae)
                        print(res)
                        if res == senha:
                            print('A senha é: {}'.format(res))
                            sw = True
                            exit()

if not sw: #Plumas
    for b in cons:
        for r in bru:
            for a in vog:
                for be in cons:
                    for ae in vog:
                        for s in cons:
                            res = (b + r + a + be + ae + s)
                            print(res)
                            if res == senha:
                                print('A senha é: {}'.format(res))
                                sw = True
                                exit()
