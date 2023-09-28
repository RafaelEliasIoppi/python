sal = int(input('Digite o valor do seu salário: '))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
        'roxo':'\033[35m'}
if sal <= 1250:
    print('Você teve um aumento de --> {}15%!!!{} Seu novo salário é --> {}{:.2f}{}'.format(cores['azul'], cores['limpa'], cores['roxo'], sal * 1.15, cores['limpa']))
if sal > 1250:
    print('Você teve um aumento de --> {}10%!!!{} Seu novo salário é --> {}{:.2f}{}'.format(cores['azul'], cores['limpa'], cores['roxo'], sal * 1.10, cores['limpa']))
