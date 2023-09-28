termos = int(input('Digite o número de termos da PA: '))
razao = int(input('Digite a razão: '))
primeiro = int(input('Digite o primeiro termo: '))
ultimo = primeiro + (termos - 1) * razao
c = 1
soma = primeiro
while c <= termos:
      print('{} ->'.format(soma), end=' ')
      soma += razao
      c += 1
print('FIM')
