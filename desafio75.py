num = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')),
      int(input('Digite um valor: ')), int(input('Digite um valor: ')))
print('Você digitou os valores: {}'.format(num))
if num.count(9) > 0:
    print('O valor 9 apareceu {} vez '.format(num.count(9)))
else:
    print('O valor 9 não foi digitado')
if 3 in num:
    print(f'O valor 3 apareceu na posiçao {num.index(3)+1}º')
else:
    print('O valor 3 não foi digitado')
print('Os Valores pares digitados foram', end=' ')
for n in num: # faz o laço retornando o valor de cada número digitado
    if n % 2 == 0:
       print('{}'.format(n), end=' ')


