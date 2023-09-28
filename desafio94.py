pessoa = {}
galera = []
mulher = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome: '))
    while True:
        pessoa['sexo'] = str(input('Digite o sexo [M/F]:')).upper()[0]
        #if pessoa['sexo'] == 'F':
        #mulher.append(pessoa['nome'])
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO - DIGITE M OU F')
    pessoa['idade'] = int(input('Digite a idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar [S/N]:')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO - Digite S ou N')
    if resp == 'N':
        break
media = soma /len(galera)
print(f'A) Há {len(galera)} pessoas cadastradas')
print(f'B) A soma das idade é: {soma} e a média é: {media:5.2f}')
print('C) As mulheres cadastradas foram: ',  end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
       print(f'{p["nome"]}', end=' ')
print('\nD) As pessoas acima da média de idade são: ', end=' ')
for p in galera:
    if p['idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()
print('ENCERRADO')


