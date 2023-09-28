from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano  do seu nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos'.format(nasc, idade))
if idade == 18:
    print('DEVE SE ALISTAR!!!!')
elif idade < 18:
    saldo = 18 - idade
    alist = saldo + atual
    print('Faltam {} anos pra você se alistar. Ano de Alistamento: {}'.format(saldo, alist))

elif idade > 18:
    saldo = idade - 18
    alist = atual - saldo
    print('Você deveria ter se alistado há {} anos.\n Ano de Alistamento: {} '.format(saldo, alist))
