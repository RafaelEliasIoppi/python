soma = 0
cont = 0
for n in range(1, 7):
    num = int(input('Digite o {} número: '.format(n)))
    if num % 2 == 0:
        cont += 1
        soma += n
print('Voce digitou {} números PARES e a soma é: {}'.format(cont, soma))
