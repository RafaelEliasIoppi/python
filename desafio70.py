total = 0
cont = totmil = menor = 0
prodbarato = ''
while True:
     produto = str(input('Qual o nome do produto: ')).strip()
     preço = int(input('Digite o preço do produto: '))
     cont += 1
     total += preço
     if preço > 1000:
        totmil += 1
     if cont == 1 or preço < menor:
        menor = preço
        prodbarato = produto
     resp = ' '
     while resp not in 'SN':
        resp = str(input('Deseja continuar [S]/[N]: ')).strip().upper()[0]
     if resp == 'N':
         break
print('O Valor total de gasto foi de: R${}'.format(total))
print('Total de produtos no valor acima de R$ 1.000 é de: {}'.format(totmil))
print('O produto mais barato é: {} e custa R${}'.format(prodbarato, menor))
print('{:-^40}'.format(' FIM DO PROGRAMA '))
