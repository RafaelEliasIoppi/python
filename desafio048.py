soma = 0
n = 0
for cont in range(1 , 501, 2):
    if cont % 3 == 0:
        soma = soma + cont # soma += cont
        n = n + 1  # n+= 1
        #print(soma, end=' ')
print('Soma dos {} valores eh: {}'.format(n, soma))

