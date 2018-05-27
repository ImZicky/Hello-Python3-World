#  Faça um algoritmo que converta temperatura por tipos de escala (Fahrenheit / Celcils / Kevin)#


def titlee():
    print('{:=^52}'.format('+++'))
    print('{:=^52}'.format(' CONVERSOR DE TEMPERATURAS '))
    print('{:=^52}'.format(''))
    print('')
    print('[Celcius [C/F] Fahrenheit]|[Kelvin [K/F]Fahrenheit]\n '
          '[Fahrenheit [F/C] Celcius]|[Kelvin [K/C] Celcius]\n '
          '[Fahrenheit [F/K] Kelvin] |[Celcius [C/K] Kelvin]')
    print('-'*52)


titlee()


res = input('Qual a conversão que você quer: ')
if res == 'C/F' or res == 'c/f':
    cel = float(input('Temperatura em celcius: '))
    fa = (cel * 1.8) + 32
    print('{:.1f}°C é igual a {:.1f}°F '.format(cel, fa))
    print('{:=^52}'.format(' F I N A L '))
elif res == 'F/C' or res == 'f/c':
    fa = float(input('Temperatura em Fahrenheit: '))
    cel = (fa - 32) / 1.8
    print('{:.1f}°F é igual a {:.1f}°C'.format(fa, cel))
    print('{:=^52}'.format(' F I N A L '))
elif res == 'C/K' or res == 'c/k':
    cel = float(input('Temperatura em Celcius: '))
    k = cel + 273
    print('{:.1f}°C é igual a {:.1f}°K'.format(cel, k))
    print('{:=^52}'.format(' F I N A L '))
elif res == 'K/C' or res == 'k/c':
    k = float(input('Temperatura em Kelvin: '))
    cel = k - 273
    print('{:.1f}°K é igual a {:.1f}°C'.format(k, cel))
    print('{:=^52}'.format(' F I N A L '))
elif res == 'F/K' or res == 'f/k':
    fa = float(input('Temperatura em Fahrenheit: '))
    cel = (fa - 32) / 1.8
    k = cel + 273
    print('{:.1f}°F é igual a {:.1f}°K'.format(fa, k))
    print('{:=^52}'.format(' F I N A L '))
elif res == 'K/F' or res == 'k/f':
    k = float(input('Temperatura em Kelvin: '))
    cel = k - 273
    fa = (cel * 1.8) + 32
    print('{:.1f}°K é igual a {:.1f}°C'.format(k, fa))
    print('{:=^52}'.format(' F I N A L '))
