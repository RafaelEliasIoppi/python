cont = 0
tot = 0
while True:
    n = int(input('Digite o valor que for quer ver a tabuada: '))
    print('--=--' *6)
    if n < 0:
        break
    for cont in range(0, 10):
        cont += 1
        tot = n * cont
        print(f'{n} X {cont}: {tot} ')
    print('--=--' *6)
print('FIM')



