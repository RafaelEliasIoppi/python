listagem = ('Lapis', 2.50,
            'Caderno', 4,
            'Borracha', 1.50,
            'Caneta', 3,
            'Livro', 30,
            'Cola', 3.40,
            'Tesoura', 5.60,
            'Mochila', 120.75)
print('==' *20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('==' *20)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')# alinhado a esquerda
    else:
        print(f'R$ {listagem[pos]:>6.2f}')#ALINHADO A DIREITA

