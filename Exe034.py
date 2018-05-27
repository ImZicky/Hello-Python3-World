#  Faça um programa que mostre tres numeros e diga qual é o maior e qual é o meno, usando funções #


def inicio():
    nums = []
    for i in range(0, 3):
        n = int(input('DIGA um numero ai meu velho: '))
        nums.append(n)
    return nums


def menor():
    i = 99 ** 9999
    for j in range(0, 3):
        if nums[j] < i:
            menors = nums[j]
            i = nums[j]
    return menors


def maior():
    i = 0 - 99**9999
    for j in range(0, 3):
        if nums[j] > i:
            maiors = nums[j]
            i = nums[j]
    return maiors


nums = inicio()
baixo = menor()
alto = maior()

print('O maior valor digitado foi: {}\nO menor valor digitado foi: {}'.format(alto, baixo))
