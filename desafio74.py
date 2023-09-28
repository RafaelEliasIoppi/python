from random import randint
lista = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for n in lista:
    print(f'{n}', end=' ')
print('\nO maior valor é: {}'.format(max(lista)))
print('O menor valor é: {}'.format(min(lista)))
