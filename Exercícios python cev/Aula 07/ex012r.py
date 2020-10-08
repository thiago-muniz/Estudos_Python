def desconto(num):
    '''
    Função para calcular desconto deum produto
    :param num: percentual de desconto
    :return: mensagem com o valor do desconto calculado
    '''
    preço = float(input('Preço do produto: '))
    desconto = preço - (preço * (num/100))
    return f'O produto que custa R${preço:.2f}, com {num}% de desconto passará a valer R${desconto:.2f}.'


#Programa principal
print(desconto(5))
print(desconto(10))