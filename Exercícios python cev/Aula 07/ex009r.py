def tabuada(num):
    from time import sleep
    for t in range(0, 11):
        print(f'{num} x {t:>2} = {num * t:>2}')
        sleep(1)
    print('Xx' * 10)


#Programa Principal
tabuada(7)
tabuada(8)
