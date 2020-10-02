def dobro(num):
    print(f'O dobro de {num} é ', end='')
    return num * 2


def triplo(num):
    print(f'O triplo de {num} é {num * 3}')


def raiz(num):
    return f'A raíz quadrada de {num} é ' + str(num ** 0.5)


#Programa principal
n = int(input('Digite um número: '))
print(dobro(n))
triplo(n)
print(raiz(n))
