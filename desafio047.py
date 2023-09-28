n = int(input('Digite o número: '))
for cont in range(1, n):
    if cont % 2  == 0:
        print('Pares: {}'.format(cont, end=' '))
    else:
        print('Ímpares: {}'.format(cont, end=' '))
