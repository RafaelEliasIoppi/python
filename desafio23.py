num = int(input('Digite um número: '))
#n = str(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número: ...')
#print('Unidade: {}'.format(n[0]))
#print('Dezena: {}'.format(n[1]))
#print('Centena: {} '.format(n[2]))
#print('Milhar: {}'.format(n[3]))
print('Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {} '.format(u, d, c, m))

