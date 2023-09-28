galera = []
dados = []
cont = 0
maior = menor = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite o peso: ')))
    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
             maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar [S]/[N]:'))
    if resp in 'Nn':
       break
print('*=' *20)
print(f'Lista completa: {galera}')
print(f'Foram cadastradas {len(galera)} pessoas')
print(f'O maior peso foi de {maior} Kgs', end=' ')
for p in galera:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi de {menor} Kgs', end= ' ')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]}')
