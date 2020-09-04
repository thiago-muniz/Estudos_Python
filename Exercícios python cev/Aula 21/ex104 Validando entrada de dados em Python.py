'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
'''
def leiaINT(num):
    while True:
        a = str(input(num))
        if a.isnumeric() == True:
            return int(a)
            break
        #elif a.isalpha() == True:
            #print(f'ERRO! Digite um número inteiro válido.')
        #elif a.isspace() == True:
           #print(f'ERRO! Digite um número inteiro válido.')
        else:
            print(f'ERRO! Digite um número inteiro válido.')


#Programa principal
n = leiaINT('Digite um número: ')
print(f'Você acabou de digitar o número {n}')