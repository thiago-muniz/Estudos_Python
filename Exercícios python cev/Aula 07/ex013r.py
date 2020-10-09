def aumento(num):
    aumento = num + (num * 0.15)
    return f'O trabalhador recebe atualmente R${num:.2f}.\n' \
           f'Com o aumento passará a receber R${aumento:.2f} '

while True:
    salarioatual = float(input('Qual o salário atual do trabalhador? '))
    print(aumento(salarioatual))
    while True:
        resp = str(input("Deseja continuar?[S/N]")).strip().upper()[0]
        if resp not in "SN":
            print('Digite apenas "S" ou "N"')
        else:
            break
    if resp == 'N':
        break
print('<<< Fim do Programa! >>>')