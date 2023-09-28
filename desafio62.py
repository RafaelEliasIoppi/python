razao = int(input('Digite a razão da PA: '))
primeiro = int(input('Digite o primeiro termo:'))
cont = 0
soma = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
          print('{} ->'.format(soma), end=' ')
          soma += razao
          cont += 1
    print('PAUSA')
    mais = int(input('Deseja acrescentar quantos termos: '))
print('Progressão finalizada com {} termos'.format(total))
print('FIM')
