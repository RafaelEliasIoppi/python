soma = 0
cont = 0
term = int(input('Digite o número de termos da PA: '))
razao = int(input('Digite a razão: '))
prim = int(input('Digite o primeiro termo da PA: '))
ultimo = prim + (term - 1) * razao
for c in range(prim, ultimo, razao):
    print('\033[31m{}\033[m'.format(c), end=' -> ')
    soma += c
print('\033[35mFIM\033[m')
print('A soma dos {} termos da PA é: \033[034m{}\033[m'.format(term, soma))
