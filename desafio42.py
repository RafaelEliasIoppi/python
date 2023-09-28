r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos formam um triângulo', end=' ')
    if r1 == r2 == r2:
        print('Equilátero')
    elif r1 != r2 != r3 != r1:
         print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os segmentos não formam triângulo')