valores = []
maior = 0
menor = 0
posicão = 0
for c in range(0, 5):
    valores.append(int(input('Digite um valor para posição {}: '.format(c))))
    if c == 0:
        maior = valores[c]
        menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
            posicão = c
        if valores[c] < menor:
            menor = valores[c]
print('A lista digitada foi: {}'.format(valores))
print('O maior valor diditado foi: {}    na posição:' .format(maior), end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end=' ')
print()
print('O menor valor digitado foi: {}    na posição:'.format(menor), end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end=' ')




