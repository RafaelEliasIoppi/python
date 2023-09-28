a = int(input('Digite o primeiro valor:'))
b = int(input('Digite o segundo valor:'))
c = int(input('Digite terceiro valor:'))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('o MAIOR valor é: {}\n O MENOR valor é: {}'.format(maior, menor))


