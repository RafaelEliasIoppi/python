rafaelista = {}
gols = []
listao = []
while True:
    gols.clear()
    lista['nome'] = str(input('Digite o nome do jogador: '))
    lista['partidas'] = int(input(f'Quantas partidas o jogador {lista["nome"]} disputou: '))
    for c in range(0, lista['partidas']):
        gols.append(int(input('Número de Gols na partida {}: '.format(c+1))))
    lista['gols'] = gols[:]
    listao.append(lista.copy())
    while True:
        resp = str(input('Deseja continuar [S/N]:')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO - Digite S ou N')
    if resp == 'N':
        break
print('=*' * 30)
print('cod', end=' ')
for i in lista.keys():
    print(f'{i:<15}', end=' ')
print()
print('-' *45)
for k, v in enumerate(listao):
    print(f'{k:<3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-' * 45)
while True:
    busca = int(input('Digite dados de qual jogador (999 parar): '))
    if busca == 999:
        print('FIM')
        break
    if busca >= len(listao):
        print(f'ERRO NÚMERO INVALIDO! NÃO existe jogador com código {busca}')
    else:
        print(f'Levantamento do jogador {listao[busca]["nome"]}')
        for i, g in enumerate(listao[busca]['gols']):
            print(f'     No jogo {i+1} fez {g} gols')
