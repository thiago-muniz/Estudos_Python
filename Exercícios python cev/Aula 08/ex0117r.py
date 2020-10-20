def HipotenusaTrianguloRetangulo(catA, catO):
    from math import sqrt, pow
    return sqrt(pow(catA,2) + pow(catO,2))


#Programa principal
catA = float(input('Cateto Adjacente: '))
catO = float(input('Cateto Oposto: '))
print('A hipotenusa do triangulo é: ', end='')
print(HipotenusaTrianguloRetangulo(catA, catO))