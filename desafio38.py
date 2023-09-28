n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
maior = n1
if n2 > n1:
    maior = n2
    print('O número: {} é MAIOR que: {}'.format(maior, n1))
elif n1 == n2:
    print('O número: {} e {} sâo IGUAIS'.format(n1, n2))
else:
    print('o número: {} é MAIOR que: {}'.format(maior, n2))