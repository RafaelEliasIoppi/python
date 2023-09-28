lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar [S]/[N]: '))
    if resp in 'Nn':
       break
for i, v in enumerate(lista):
    if v % 2 == 0:
       pares.append(v)
    elif v % 2 == 1:
       impares.append(v)
print(lista)
print('Pares: {}'.format(pares))
print('Impares: {}'.format(impares))
