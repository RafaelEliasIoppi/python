n = int(input('Digite um número: '))
cores = {'azul':'\033[34m', 'limpa':'\033[m'}
if (n % 2) == 0:
    print('{}{} é PAR{}'.format(cores['azul'], n, cores['limpa']))
else:
    print('{}{} é ÍMPAR{}'.format(cores['azul'],n, cores['limpa']))
