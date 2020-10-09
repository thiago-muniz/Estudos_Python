def CelsiusFarenheit(temp):
    print(f'{Celsius:.1f}ºC equivalem a ', end="")
    return f'{(temp * 9/5) + 32:.1f}ºF'


def CelsiusKelvin(temp):
    print(f'{Celsius:.1f}ºC equivalem a ', end="")
    return f'{temp + 273.15}K'


Celsius = float(input('Temperatura em Graus Celsius: '))
while True:
        escala = str(input('Qual escala deseja converter? [F]arenheit ou [K]elvin')).upper().strip()[0]
        if escala == "F":
            print(CelsiusFarenheit(Celsius))
        elif escala == "K":
            print(CelsiusKelvin(Celsius))
        else:
            print('Valor Inválido!')
            resp = input('Digite 0 para finalizar o programa ou Qualquer tecla para tentar de novo.)')
            if resp == "0":
                break


print('Programa Finalizado')
