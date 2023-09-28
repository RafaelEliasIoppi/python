lista = {}
lista['nome'] = str(input('Digite o nome do jogador: '))
lista['total'] = int(input('Digite o número de partidas: '))
gols = []
for c in range(0, lista['total']):
     gols.append(int(input(f'Digite o número de gols na partida {c+1}: ')))
lista['gols'] = gols
print(lista)
for k, v in lista.items():
    print(f'{k} tem valor: {v}')
cont = 0
total = 0
for pos in range(0, lista['total']):
    print('Na partida {} foram marcados {} gols'.format(cont, lista['gols'][pos]))
    total += lista['gols'][pos]
    cont += 1
print('Foram realizadas {} partidas e foram feitos {} gols'.format(cont, total))



