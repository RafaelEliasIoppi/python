from random import randint
from time import sleep
from operator import itemgetter
jogos = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
        'jogador3': randint(1, 6), 'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = []
print('Valores sorteados: ')
for k, v in jogos.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
cont = 1
print('=*'* 20)
for k, v in ranking:
    print(f'{k} tirou: {v}  --> {cont}ºLugar')
    cont += 1

