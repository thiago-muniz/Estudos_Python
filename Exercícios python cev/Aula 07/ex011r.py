def pintura():
    '''
    Função para calcular e mostrar na tela a area de uma parede e
    a quantidade de tinta necessária para pintura.
    :return: mensagem com resultado
    '''
    altura = float(input('Altura da paredeem metros: '))
    largura = float(input('Largura da parede em metros: '))
    area = altura * largura
    tinta = area / 2
    return f'A área da sua parede mede {area:.0f} m2.\nVocê precisará de {tinta:.0f} litros de tinta.'


#Programa principal
print(pintura())
