from random import randint
from time import sleep
lista = []
jogos = []
cont = 0
print('-=' *30)
print('JOGA NA MEGASENA')
print('-=' *30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
         num = randint(0, 60)
         if num not in lista:
            lista.append(num)
            cont += 1
         if cont >= 6:
             break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 4, f'SORTEANDO {quant} JOGOS ', '-=' * 4 )
for i, l in enumerate(jogos):
    print('SORTEANDO...')
    print(f'JOGO {i+1}: {l}')
    sleep(1)

