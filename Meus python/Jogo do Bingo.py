from random import randint

def cartela(lst):
    for num in lst:
        print(num, end=' ')


#Programa Principal
cartelageraljogador = []
cartelageralcomputador = []


# Sorteia números da cartela do jogador
while len(cartelageraljogador) <= 23:
        num = randint(1, 75)
        if num not in cartelageraljogador:
            cartelageraljogador.append(num)
        elif num in cartelageraljogador:
            while True:
                num = randint(1, 75)
                if num not in cartelageraljogador:
                    cartelageraljogador.append(num)
                    break
# Sorteia números da cartela do computador
while len(cartelageralcomputador) <= 23:
        num = randint(1, 75)
        if num not in cartelageralcomputador:
            cartelageralcomputador.append(num)
        elif num in cartelageralcomputador:
            while True:
                num = randint(1, 75)
                if num not in cartelageralcomputador:
                    cartelageralcomputador.append(num)
                    break

# Para Mostrar em formato de cartela [não está pronto]
#for pos, num in enumerate(cartelageraljogador):
    #for l, zeros in enumerate(cartelajogador):
        #print(l)


cartelageraljogador.sort()
cartelageralcomputador.sort()

cartela(cartelageraljogador)

print(f'cartela computador{cartelageralcomputador}')