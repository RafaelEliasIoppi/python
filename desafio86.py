matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] =  int(input(f'Digite o valor para posição [{l}, {c}]: '))
print('-=' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
pares = 0
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
soma = 0
for l in range(0, 3):
    soma += matriz[l][2]
    maior = matriz[0][1]
    if matriz[l][1] > maior:
        maior = matriz[l][1]
print('-=' *15)
print('A somas dos valores pares é: {} '.format(pares))
print('A soma dos valores da coluna 3 é: {}'.format(soma))
print('A maior valor da segudna coluna é: {}'.format(maior))
print('-=' * 15)
