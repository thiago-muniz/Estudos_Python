def centimetro(num):
    print(f'{num}m equivale a {num * 100}cm')


def milimetro(num):
    print(f'{num}m equivale a {num * 1000}mm')


# Programa principal
medida = float(input('Digite uma medida em metros: '))
centimetro(medida)
milimetro(medida)
