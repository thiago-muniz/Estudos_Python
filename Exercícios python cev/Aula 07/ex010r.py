def dolar(num):
    cot = float(input('Qual a cotação do Dólar atual? '))
    conversão = cot * num
    return f'R${num:.2f} em equivalem a US${conversão:.2f}'


#Programa Principal
carteira = float(input('Quanto você deseja converter? '))
print(dolar(carteira))