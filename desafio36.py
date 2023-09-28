casa = float(input('Digite o valor da casa: R$  '))
sal = float(input('Digite o valor do salário: R$ '))
ano = int(input('Digite em quantos anos pretende pagar o empréstimo: '))
prest = casa / (ano * 12)
if prest > sal *0.3:
    print('\033[1;35mEmprestimo Negado !!!\033[m Parcela de: R$ {:.2f}  --> \033[4m{:.2f}\033[m% do seu salário'.format(prest, ((prest * 100) / sal)))
else:
    print('\033[1;34mEmpréstimo APROVADO !!!\033[m Parcela de: R$ {:.2f} -->  \033[4m{:.2f}\033[m% do seu salário'.format(prest, ((prest * 100) / sal)))