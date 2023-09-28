numeros = list()
chave = True
cont = 0
while True:
   n = int(input('Digite um valor: '))
   if n not in numeros:
      numeros.append(n)
      cont += 1
   else:
       print('Valor duplicado')
   chave = str(input('Deseja continuar [S]/[N]: ')).strip()
   if chave in 'Nn':
      break
print('-='*30)
print(f'Você digitou {cont} números distintos', end=' ')
numeros.sort()
print(numeros)
print('-='*30)
