from random import randint
from time import sleep
computador = randint(0, 5)
print('--=--' *10)
print('Vou pensa em um número entre 0 e 5. Tente Adivinhar...')
print('--=--' *10)
jogador = int(input('Digite um número entre 0 e 5: '))
print('PROCESSANDO ...')
sleep(3)
if jogador == computador:
    print('Parabéns você me venceu!!!')
else:
    print(' Eu venci!!!!\n Pensei no número: {} e não no número: {}'.format(computador, jogador))



