from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(""" Suas opções: 
[ 0 ] PEDDRA
[ 1 ] PAPEL
[ 2 ] TESOURA """)
jogador = int(input('Qual a sua jogada: '))
print('\033[31m-=\033[m' * 10)
print('Computador escolheu: \033[1;34m{}\033[m'.format(itens[computador]))
print('Jogador escolheu: \033[1;35m{}\033[m'.format(itens[jogador]))
print('\033[31m-=\033[m' * 10)
if computador == 0: #  computador jogou pedra
    if jogador == 0: # jogador jogou pedra
        print('EMPATE')
    elif jogador == 1:  # jogador jogou papel
        print('JOGADOR VENCE')
    elif jogador == 2: # jogador jogou tesoura
         print('COMPUTADOR VENCE')
    else:
      print('Jogada Inválida')
elif computador == 1: #  computador jogou    papel
    if jogador == 0: # jogador jogou pedra
        print('COMPUTADOR VENCE')
    elif jogador == 1: # jogador jogou papel
        print('EMPATE')
    elif jogador == 2: # jogador jogou tesoura
        print('JOGADOR VENCE')
    else:
       print('Jogada Inválida')

elif computador == 2: # jogou tesoura
    if jogador == 0: #jogador jogou pedra
        print('JOGADOR VENCE')
    elif jogador == 1: # jogador jogou papel
        print('COMPUTADOR VENCE')
    elif jogador == 2: # jogador jogou tesoura
        print('EMPATE')
    else:
        print('Jogada Inválida')