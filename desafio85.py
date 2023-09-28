num = [[], []]
valor = 0
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        num[0].append(n)
    if n % 2 == 1:
        num[1].append(n)
num[0].sort()
num[1].sort()
print('Lista Completa: {}'.format(num))
print(f'Números pares: {num[0]}')
print(f'Números ímpares: {num[1]}')
