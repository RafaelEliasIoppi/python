chave = True
soma = 0
cont = 0
while chave == True:
    n = int(input('Digite um valor [999] para sair: '))
    if n == 999:
        chave = False
    else:
        soma += n
        cont += 1
print('Você somou {} números no total de {}'.format(cont, soma))
print('FIM')
