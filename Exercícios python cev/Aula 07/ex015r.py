def aluguel():
    '''
    Programa para calcular o valor de um aluguel de carro.
    return: retorna uma mensagem com o valor calculado
    '''
    print('-=' * 15)
    print(f'LOCADORA CARROS'.center(30))
    print('-=' * 15)
    km = float(input('Quilometragem? '))
    dias = int(input('Dias alugado? '))
    valor = (km * 0.15) + (dias * 60)
    print('-=' * 15)
    return f'O valor a pagar sera de R${valor:.2f}'



print(aluguel())
