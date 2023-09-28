lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    resp = str(input('Deseja Continuar [S]/[N]: ')).strip().upper()[0]
    if resp != 'S':
        print('Você digitou {} números'.format(cont))
        lista.sort(reverse=True)
        if 5 in lista:
            print('A lista tem o número 5')
        else:
            print('A lista não tem o número 5')
        break
print('Lista em Ordem Decrescente: {}'.format(lista))
