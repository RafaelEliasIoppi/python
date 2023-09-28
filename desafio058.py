from random import randint
from time import sleep
cont = 0
acerto = False
computador = randint(0, 10)
while not acerto:
    print('\033[34m--=--\033[m' *10)
    print('ADIVINHE O NÚMERO QUE ESTOU PENSANDO...')
    print('\033[34m--=--\033[m' *10)
    jogador = int(input('Digite o número mágico: '))
    cont += 1
    print('PROCESSANDO...')
    sleep(2)
    if jogador > computador:
        print('ERROU. O número é MENOR... Digite novamente: \n')
    elif jogador < computador:
        print('ERROU. O número é MAIOR... Digite novamente: \n')
    else:
        acerto = True
        print('PARABÉNS ACERTOU!!! Você tentou {} vezes até acertar.'.format(cont))

