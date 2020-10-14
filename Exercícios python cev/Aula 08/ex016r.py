def NumeroRealParaInteiro(numreal):
    '''
    Programa para transformar um número real em número inteiro
    :param numreal: Recebe número real a ser reduzido
    :return: retorna parte inteira do número real
    '''
    return int(numreal)


num = float(input('Digite um número real qualquer: '))
print(f'A parte inteira de {num} é {NumeroRealParaInteiro(num)}')
