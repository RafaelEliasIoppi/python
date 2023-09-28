n = int(input('Digite um número para resolver seu fatorial: '))
c = n
fat = 1
print('Calculando {}!'.format(n))
while c > 0:
     print('{}'.format(c), end=' ')
     print('X' if c > 1 else '=', end=' ')
     fat *= c
     c -= 1
print(fat)
