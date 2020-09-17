'''
Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''

def leiaINT(num):
    while True:
        try:
            global i
            i = int(input(num))
        except (ValueError, TypeError):
            print(f'ERRO! Digite um número inteiro válido.')
        except (KeyboardInterrupt):
            i = 0
            print('O usuário preferiu não digitar esse número.')
            break
        else:
            break


def leiafloat(num):
    while True:
        try:
            global r
            r = float(input(num))
        except (ValueError, TypeError):
            print(f'ERRO! Digite um número real válido.')
        except (KeyboardInterrupt):
            r = 0
            print('O usuário preferiu não digitar esse número.')
            break
        else:
            break


#Programa Principal
leiaINT('Digite um número inteiro: ')
leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')