n = int(input('Digite o número de termos da sequência: ')) #sequencia de fibonaci
t1 = 1
t2 = 0
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('{} ->'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')


