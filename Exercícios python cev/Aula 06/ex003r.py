
try:
    n1 = int(input('Digite um número inteiro : '))
    n2 = int(input('Digite outro número inteiro: '))
except (ValueError, TypeError):
    print('O valor inserido não é válido.')
except KeyboardInterrupt:
    print('O usuário preferiu não digitar o valor.')
else:
    print(f'A soma entre {n1} e {n2} é {n1 + n2}')

finally:
    print('Obrigado! Volte sempre!')
