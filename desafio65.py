cont = 0
chave ='S'
soma = 0
media = 0
maior = 0
menor = 0
while chave == 'S':
    n = int(input('Digite um valor: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    chave = str(input('Quer continuar: [S]/[N]: ')).strip()[0].upper()
media = soma / cont
print('Você digitou {} números e a média é: {:.2f}'.format(cont, media))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))